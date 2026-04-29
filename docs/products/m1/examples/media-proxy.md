---
title: Media Proxy
description: Stream GIFs, YouTube videos, still images, and album art to your M-1 LED Matrix
---
# Media Proxy

The <a href="https://github.com/stuartparmenter/media-proxy" target="_blank" rel="noreferrer nofollow noopener">Media Proxy</a> is a Home Assistant add-on that takes almost any media URL, resizes and decodes it for your panel, and streams the result to the M-1 over the network. It's how the M-1 ESPHome firmware plays animated GIFs, YouTube videos, still images, and album art on a 64x64 panel without you having to convert anything by hand.

!!! tip "Need to install it first?"

    Head to the **Media Proxy** section of the <a href="https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1-esphome/#media-proxy" target="_blank" rel="noreferrer nofollow noopener">M-1 ESPHome Getting Started</a> page to install the add-on, then come back here.

## What you can do

- Play **animated GIFs** from any URL (Tenor, Giphy, raw `.gif` links, etc.).
- Stream **YouTube videos** by pasting in the regular `youtube.com/watch?v=...` URL. Media Proxy automatically picks an appropriate resolution and codec for the panel, so you don't have to hunt for a 144p version.
- Display **still images** in PNG, JPEG, WebP, or APNG format.
- Show **album art with track info** during music playback by pairing Media Proxy with <a href="https://www.music-assistant.io/" target="_blank" rel="noreferrer nofollow noopener">Music Assistant</a> and the <a href="https://wiki.apolloautomation.com/products/m1/examples/sendspin/" target="_blank" rel="noreferrer nofollow noopener">SendSpin</a> page.
- Use **hardware-accelerated decode** (Intel Quick Sync, NVIDIA, VAAPI, VideoToolbox) when your Home Assistant host supports it, so streaming stays smooth without bogging down your HA host.
- Get **smart resizing for tiny panels** with high-quality Lanczos scaling and optional automatic letterbox cropping for cinematic content.

## How to use it

Once Media Proxy is installed and running, all of these things are driven from a single text entity on your M-1.

1\. Open the <a href="http://homeassistant.local:8123/config/integrations/integration/esphome" target="_blank" rel="noreferrer nofollow noopener">ESPHome integration page</a> in Home Assistant and click your M-1 device.

2\. Find the entity named **Media Source** and paste any supported URL into it.

3\. The M-1 jumps to the **Media Stream** page automatically and starts playing.

!!! tip "Don't want the panel to auto-switch?"

    Under the M-1's **Configuration** entities you'll find a switch called **Auto-switch to Media Stream on source change**. Turn it off if you'd rather change the source quietly and navigate to the Media Stream page yourself when you're ready.

## Things to try

!!! example "Animated GIF"

    Paste a Tenor or Giphy URL straight into Media Source. Animated GIFs loop automatically.

    Try it: `https://media1.tenor.com/m/cOxR1hF63Y0AAAAd/matrix-film.gif`

!!! example "YouTube video"

    Paste any normal YouTube URL into Media Source. Media Proxy picks the resolution and codec that fits the M-1 best, so a single 4K music video URL works the same as a 360p clip without any manual conversion.

    Try it: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

!!! example "Album art with Music Assistant"

    Pair Media Proxy with Music Assistant and the SendSpin page on hub75-studio to show album art and track info while music plays. The full setup is covered on the <a href="https://wiki.apolloautomation.com/products/m1/examples/sendspin/" target="_blank" rel="noreferrer nofollow noopener">SendSpin example page</a>.

## Going further

- The <a href="https://github.com/stuartparmenter/media-proxy/blob/main/README.md" target="_blank" rel="noreferrer nofollow noopener">Media Proxy README</a> covers fit modes, autocrop tuning, hardware acceleration setup, and the YAML config file if you want to tweak how content gets resized or decoded.
- The <a href="https://github.com/stuartparmenter/homeassistant-addons" target="_blank" rel="noreferrer nofollow noopener">homeassistant-addons repo</a> is the home of the Media Proxy add-on itself, including release notes and install troubleshooting.
- If you need to (re)install Media Proxy, the steps live on the <a href="https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1-esphome/#media-proxy" target="_blank" rel="noreferrer nofollow noopener">M-1 ESPHome Getting Started</a> page.
