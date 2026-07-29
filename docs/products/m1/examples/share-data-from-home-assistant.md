---
title: >-
  M-1 LED Matrix Setting up scrolling text with the states of Home Assistant
  entities!
description: >-
  Step by step guide for custom scrolling text using the states of Home
  Assistant entities!
---
# Share Data From Home Assistant on Your M-1

!!! tip "Set up your segments first"

    This one expects four segments already on the display. Single panel? Follow [Segments](/products/m1/setup/m1-segments.md). Multiple panels? Use [Multiple Panels](/products/m1/setup/m1-multiple-panels.md) instead, then come back.

The <a href="https://www.home-assistant.io/integrations/wled/" target="_blank" rel="noreferrer nofollow noopener">WLED integration for Home Assistant</a> cannot push sensor values onto the matrix on its own, but the <a href="https://kno.wled.ge/interfaces/json-api/" target="_blank" rel="noreferrer nofollow noopener">WLED JSON API</a> can. This is an advanced tutorial. Follow each step closely and it works.

1\. Install **Studio Code Server** <a href="https://github.com/hassio-addons/addon-vscode" target="_blank" rel="noreferrer nofollow noopener">from the App Store</a> in Home Assistant. Click **Open Web UI** and navigate to your `configuration.yaml`.

![](/assets/m1-navigate-to-configuration-yaml.gif)

!!! danger "This file is used by Home Assistant and must be carefully edited."

    Home Assistant depends on this file to function correctly. Only make the changes exactly as outlined below. Do not add extra spaces or modify anything beyond what is specified in the instructions.

2\. Fill in the YAML generator below with your own entity IDs, then click **Copy to Clipboard** at the bottom.

<iframe src="/snippets/matrix-yaml-generator.htm" width="100%" height="700" style="border: 1px solid #ccc; border-radius: 6px;"></iframe>

3\. Back in `configuration.yaml`, paste the generated YAML on a new line at the bottom of the file.

![](/assets/m-1-matrix-automation-example-yaml.png)

4\. Open **Developer Tools** and run **Check Configuration**. A green response means you are clear to continue. Scroll down to **Restful Command**, click **Actions** at the top, type "matrix", select the command you just created, and click **Perform Action**.

![](/assets/m1-config-check-restful-actions-gif.gif)

5\. Create an **Automation** with a time pattern trigger that fires every minute.

![](/assets/m-1-matrix-automation-example-trigger.gif)

6\. Add an action, type *matrix*, and pick **RESTful command: matrix\_all\_segments**. Save and name the automation. The matrix now refreshes every minute.

![](/assets/m-1-matrix-automation-example-action.gif)

Scrolling text is capped at 32 characters per segment, so keep entity values short. Stick to one to three panels for text-heavy displays.
