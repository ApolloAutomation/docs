---
title: >-
  M-1 LED Matrix Setting up scrolling text with the states of Home Assistant
  entities!
description: >-
  Step by step guide for custom scrolling text using the states of Home
  Assistant entities!
---
# Share Data From Home Assistant on Your M-1

Turn your matrix into a live status board. Outside temperature on one line, the dryer's remaining time on the next, tomorrow's forecast under that, each line refreshing on its own without you touching anything.

The <a href="https://www.home-assistant.io/integrations/wled/" target="_blank" rel="noreferrer nofollow noopener">WLED integration for Home Assistant</a> cannot push sensor values onto the matrix on its own, but the <a href="https://kno.wled.ge/interfaces/json-api/" target="_blank" rel="noreferrer nofollow noopener">WLED JSON API</a> can. This is an advanced tutorial. Follow each step closely and it works.

!!! tip "Set up your segments first"

    This one expects four segments already on the display. Single panel? Follow [Segments](/products/m1/setup/m1-segments.md). Multiple panels? Use [Multiple Panels](/products/m1/setup/m1-multiple-panels.md) instead, then come back.

Each line is capped at **64 characters** on WLED and **32** on WLED-MM, which is worth knowing before you pick entities. A long sensor name plus its value runs out of room fast, so shorten the text you send rather than the entity itself.

1\. Install **Studio Code Server** <a href="https://github.com/hassio-addons/addon-vscode" target="_blank" rel="noreferrer nofollow noopener">from the App Store</a> in Home Assistant. Click **Open Web UI** and navigate to your `configuration.yaml`.

![](/assets/m1-navigate-to-configuration-yaml.gif)

!!! danger "This file is used by Home Assistant and must be carefully edited."

    Home Assistant depends on this file to function correctly. Only make the changes exactly as outlined below. Do not add extra spaces or modify anything beyond what is specified in the instructions.

2\. Fill in the YAML generator below with your own entity IDs, then click **Copy to Clipboard** at the bottom.

<iframe src="/snippets/matrix-yaml-generator.htm" width="100%" height="700" style="border: 1px solid #ccc; border-radius: 6px;"></iframe>

3\. Back in `configuration.yaml`, paste the generated YAML on a new line at the bottom of the file and save.

![](/assets/m-1-matrix-automation-example-yaml.png)

4\. Open **Developer Tools** and run **Check Configuration**. A green response means you are clear to continue. Then reload your new command from the **YAML** tab by clicking **RESTful Commands**, or restart Home Assistant. Until you do, the command will not show up in the next step.

5\. Still in **Developer Tools**, scroll down to **Restful Command**, click **Actions** at the top, type "matrix", select the command you just created, and click **Perform Action**. Your text should appear on the matrix straight away.

![](/assets/m1-config-check-restful-actions-gif.gif)

6\. Create an **Automation** with a time pattern trigger that fires every minute.

![](/assets/m-1-matrix-automation-example-trigger.gif)

7\. Add an action, type *matrix*, and pick **RESTful command: matrix\_all\_segments**. Save and name the automation. The matrix now refreshes every minute.

![](/assets/m-1-matrix-automation-example-action.gif)

Here is the finished board on a two panel setup, four segments each pulling a different entity.

![](/assets/m1-share-data-home-assistant-result.webp)

###### Tuning It

A minute suits temperatures and forecasts. For something that changes faster, like a countdown timer, drop the time pattern to every ten or thirty seconds. Going much below that gains you little, since the text has to finish scrolling before anyone can read it anyway.

If a line goes blank, the entity behind it is probably `unavailable` or `unknown` rather than anything being wrong with the matrix. Check it in **Developer Tools**, then **States**.

To change what a line says later, edit the RESTful command in `configuration.yaml` and reload it the same way as step 4. The automation keeps working untouched.
