---
title: Pixel Forge on the M-1
description: Convert images and build scrolling text directly on your M-1 using WLED's built-in Pixel Forge tool.
---
# Pixel Forge on the M-1

Pixel Forge ships inside WLED and runs on the M-1 itself. It converts images to GIFs sized for your matrix, builds scrolling text with live values like time and temperature, and writes everything straight to the device's filesystem. The old routine of resizing a GIF on an external site and uploading it by hand is gone.

!!! tip "WLED only"

    Pixel Forge is a stock WLED feature, so it is not in WLED-MM 14.5.1. On a Rev6 controller you can [upgrade to WLED](/products/m1/setup/upgrade-to-wled.md) and keep your settings.

Open it from the icon below the color picker in the WLED interface, or go straight to `http://<your-m1-ip>/pixelforge.htm`.

Pixel Forge has three of its own tabs: **Image Tool**, **Scrolling Text Tool**, and **Other Tools**.

## Image Tool

Turns any image into a GIF the matrix can play.

1\. Pick the segment the image will display on. One image goes to one segment.

2\. Drop an image onto the upload area, or click it and browse. JPEG, PNG, WebP, BMP, and animated GIF all work. A red frame around the preview means the format is not supported.

3\. Frame the picture. Drag the crop frame over the part you want, use the zoom and rotation sliders to fit it, and pan by dragging outside the frame.

4\. If the image has a dark background you want to drop out, raise the **Dark Pixel Cutoff** slider until those pixels go transparent.

5\. Set a filename and the output size. On a single M-1 panel that is 64 x 64. On a [2x2 grid](/products/m1/setup/m1-multiple-panels.md) it is 128 x 128.

6\. Save. The converted GIF lands on the M-1's filesystem and shows up in the effects list, ready to run.

Pixel Forge shows how much filesystem space is left as you go, which matters because the M-1 stores these images on the device.

## Scrolling Text Tool

Configures WLED's Scrolling Text effect without editing segment names by hand.

Pick the target segment, type your message, and apply it with the checkmark. Speed, text size, and color palette are all on the same screen.

The useful part is the dynamic tokens. Insert date, time, or temperature and the text updates itself instead of showing a fixed string. For values that come from elsewhere in your house, [push them from Home Assistant over the JSON API](/products/m1/examples/share-data-from-home-assistant.md) instead.

## Other Tools

Downloads extra utilities, such as PixelPaint for drawing on the matrix pixel by pixel. Anything you download stays on the device until you delete it, and works offline afterward.

On WLED-MM the equivalent workflow is [resizing a GIF externally and uploading it](/products/m1/examples/add-gifs-to-wled.md).
