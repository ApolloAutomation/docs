---
title: Home Assistant Integration
description: >-
  Guide to integrating Apollo Automation devices with the Home Assistant smart
  home platform.
---
<h1 style="display: none">Apollo Automation Docs</h1>

!!! info "Welcome to Apollo Automation Docs!"

    Your go-to resource for setup guides, troubleshooting, and tips for every Apollo device. Found an error or need help? [Open a GitHub issue](https://github.com/ApolloAutomation/docs/issues), hop into our [Discord](https://link.apolloautomation.com/discord), post on our [Community Forum](https://forum.apolloautomation.com/), or email [support@apolloautomation.com](mailto:support@apolloautomation.com).

<style>
  @media (min-width: 701px) {
    .apollo-esk-img {
      position: absolute !important;
      top: 50% !important;
      right: 28px !important;
      transform: translateY(-50%) !important;
      width: 280px !important;
      height: 212px !important;
      object-fit: cover !important;
      border-radius: 12px !important;
      display: block !important;
      max-width: none !important;
    }
  }
  @media (max-width: 700px) {
    .apollo-esk-card { min-height: 0 !important; padding: 24px !important; }
    .apollo-esk-text { max-width: 100% !important; }
    .apollo-esk-text h2 { font-size: 22px !important; }
    .apollo-esk-img {
      position: static !important;
      width: 100% !important;
      height: 200px !important;
      margin-top: 20px !important;
      transform: none !important;
      border-radius: 12px !important;
      object-fit: cover !important;
      display: block !important;
    }
  }
</style>

<div class="apollo-esk-card" style="background: #4379AA; border-radius: 12px; padding: 24px 28px; position: relative; overflow: hidden; min-height: 260px; margin: 1.5em 0;">
  <div class="apollo-esk-text" style="max-width: calc(100% - 320px);">
    <div style="color: #9ABD32; font-size: 13px; font-weight: 600; letter-spacing: 0.4px; text-transform: uppercase;">
      Spotlight
    </div>
    <h2 style="color: white; font-size: 28px; font-weight: 600; margin: 8px 0 6px;">ESPHome Starter Kit</h2>
    <p style="color: #D4E8F8; font-size: 15px; margin: 0 0 16px; line-height: 1.5;">Build your first smart sensor from scratch.</p>
    <div style="display: flex; flex-wrap: wrap; gap: 28px;">
      <a href="https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/start-here/" style="display: inline-flex; align-items: center; gap: 8px; background: #9ABD32; color: #1F425F; padding: 11px 22px; border-radius: 8px; font-weight: 600; font-size: 15px; text-decoration: none;">
        View the setup guide →
      </a>
      <a href="https://apolloautomation.com/products/esk-1-esphome-starter-kit" style="display: inline-flex; align-items: center; gap: 8px; background: white; color: #1F425F; padding: 11px 22px; border-radius: 8px; font-weight: 600; font-size: 15px; text-decoration: none;">
        Buy now →
      </a>
    </div>
  </div>
  <img class="apollo-esk-img" src="assets/esphome-starter-kit-at-sotoh-2026.jpg" alt="ESPHome Starter Kit" />
</div>

&nbsp;

### Which mmWave Sensor Should I Buy?

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 30, 'rankSpacing': 50}}}%%
flowchart LR
    START{{"Which Apollo mmWave sensor is right for me?"}}

    START --> Q1(["Do you need PoE or<br/>Ethernet connectivity?"])
    START -.-> GUIDE(["Deep dive into each sensor"])

    Q1 -->|Yes| RPRO
    Q1 -->|No| Q2(["Do you need to detect and track<br/>multiple people in zones?"])

    Q2 -->|Yes| Q3(["Do you also need reliable still detection?<br/>e.g. sleeping, sitting on a couch"])
    Q2 -->|No| MSR

    Q3 -->|Yes| RPRO
    Q3 -->|No| MTR

    MSR(("MSR-2<br/>Best still detection · Single person"))
    MTR(("MTR-1<br/>Up to 3 people · Up to 3 zones"))
    RPRO(("R-PRO-1<br/>PoE · Ethernet · Best of both worlds"))

    classDef product fill:#4379AA,stroke:#2d5a8a,color:#fff,font-weight:bold
    class MSR,MTR,RPRO product

    classDef guide fill:#2e7d46,stroke:#1f5630,color:#fff,font-weight:bold
    class GUIDE guide

    click MSR href "https://wiki.apolloautomation.com/products/msr2/introduction/" _blank
    click MTR href "https://wiki.apolloautomation.com/products/mtr1/introduction/" _blank
    click RPRO href "https://wiki.apolloautomation.com/products/rpro1/introduction/" _blank
    click GUIDE href "https://wiki.apolloautomation.com/products/general/choosing-an-mmwave-sensor/" _blank
```

### Most Popular

* [Getting started with your brand new Apollo device](https://wiki.apolloautomation.com/products/general/setup/getting-started/)
* [Updating Firmware](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/updating-firmware/)
* [Add Bluetooth Proxy functionality to your Apollo device](https://wiki.apolloautomation.com/products/general/setup/bluetooth-proxy/)

### Radar & Zones

* [Tuning out false positives with the MSR-2](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/mmwave-videos/)
* [Setting up zones on MTR-1 with the HLK app](https://wiki.apolloautomation.com/products/mtr1/setup/zones-hlk/)
* [Beta test our new Zone Mapper tool!](https://github.com/ApolloAutomation/zone-mapper) - [Use this custom card along with Zone Mapper!](https://github.com/ApolloAutomation/zone-mapper-card)
* [Tune your new R-PRO-1 PoE mmWave sensor](https://wiki.apolloautomation.com/products/rpro1/setup/zones-ha/)

### Quick References

* [Understanding your AIR-1 and the various sensors it exposes](https://wiki.apolloautomation.com/products/air1/setup/general-tips/)
* [How to re-calibrate your CO<sub>2</sub> sensor](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/)
* [Put your Apollo devices to sleep!](https://wiki.apolloautomation.com/products/general/battery-sensors/prevent-sleep/)
* [Setup your new M-1 LED Matrix with Multiple Panels](https://wiki.apolloautomation.com/products/m1/setup/m1-multiple-panels/)
* [3D Print your own case in any color or material](https://wiki.apolloautomation.com/products/general/links/)

### Community

* [Discord - Support, community, updates, live streams](https://link.apolloautomation.com/discord)
* [YouTube - Tutorials and live streams](https://www.youtube.com/@ApolloAutomation)

### What is Apollo Automation?

Apollo Automation builds high-quality, affordable, open-source home automation hardware - designed and assembled in Lexington, KY. What started as a side project among friends (named after Trevor's dog, Apollo) grew into a full-fledged business driven by community feedback. We build everything in-house, keep our designs transparent, and host a monthly livestream on Discord and YouTube so you can connect with us directly.

### What do we offer?

Sensors and devices that solve real problems in home automation - presence detection, air quality monitoring, plant care, and more. Every product ships with ESPHome firmware, full Home Assistant integration, and support from a team that actually uses what we build.