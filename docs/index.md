---
title: Home Assistant Integration
description: Guide to integrating Apollo Automation devices with the Home Assistant smart home platform.
---
<img src="https://imagedelivery.net/VXI8oYYsJOyBOIySOviPCQ/4e7161b4-573c-40fa-0465-648a99bafe00/public" height="344" width="900" />

!!! info "Welcome to Apollo Automation Docs!"

    Your go-to resource for setup guides, troubleshooting, and tips for every Apollo device. Found an error or need help? [Open a GitHub issue](https://github.com/ApolloAutomation/docs/issues), hop into our [Discord](https://dsc.gg/apolloautomation), or email [support@apolloautomation.com](mailto:support@apolloautomation.com).

### Not Sure Which mmWave Sensor to Get?

```mermaid
flowchart TD
    START([Which Apollo mmWave sensor is right for me?])

    START --> Q1{Do you need PoE or\nEthernet connectivity?}

    Q1 -->|Yes| RPRO
    Q1 -->|No| Q2{Do you need to track\nmultiple people in zones?}

    Q2 -->|Yes| Q3{Do you also need reliable\nstill detection?\ne.g. sleeping, sitting on a couch}
    Q2 -->|No| MSR

    Q3 -->|Yes| RPRO
    Q3 -->|No| MTR

    MSR("<b>MSR-2</b><br/>Best-in-class still detection<br/>Single person · Close to far range<br/>Great for: bedrooms, offices, bathrooms")
    MTR("<b>MTR-1</b><br/>Track up to 3 people in up to 3 zones<br/>Great for: living rooms, open spaces")
    RPRO("<b>R-PRO-1</b><br/>Best of both worlds<br/>PoE · Ethernet · Wi-Fi · USB-C<br/>LD2450 zones + optional LD2412 still detection addon")

    classDef product fill:#daa520,stroke:#9a7510,color:#000,font-weight:bold,rx:8
    classDef question fill:#1e1e2e,stroke:#555,color:#eee
    classDef start fill:#2d2d2d,stroke:#daa520,color:#daa520,font-weight:bold

    class MSR,MTR,RPRO product
    class Q1,Q2,Q3 question
    class START start
```

### Most Popular

* [Getting started with your brand new Apollo device](https://wiki.apolloautomation.com/products/general/setup/getting-started/)
* [Updating Firmware](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/updating-firmware/)
* [Add Bluetooth Proxy functionality to your Apollo device](https://wiki.apolloautomation.com/products/general/setup/bluetooth-proxy/)

### Radar & Zones

* [Tuning out false positives with the MSR-2](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/mmwave-videos/)
* [Setting up zones on MTR-1 with the HLK app](https://wiki.apolloautomation.com/products/mtr1/setup/zones-hlk/)
* [Beta test our new Zone Mapper tool!](https://github.com/ApolloAutomation/zone-mapper) - [Use this custom card along with Zone Mapper!](https://github.com/ApolloAutomation/zone-mapper-card)
* [Tune your new R-PRO-1 PoE mmWave sensor](https://wiki.apolloautomation.com/products/rpro1/calibrating-and-updating/zones-ha/)

### Quick References

* [Understanding your AIR-1 and the various sensors it exposes](https://wiki.apolloautomation.com/products/air1/setup/general-tips/)
* [How to re-calibrate your CO<sub>2</sub> sensor](https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/)
* [Put your Apollo devices to sleep!](https://wiki.apolloautomation.com/products/general/battery-sensors/prevent-sleep/)
* [Setup your new M-1 LED Matrix with Multiple Panels](https://wiki.apolloautomation.com/products/m1/setup/m1-multiple-panels/)
* [3D Print your own case in any color or material](https://wiki.apolloautomation.com/products/general/links/)

<h3>Community</h3>

* [Discord - Support, community, updates, live streams](https://discord.gg/F3RZGPcuzV)
* [YouTube - Tutorials and live streams](https://www.youtube.com/@ApolloAutomation)

<h3>What is Apollo Automation?</h3>

Apollo Automation builds high-quality, affordable, open-source home automation hardware - designed and assembled in Lexington, KY. What started as a side project among friends (named after Trevor's dog, Apollo) grew into a full-fledged business driven by community feedback. We build everything in-house, keep our designs transparent, and host a monthly livestream on Discord and YouTube so you can connect with us directly.

<h3>What do we offer?</h3>

Sensors and devices that solve real problems in home automation - presence detection, air quality monitoring, plant care, and more. Every product ships with ESPHome firmware, full Home Assistant integration, and support from a team that actually uses what we build.