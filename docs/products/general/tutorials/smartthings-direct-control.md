---
title: Direct SmartThings Integration (No Hub)
description: Control SmartThings devices directly from Apollo ESPHome sensors using OAuth2 — no Home Assistant or hub required.
---

# Apollo Sensors + SmartThings Direct Control

!!! note "Compatible Devices"
    This works with any Apollo ESPHome device running ESPHome: MTR-1, MSR-2, AIR-1, and others. The OAuth2 token block is fully device-agnostic — just swap the `packages:` line for your device.

## Background

Since early 2025, Samsung SmartThings no longer supports permanent Personal Access Tokens (PAT). All API access now requires OAuth2 tokens that expire every 24 hours. This makes direct ESP32 integrations tricky — but not impossible.

This tutorial shows how to make your Apollo MTR-1 control SmartThings lights directly, with zero external servers, no Home Assistant, and no intermediate hub. The ESP32 handles the full OAuth2 token lifecycle autonomously — including persisting the refresh token across reboots using NVS flash storage. Once set up, it runs forever without any manual intervention.

**What you will achieve:**

- Zone-based presence detection on the MTR-1 that triggers SmartThings lights on/off instantly
- Fully autonomous OAuth2 token renewal every 20 hours
- Token persistence across power cuts and reboots via NVS flash

## What You Need

- Apollo MTR-1 (the same pattern works for MSR-2, AIR-1, and other Apollo ESPHome devices)
- A Samsung SmartThings account
- ESPHome installed on your PC (`pip install esphome`)
- One or more SmartThings-connected lights or switches
- About 30 minutes for the initial setup

---

## Part 1: Create a SmartThings OAuth2 App

This is a one-time setup. You need to register an OAuth2 client in the SmartThings Developer Workspace to get your `client_id` and `client_secret`.

**Step 1 — Create a project:**

1. Go to [https://developer.smartthings.com](https://developer.smartthings.com) and sign in with your Samsung account
2. Click **"Create Project"** → select **"Automation for SmartThings"**
3. Give it any name, e.g. "Apollo MTR-1"

**Step 2 — Add an OAuth2 Client:**

1. Inside your project, go to **Automation → OAuth2**
2. Set the Redirect URI to: `https://oauth.pstmn.io/v1/callback`
3. Set scopes: `r:devices:*` `w:devices:*` `x:devices:*`
4. Save — you will receive a **Client ID** and a **Client Secret**. Note both down.

---

## Part 2: Get Your First Token Pair (One-Time via Browser)

SmartThings requires a one-time browser-based authorization. After this, the ESP32 renews everything automatically.

**Step 1 — Open this URL in your browser** (replace `YOUR_CLIENT_ID`):

```
https://api.smartthings.com/oauth/authorize?client_id=YOUR_CLIENT_ID&scope=x:devices:*+w:devices:*+r:devices:*&response_type=code&redirect_uri=https://oauth.pstmn.io/v1/callback
```

Log in with your Samsung account and authorize the app. You will be redirected to a URL like:

```
https://oauth.pstmn.io/v1/callback?code=XXXXXX
```

Copy the `code` value. **It expires in about 60 seconds — act fast.**

**Step 2 — Exchange the code for tokens (PowerShell on Windows):**

```powershell
$b64 = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("YOUR_CLIENT_ID:YOUR_CLIENT_SECRET"))
Invoke-RestMethod -Method Post `
  -Uri "https://api.smartthings.com/oauth/token" `
  -Headers @{Authorization="Basic $b64"} `
  -ContentType "application/x-www-form-urlencoded" `
  -Body "grant_type=authorization_code&code=YOUR_CODE&redirect_uri=https://oauth.pstmn.io/v1/callback"
```

You will receive a response like:

```
access_token  : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
refresh_token : yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
expires_in    : 86399
```

Save both tokens. You will enter them into the ESPHome config exactly once.

**How to generate the Base64 credential string** you will need later:

```powershell
[Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("YOUR_CLIENT_ID:YOUR_CLIENT_SECRET"))
```

Save this Base64 string too.

---

## Part 3: Create Virtual Switches and Find Device IDs

To map your physical MTR-1 zones to SmartThings routines without a hub, we need Virtual Switches. The MTR-1 will send ON/OFF commands to these virtual switches, which you can then use in SmartThings to trigger your actual lights.

**Step 1 — Create Virtual Switches**

Log into your account @ [my.smartthings.com](https://my.smartthings.com) > advanced > add device > cloud > switch

**Step 2 — Find Your SmartThings Device IDs**

In the my.smartthings webapp you can copy your new virtual device IDs.

For each light or switch you want to control, you need its Device ID (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).

---

## Part 4: The ESPHome Configuration

Below is the complete, production-tested YAML. Replace all `YOUR_*` placeholders with your actual values.

!!! tip "Key Design Decisions"
    1. **`wifi: on_connect` instead of `on_boot`** — the ESP-IDF HTTP stack is not ready at boot time. Using `on_connect` with a 15-second delay guarantees the network is fully available before the first token refresh fires.
    2. **`script: mode: single`** — prevents a second token refresh from being triggered while the first one is still running. This is critical during router reboots or mesh WiFi reconnects where `wifi: on_connect` can fire multiple times in rapid succession.
    3. **`restore_value: yes` on `st_refresh_token`** — saves the latest refresh token to NVS flash after every successful renewal. It survives reboots and power cuts. The `initial_value` in the YAML is only ever used on the very first flash.
    4. **`body: !lambda |-`** — plain string bodies are silently ignored by the ESP-IDF HTTP client. The lambda syntax is required for the POST body to actually be sent.

```yaml
substitution:
  name: "apollo-mtr1"
  friendly_name: "Apollo MTR-1"

esphome:
  name: ${name}
packages:
  - github://ApolloAutomation/MTR-1/Integrations/ESPHome/MTR-1_Factory.yaml

http_request:
  id: http_request_id
  verify_ssl: false
  timeout: 10s
  buffer_size_rx: 1024
  buffer_size_tx: 512

globals:
  - id: st_access_token
    type: std::string
    restore_value: no
    initial_value: '"Bearer YOUR_ACCESS_TOKEN"'
  - id: st_refresh_token
    type: std::string
    restore_value: yes        # saved to NVS flash, survives reboots
    initial_value: '"YOUR_REFRESH_TOKEN"'

script:
  - id: refresh_oauth_token
    mode: single              # ignore duplicate calls while refresh is in progress
    then:
      - lambda: |-
          ESP_LOGI("oauth", ">>> Refresh START");
      - http_request.send:
          method: POST
          url: "https://api.smartthings.com/oauth/token"
          capture_response: true
          max_response_buffer_size: 1024
          request_headers:
            Authorization: "Basic YOUR_BASE64_CLIENT_ID_SECRET"
            Content-Type: "application/x-www-form-urlencoded"
          body: !lambda |-
            return std::string("grant_type=refresh_token&refresh_token=") + id(st_refresh_token);
          on_response:
            then:
              - lambda: |-
                  ESP_LOGI("oauth", ">>> HTTP Status: %d", response->status_code);
                  if (response->status_code == 200) {
                    json::parse_json(body, [](JsonObject root) -> bool {
                      std::string new_access = root["access_token"] | "";
                      std::string new_refresh = root["refresh_token"] | "";
                      if (!new_access.empty()) {
                        id(st_access_token) = "Bearer " + new_access;
                        ESP_LOGI("oauth", ">>> Access token updated");
                      }
                      if (!new_refresh.empty()) {
                        id(st_refresh_token) = new_refresh;
                        ESP_LOGI("oauth", ">>> Refresh token updated and saved to NVS");
                      }
                      return true;
                    });
                  } else {
                    ESP_LOGW("oauth", ">>> Refresh FAILED: %s", body.c_str());
                  }

wifi:
  on_connect:
    - delay: 15s
    - lambda: |-
        ESP_LOGI("oauth", ">>> WiFi ready, firing token refresh");
    - script.execute: refresh_oauth_token

interval:
  - interval: 20h             # tokens expire after 24h, refresh safely at 20h
    then:
      - lambda: |-
          ESP_LOGI("oauth", ">>> 20h interval token refresh");
      - script.execute: refresh_oauth_token

# ---------------------------------------------------------------
# PRESENCE ZONES
# The MTR-1 uses the LD2450 radar which provides X/Y coordinates
# in mm for up to 3 simultaneous targets. Define rectangular zones
# based on your room layout. Use the ESPHome web UI live view to
# find the right coordinates by walking through your space.
# X = left/right from sensor center, Y = distance forward
# ---------------------------------------------------------------

sensor:
  - platform: ld2450
    target_1:
      x: { name: "My T1 X", id: my_t1_x, internal: true }
      y: { name: "My T1 Y", id: my_t1_y, internal: true }
    target_2:
      x: { name: "My T2 X", id: my_t2_x, internal: true }
      y: { name: "My T2 Y", id: my_t2_y, internal: true }
    target_3:
      x: { name: "My T3 X", id: my_t3_x, internal: true }
      y: { name: "My T3 Y", id: my_t3_y, internal: true }

binary_sensor:
  # Zone 1 — replace coordinates and device ID with your own
  - platform: template
    name: "SmartThings Zone Kitchen Counter"
    lambda: |-
      return (
        (id(my_t1_x).state >= -1400 && id(my_t1_x).state <= 950 && id(my_t1_y).state >= 700 && id(my_t1_y).state <= 2700) ||
        (id(my_t2_x).state >= -1400 && id(my_t2_x).state <= 950 && id(my_t2_y).state >= 700 && id(my_t2_y).state <= 2700) ||
        (id(my_t3_x).state >= -1400 && id(my_t3_x).state <= 950 && id(my_t3_y).state >= 700 && id(my_t3_y).state <= 2700)
      );
    on_press:
      - http_request.send:
          url: "https://api.smartthings.com/v1/devices/YOUR_DEVICE_ID_1/commands"
          method: POST
          request_headers:
            Authorization: !lambda return id(st_access_token).c_str();
            Content-Type: "application/json"
          body: '{"commands": [{"component": "main", "capability": "switch", "command": "on"}]}'
    on_release:
      - http_request.send:
          url: "https://api.smartthings.com/v1/devices/YOUR_DEVICE_ID_1/commands"
          method: POST
          request_headers:
            Authorization: !lambda return id(st_access_token).c_str();
            Content-Type: "application/json"
          body: '{"commands": [{"component": "main", "capability": "switch", "command": "off"}]}'

  # Zone 2 — add as many zones as you need, one per light/switch
  - platform: template
    name: "SmartThings Zone Dining Table"
    lambda: |-
      return (
        (id(my_t1_x).state >= 1000 && id(my_t1_x).state <= 2600 && id(my_t1_y).state >= 1000 && id(my_t1_y).state <= 2000) ||
        (id(my_t2_x).state >= 1000 && id(my_t2_x).state <= 2600 && id(my_t2_y).state >= 1000 && id(my_t2_y).state <= 2000) ||
        (id(my_t3_x).state >= 1000 && id(my_t3_x).state <= 2600 && id(my_t3_y).state >= 1000 && id(my_t3_y).state <= 2000)
      );
    on_press:
      - http_request.send:
          url: "https://api.smartthings.com/v1/devices/YOUR_DEVICE_ID_2/commands"
          method: POST
          request_headers:
            Authorization: !lambda return id(st_access_token).c_str();
            Content-Type: "application/json"
          body: '{"commands": [{"component": "main", "capability": "switch", "command": "on"}]}'
    on_release:
      - http_request.send:
          url: "https://api.smartthings.com/v1/devices/YOUR_DEVICE_ID_2/commands"
          method: POST
          request_headers:
            Authorization: !lambda return id(st_access_token).c_str();
            Content-Type: "application/json"
          body: '{"commands": [{"component": "main", "capability": "switch", "command": "off"}]}'
```

---

## Part 5: Flash and Verify

```
esphome run your_config.yaml --device 192.168.x.x
```

Within 15 seconds of connecting to WiFi, you should see in the logs:

```text
[oauth] >>> WiFi ready, firing token refresh
[oauth] >>> Refresh START
[oauth] >>> HTTP Status: 200
[oauth] >>> Access token updated
[oauth] >>> Refresh token updated and saved to NVS
```

Then walk into one of your defined zones. The SmartThings API response will show `content-type: application/json` (not `text/html`) and your light turns on.

If you see `HTTP Request failed; Code: 401` — the access token has expired. A simple reboot fixes it: the `wifi: on_connect` handler will fetch a fresh token automatically.

---

## How the Token Lifecycle Works

```text
First flash:   initial_value token → refresh → new access + refresh → saved to NVS
Every 20h:     NVS refresh token   → refresh → new access + refresh → saved to NVS
After reboot:  NVS token loaded    → refresh → new access + refresh → saved to NVS
```

After the first flash, the `initial_value` in the YAML is never used again. The NVS token takes over and the chain is fully self-sustaining.

---

## Troubleshooting

!!! warning "401 on SmartThings API calls"
    The access token has expired. Reboot the device — the `wifi: on_connect` handler will fetch a fresh pair automatically.

!!! warning "400 `invalid_grant` on token refresh"
    The refresh token was invalidated. This can happen if the device was offline for more than 30 days, or if a previous refresh failed mid-way. Re-run the browser OAuth flow from Part 2, update both `initial_value` fields in your YAML, flash once, and the self-sustaining chain resumes from there.

!!! warning "400 `invalid_grant` after router reboot or power outage"
    This is the trickiest failure mode. It happens when the device reconnects to WiFi multiple times in quick succession (e.g. during a router restart), causing two parallel token refresh calls. Both use the same refresh token — one succeeds, one invalidates it. The broken token then gets saved to NVS flash and survives every reboot.

    `mode: single` on the script prevents this going forward, but if you already have a broken NVS token, here is the recovery procedure (no USB required):

    **Step 1 — Get a fresh refresh token via PowerShell:**

    ```powershell
    $b64 = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("YOUR_CLIENT_ID:YOUR_CLIENT_SECRET"))
    Invoke-RestMethod -Method Post `
      -Uri "https://api.smartthings.com/oauth/token" `
      -Headers @{Authorization="Basic $b64"} `
      -ContentType "application/x-www-form-urlencoded" `
      -Body "grant_type=refresh_token&refresh_token=LAST_KNOWN_GOOD_REFRESH_TOKEN"
    ```

    If that returns 400 too, use the browser OAuth flow from Part 2 to get a completely fresh pair.

    **Step 2 — Flash 1: add an `on_boot` override** (priority 600 runs after NVS load but before WiFi):

    ```yaml
    esphome:
      name: ${name}
      on_boot:
        priority: 600.0
        then:
          - lambda: |-
              id(st_refresh_token) = "YOUR_FRESH_REFRESH_TOKEN";
              ESP_LOGI("oauth", ">>> Boot: token override active");
    ```

    Flash OTA and wait for `HTTP Status: 200` and `Refresh token updated: xxxxxxxx-...` in the logs. Note down the full new refresh token.

    **Step 3 — Flash 2: remove the override immediately** (while device is still running): Remove the entire `on_boot` block, update `initial_value` for `st_refresh_token` to the token you just noted, keep `restore_value: yes`. Flash OTA again.

    The NVS now holds the correct token and the self-sustaining chain resumes.

!!! warning "Token refresh fires but `on_response` never runs"
    You are likely triggering the refresh from `on_boot`. The ESP-IDF HTTP stack is not ready at that point. Move to `wifi: on_connect` with a 15-second delay as shown above.

!!! warning "POST body is not being sent"
    Make sure you use `body: !lambda |- return std::string("...");` — plain YAML string values for `body:` are silently dropped by the ESP-IDF HTTP client.

---

## Adapting for Other Apollo Devices

The OAuth2 token block (globals, script, wifi on_connect, interval) is completely device-agnostic. Swap the `packages:` line for your device and add your own triggers:

- **AIR-1**: trigger a SmartThings ventilation fan when the CO₂ sensor exceeds 1200 ppm
- **MSR-2**: simple presence-based lighting in smaller rooms

---

*Tested continuously for 10+ days including multiple reboot cycles. The token chain has not required any manual intervention since initial setup.*

Thanks to Matteo for putting this tutorial together!
