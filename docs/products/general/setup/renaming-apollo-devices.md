---
title: Renaming Apollo Devices
description: Tutorial for How To Rename Apollo Devices in the ESPHome integration and ESPHome Device Builder!
---
# Renaming Apollo Devices

## ESPHome Integration - Part 1

1\. Click the button below to open the **ESPHome** integration page (**Settings → Devices & services → ESPHome**).

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. On the device you want to rename, click the pencil icon and enter a new name. Click **Update**, then select the name you just created.

![Renaming a BTN-1 to Smart Keys with the pencil icon on the ESPHome integration page](/assets/esphome-integration-rename-device-gif.gif)

3\. Click the 3 dots in the top right and select **Recreate Entity IDs** then select **Update**.

!!! success "It's okay if there are some entities that cannot be regenerated!"

    You will likely run into a popup showing that 2 entity IDs cannot be regenerated because they are not available. This is fine, we can manually fix these later or just ignore them as they are disabled entities and not expected to be used.

![Selecting Recreate entity IDs from the three-dot menu on a BTN-1 device page, then Update](/assets/esphome-integration-recreate-entity-ids-gif.gif)

4\. Scroll down to the Diagnostic section and click on **\+2 disabled entities**. Select each entity and replace the old name with the new name. Make sure to replace spaces with underscores as shown in the gif below!

![Opening each disabled Diagnostic entity on the BTN-1 device page and editing its entity ID](/assets/esphome-integration-manually-rename-disabled-entities-gif.gif)

## ESPHome Integration - Part 2

This section only changes the device name shown in the ESPHome integration page. It is safe to skip, but we recommend doing it to keep naming consistent.

1\. Click the button below to open the **ESPHome** integration page (**Settings → Devices & services → ESPHome**).

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2\. On the device you would like to rename, click the 3 dots icon and select **Rename** and type in your new name then click **OK**.

![Using the three-dot menu Rename option on the ESPHome integration page to rename a BTN-1 entry](/assets/esphome-integration-rename-device-for-integration-gif.gif)

!!! success "The next section is not necessary unless you use ESPHome Device Builder!"

    The next section is for ESPHome device builder which is for tinkerers and advanced users to take control of their device and edit the yaml. Please skip the next section if you do not use ESPHome Device Builder!

## ESPHome Device Builder

1\. Make sure you are already using the ESPHome Device Builder app as <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started/#connecting-to-esphome-device-builder" target="_blank" rel="noreferrer nofollow noopener">gone over in the getting started wiki articles</a>.

[![Open your Home Assistant instance and show the dashboard of an app.](https://my.home-assistant.io/badges/supervisor_app.svg)](https://my.home-assistant.io/redirect/supervisor_app/?app=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

2\. Click the 3 dots next to your new Apollo device and select **Rename hostname** then enter in the new name of your sensor and click **Rename**. This cannot have any spaces or underscores only hyphens, numbers, and lowercase letters such as "**smart-keys**". Once it finishes it will say OTA successful and you can click close to get back to the main dashboard.

![Using Rename hostname in ESPHome Device Builder to rename a BTN-1 and install the change](/assets/rename-hostname-esphome-device-builder-gif.gif)

!!! null "We are now ready to rename the friendly_name to a new name such as Smart Keys"

    This can have spaces and capital letters and will be the same name Home Assistant will give the device and all entity names!

3\. Click **Edit** then replace the text after friendly\_name with your new name such as Smart Keys. Click Save and Install in the top right once you are done with the rename and it will save and install. Once it finishes it will say OTA successful and you can click close to get back to the main dashboard.

![Editing friendly_name to Smart Keys in ESPHome Device Builder, then installing wirelessly](/assets/rename-friendiy-name-esphome-device-builder-gif.gif)

4\. Finally we should delete the device from the ESPHome Integration in Home Assistant and then add it back! Head to the **ESPHome** integration page (**Settings → Devices & services → ESPHome**). Next to the device you would like to remove, click the three dots and then **Delete**.

[![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

![Deleting the renamed BTN-1 from the ESPHome integration page using the three-dot menu](/assets/delete-device-from-esphome-device-builder-gif2.gif)

5\. Scroll up and add the new auto-discovered device. The name should be the same Friendly name you put in the ESPHome Device builder and all of your entities should be the correct name to begin with!

![Adding the rediscovered Smart Keys BTN-1 from the ESPHome integration page in Home Assistant](/assets/auto-discover-and-add-esphome-device-gif.gif)