---
title: M-1 LED Matrix General Tips
description: Multiple helpful tips to use your M-1 LED Matrix to the fullest!
---
# General Tips

The M-1 LED Matrix is using <a href="https://github.com/MoonModules/WLED-MM" target="_blank" rel="noreferrer nofollow noopener">WLED MoonModules</a> which is a fork of WLED that supports the Hub75 Matrix.

WLED uses <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-segments/" target="_blank" rel="noreferrer nofollow noopener">segments</a> which allow you to create virtual led strips (or panels) of leds to control individually. This is useful in cases where you want to <a href="https://wiki.apolloautomation.com/products/m1/setup/m1-multiple-panels/#software-setup" target="_blank" rel="noreferrer nofollow noopener">connect multiple panels and have text scrolling across the screens</a>.

Segments are also able to be used to control two panels from one controller such as making the first segment a 64x64 panel and the second segment control second 64x64 panel.

The M-1 Matrix can be controlled using the <a href="https://mm.kno.wled.ge/interfaces/json-api/" target="_blank" rel="noreferrer nofollow noopener">JSON API</a>, allowing you to do some really cool things like sending data from Home Assistant to display as scrolling text on the matrix. (For best results, use 1 to 3 panels instead of 4, as the scrolling text supports up to 32 characters.)