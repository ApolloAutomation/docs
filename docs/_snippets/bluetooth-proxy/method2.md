The easiest way is to let ESPHome Device Builder add the component for you. You can also paste the single line by hand.

1\. Open ESPHome Device Builder and click **Edit** on your device. The button below opens the app right in your Home Assistant.

<a href="http://homeassistant.local:8123/5c53de3b_esphome" target="_blank" rel="noreferrer nofollow noopener" class="md-button md-button--primary"><img src="/assets/esphome-logo.svg" /> Open ESPHome Device Builder</a>

Don't have it installed yet? Add it from the App Store with the badge below first.

[![Open your Home Assistant instance and show the dashboard of the ESPHome Device Builder app.](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

2\. Click **Add Component** in the editor toolbar, search for **Bluetooth Proxy**, and click **Add**.

![](/assets/esphome-device-builder-add-ble-proxy-component.gif)

Device Builder drops a single line into your config:

```yaml
bluetooth_proxy:
```

That's all it needs. Active connections are on by default, and `bluetooth_proxy` automatically pulls in the <a href="https://esphome.io/components/esp32_ble_tracker/" target="_blank" rel="noreferrer nofollow noopener">ESP32 BLE Tracker</a> it depends on, so there's nothing else to add. Prefer to type it? Paste that one line at the top level of your YAML instead of using **Add Component**.

3\. Click **Save**, then **Install**, and choose **On the Network** to flash the new firmware over Wi-Fi.

![](/assets/esphome-device-builder-add-ble-proxy-save-validate-install.gif)

--8<-- "_snippets/bluetooth-proxy/verify.md"
