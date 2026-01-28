---
title: How To Add Renaming Apollo Devices
description: Tutorial for How To Rename Apollo Devices.
---
# Renaming Apollo Devices

##### ESPHome Integration - Part 1

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>.

2\. On the device you would like to rename, click the pencil icon and enter in a new name then click **Update** and finally click the name you just created.

![](../../../assets/esphome-integration-rename-device-gif.gif)

3\. Click the 3 dots in the top right and select **Recreate Entity IDs** then select **Update**.

!!! success "It's okay if there are some entities that cannot be regenerated!"

    You will likely run into a popup showning that 2 entity IDs cannot be regenerated because they are not available. This is fine, we can manually fix these later or just ignore them as they are disabled entities and not expected to be used.

![](../../../assets/esphome-integration-recreate-entity-ids-gif.gif)

4\. Scroll down to the Diagnostic section and click on **\+2 disabled entities**. Select each entity and replace the old name with the new name. Make sure to replace spaces with underscores as shown in the gif below!

![](../../../assets/esphome-integration-manually-rename-disabled-entities-gif.gif)

##### ESPHome Integration - Part 2

This section only changes the device name shown in the ESPHome integration page. It is safe to skip, but we recommend doing it to keep naming consistent.

1\. Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>.

2\. On the device you would like to rename, click the 3 dots icon and select **Rename** and type in your new name then click **OK**.

![](../../../assets/esphome-integration-rename-device-for-integration-gif.gif)

!!! success "The next section is not necessary unless you use ESPHome Device Builder!"

    The next section is for ESPHome device builder which is for tinkerers and advanced users to take control of their device and edit the yaml. Please skip the next section if you do not use ESPHome Device Builder!

##### ESPHome Device Builder

1\. Make sure you are already using the ESPHome Device Builder app as <a href="https://wiki.apolloautomation.com/products/general/setup/getting-started/#connecting-to-esphome-device-builder" target="_blank" rel="noreferrer nofollow noopener">gone over in the getting started wiki articles</a>.

2\. Click the 3 dots next to your new Apollo device and select **Rename hostname** then enter in the new name of your sensor and click **Rename**. This cannot have any spaces or underscores only hyphens, numbers, and lowercase letters such as "**smart-keys**". Once it finishes it will say OTA successful and you can click close to get back to the main dashboard.

![](../../../assets/rename-hostname-esphome-device-builder-gif.gif)

!!! null "We are now ready to rename the friendly_name to a new name such as Smart Keys"

    This can have spaces and capital letters and will be the same name home assistant will give the device and all entity names!

3\. Click **Edit** then replace the text after friendly\_name with your new name such as Smart Keys. Click Save and Install in the top right once you are done with the rename and it will save and install. Once it finishes it will say OTA successful and you can click close to get back to the main dashboard.

![](../../../assets/rename-friendiy-name-esphome-device-builder-gif.gif)

4\. Finally we should delete the device from the ESPHome Integration in home assistant and then add it back! Head to the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" title="Click me to go to the ESPHome integrations page" target="_blank" rel="noreferrer nofollow noopener">ESPHome Integrations page</a>. Next to the device you would like to remove, click the three dots and then **Delete**.

![](../../../assets/delete-device-from-esphome-device-builder-gif2.gif)

5\. Scroll up and add the new auto-discovered device. The name should be the same Friendly name you put in the ESPHome Device builder and all of your entities should be the correct name to begin with!

![](../../../assets/auto-discover-and-add-esphome-device-gif.gif)