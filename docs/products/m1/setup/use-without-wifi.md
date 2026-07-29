---
title: Use Your M-1 Without Wi-Fi
description: Run and control the M-1 with no network at all, using its own hotspot.
---
# Use Your M-1 Without Wi-Fi

The M-1 does not need a Wi-Fi network. Out of the box it makes its own, and the panel walks you through connecting to it. You get full control with nothing sent anywhere and no internet involved, which is what you want on a boat, in an RV, at a market stall, or anywhere without a network.

### First Power-On

Plug the M-1 in. The Apollo dog appears for a few seconds, then the panel shows a setup card and keeps showing it until the device is set up. The card has the steps on it along with a QR code.

![](/assets/wled-16-boot-image-preset.webp)

1\. On your phone or laptop, open the Wi-Fi list and join the open network named **Apollo M-1**. There is no password. If your phone warns that the network has no internet and asks whether to stay connected, choose to **stay connected**. You can leave mobile data on.

2\. Point your camera at the QR code on the panel and tap the link. Your browser opens the M-1's control page.

3\. No camera? Open any browser and go to <a href="http://4.3.2.1/" target="_blank" rel="noopener">http://4.3.2.1</a>, which is printed on the card too. That address works any time you are connected to the M-1's own network.

From the control page you get everything: presets, effects, scrolling text, Pixel Paint, and GIF upload through [Pixel Forge](/products/m1/examples/pixel-forge.md), all without the M-1 ever touching a network.

### Good to Know

The setup card only shows while the M-1 has no Wi-Fi configured. Once you connect it to a network it boots straight to the Apollo dog instead, and you reach it at its normal address. You can bring the card back any time from the preset list, where it is saved as **Setup**.

The hotspot stays available as a fallback. If the M-1 ever cannot reach the Wi-Fi network it was set up on, it opens its own hotspot again and 4.3.2.1 works as above.

!!! warning "Upload GIFs from a browser, not the WLED phone app"

    The WLED app's file picker greys out image files, so GIF upload from the app does not work. This is a bug in the app itself, not the M-1. Scan the QR code or go to 4.3.2.1 in any browser and use Pixel Forge instead.

While your phone is joined to the M-1's hotspot, apps that need the internet may stall. Your phone goes back to normal as soon as you leave the network.
