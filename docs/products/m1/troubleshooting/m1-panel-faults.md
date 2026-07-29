---
title: M-1 Panel Troubleshooting
description: Match what your M-1 panel is showing to the likely cause and the fix.
---
# M-1 Panel Troubleshooting

Find what you are seeing in the table below and work top to bottom. The first row that matches is usually the cause.

| What you see | Likely cause | What to do |
| --- | --- | --- |
| Only one quarter of the panel lights, the rest dark | Panel size set to 32x32 instead of 64x64 | On WLED, hold the button for ten seconds to factory reset. On WLED-MM, work through [Matrix Settings](/products/m1/setup/m1-matrix-settings.md) |
| Panel completely dark, power LED on | No LED output configured, or an update failed partway | [Reflash](/products/m1/troubleshooting/m1-reflash.md) from the installer to restore factory settings |
| Whole panel dim or nearly black | Brightness turned down, or the brightness limiter was switched on | Raise brightness on the main page, then check **Enable automatic brightness limiter** is unchecked under **Config**, **LED Preferences** |
| Image repeated on every panel, or stretched sideways | Panel count set higher than the panels you actually have | Under **Config**, **LED Preferences**, match the count to your setup. See [Multiple Panels](/products/m1/setup/m1-multiple-panels.md) |
| Interleaved horizontal bands, or a doubled image | LED type set to the Quarter Scan variant | Under **Config**, **LED Preferences**, set the type back to **HUB75 (Half Scan)** |
| Colors washed out or pastel | An advanced HUB75 option was changed | Factory reset, or reflash if you are on WLED-MM |
| Colors bleeding sideways, vertical tearing | Clock phase toggled | Under **Config**, **LED Preferences**, uncheck **Reversed** |
| Faint smearing or ghosting at high brightness | The panel is running at full brightness | Lower the brightness a step. This is normal panel behaviour at 100% |
| Panel went black right after you changed LED settings | HUB75 changes need a restart | Reboot from **Info**, or power cycle the M-1 |
| Vertical lines or column artifacts | Controller not fully seated on the panel connector | Power off, re-seat the controller on the back of the matrix, power back on |

If the display is wrong on more than one count, or nothing above matches, run the full install from the <a href="https://install.apolloautomation.com/#/m-1" target="_blank" rel="noreferrer nofollow noopener">Apollo M-1 installer</a>. It restores every factory setting and you only need to enter your Wi-Fi details again.

If the symptom survives a full reinstall, it is worth contacting support with a photo of the panel.

###### Factory Reset

On WLED, holding the button for ten seconds resets the M-1 to factory settings, including the display size, without needing a computer. You will need to reconnect it to Wi-Fi afterward.

On WLED-MM, a reset does not restore the display settings on its own. Use the [reflash](/products/m1/troubleshooting/m1-reflash.md) instead.
