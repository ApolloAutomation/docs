---
title: M-1 LED Matrix General Tips
description: Multiple helpful tips to use your M-1 LED Matrix to the fullest!
---
# General Tips

=== "WLED"

    Your M-1 runs stock, upstream <a href="https://kno.wled.ge/" target="_blank" rel="noreferrer nofollow noopener">WLED</a>. HUB75 matrix support lives in WLED itself now, so the M-1 no longer needs the MoonModules fork it used to ship with. Anything in the official WLED documentation applies to your device.

    [Pixel Forge](/products/m1/examples/pixel-forge.md) runs on the device at `http://<your-m1-ip>/pixelforge.htm`. It converts images to GIFs, builds scrolling text with live tokens like time and temperature, and writes the result straight to the M-1's filesystem. No external converter needed.

=== "WLED-MM"

    The M-1 LED Matrix is using <a href="https://github.com/MoonModules/WLED-MM" target="_blank" rel="noreferrer nofollow noopener">WLED MoonModules</a> which is a fork of WLED that supports the Hub75 Matrix.

    On a Rev6 controller you can move to stock WLED and keep your settings, which gets you Pixel Forge and 2x2 panel layouts. See [Upgrade to WLED](/products/m1/setup/upgrade-to-wled.md).

[Segments](/products/m1/setup/m1-segments.md) carve the matrix into areas you can control separately, which is how you get four independent lines of text on one panel. Across [multiple panels](/products/m1/setup/m1-multiple-panels.md) you can dedicate a segment to each physical panel, or run one effect across all of them.

The <a href="https://kno.wled.ge/interfaces/json-api/" target="_blank" rel="noreferrer nofollow noopener">JSON API</a> is how you drive the matrix from elsewhere, such as [pushing Home Assistant sensor values](/products/m1/examples/share-data-from-home-assistant.md) onto the display as scrolling text. Scrolling text tops out at 64 characters on WLED and 32 on WLED-MM, so keep to one to three panels for text-heavy displays.

Watch your power. Each 64x64 panel can draw about 3A at 5V, and the controller's onboard rail only covers one of them. Details are on the [Multiple Panels](/products/m1/setup/m1-multiple-panels.md) page.
