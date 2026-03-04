---
title: How To Switching to Beta branch with ESPHome Device Builder
description: Tutorial for How To Switching to Beta branch with ESPHome Device Builder.
---
# Switching to Beta branch with ESPHome Device Builder

1\. In Home Assistant open the <a href="http://homeassistant.local:8123/5c53de3b_esphome" target="_blank" rel="noopener"><strong>ESPHome Device Builder</strong></a>.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=ESPHome+Device+Builder&repository_url=http%3A%2F%2Fhomeassistant.local%3A8123%2F5c53de3b_esphome)

!!! tip "Make sure you are running the latest version of ESPHome"

    You should be fully up to date with the ESPHome Device Builder before updating our sensors for ideal performance and ease of troubleshooting!

2\. Find the sensor you want to edit and click the "**EDIT**".

![](/assets/switch-to-beta-pic-1.png)

!!! danger "This is code and requires you to follow the directions carefully."

    Editing the YAML here means even a space matters. Follow the guide just as shown and ask questions if you need help!

3\. Look for the line that starts with packages and the line below it and put a \# in front of each line as shown in the second image below.

![](/assets/switch-to-beta-pic-2.png)

![](/assets/switch-to-beta-pic-3.png)

4\. Select your product below, copy the code, and paste it below the two lines you just commented out.

=== "AIR-1"

    ```yaml
    packages:
      ApolloAutomation.AIR-1:
        url: https://github.com/ApolloAutomation/AIR-1
        ref: beta
        files: [Integrations/ESPHome/AIR-1.yaml]
        refresh: 1min
    ```

=== "BTN-1"

    ```yaml
    packages:
      ApolloAutomation.BTN-1:
        url: https://github.com/ApolloAutomation/BTN-1
        ref: beta
        files: [Integrations/ESPHome/BTN-1_Minimal.yaml]
        refresh: 1min
    ```

=== "MSR-2"

    ```yaml
    packages:
      ApolloAutomation.MSR-2:
        url: https://github.com/ApolloAutomation/MSR-2
        ref: beta
        files: [Integrations/ESPHome/MSR-2.yaml]
        refresh: 1min
    ```

=== "MTR-1"

    ```yaml
    packages:
      ApolloAutomation.MTR-1:
        url: https://github.com/ApolloAutomation/MTR-1
        ref: beta
        files: [Integrations/ESPHome/MTR-1.yaml]
        refresh: 1min
    ```

=== "PLT-1 / PLT-1B"

    **PLT-1:**

    ```yaml
    packages:
      ApolloAutomation.PLT-1:
        url: https://github.com/ApolloAutomation/PLT-1
        ref: beta
        files: [Integrations/ESPHome/PLT-1_Minimal.yaml]
        refresh: 1min
    ```

    **PLT-1B:**

    ```yaml
    packages:
      ApolloAutomation.PLT-1:
        url: https://github.com/ApolloAutomation/PLT-1
        ref: beta
        files: [Integrations/ESPHome/PLT-1B_Minimal.yaml]
        refresh: 1min
    ```

=== "PUMP-1"

    ```yaml
    packages:
      ApolloAutomation.PUMP-1:
        url: https://github.com/ApolloAutomation/PUMP-1
        ref: beta
        files: [Integrations/ESPHome/PUMP-1_Minimal.yaml]
        refresh: 1min
    ```

=== "R_PRO-1"

    **Ethernet:**

    ```yaml
    packages:
      ApolloAutomation.R_PRO-1:
        url: https://github.com/ApolloAutomation/R_PRO-1
        ref: beta
        files: [Integrations/ESPHome/R_PRO-1_ETH.yaml]
        refresh: 1min
    ```

    **WiFi:**

    ```yaml
    packages:
      ApolloAutomation.R_PRO-1:
        url: https://github.com/ApolloAutomation/R_PRO-1
        ref: beta
        files: [Integrations/ESPHome/R_PRO-1_W.yaml]
        refresh: 1min
    ```

=== "TEMP-1 / TEMP-1B"

    **TEMP-1:**

    ```yaml
    packages:
      ApolloAutomation.TEMP-1:
        url: https://github.com/ApolloAutomation/TEMP-1
        ref: beta
        files: [Integrations/ESPHome/TEMP-1_Minimal_R2.yaml]
        refresh: 1min
    ```

    **TEMP-1B:**

    ```yaml
    packages:
      ApolloAutomation.TEMP-1:
        url: https://github.com/ApolloAutomation/TEMP-1
        ref: beta
        files: [Integrations/ESPHome/TEMP-1B_Minimal_R2.yaml]
        refresh: 1min
    ```

!!! warning "Do not change the name or friendly_name!"

    Changing the name can cause the install to fail due to mDNS issues. If you want to rename your device, [follow this guide](https://wiki.apolloautomation.com/products/general/setup/renaming-apollo-devices/) instead.

![](/assets/switch-to-beta-pic-4.png)

5\. Click save then install in the top right and click **Wirelessly** when prompted.

![](/assets/click-save-then-install-gif.gif)

6\. Once you see "**INFO OTA successful**" you are done. Click "**STOP**" in the bottom right to exit.

![](/assets/switch-to-beta-pic-7.png)
