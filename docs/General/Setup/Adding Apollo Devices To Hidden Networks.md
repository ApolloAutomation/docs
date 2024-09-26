# Adding Apollo Devices To Hidden Networks

Thanks to [Panzer ](https://discord.com/channels/1126966963206361199/1126969359236071465/1184558540166266962)from our [Discord](https://discord.gg/mMNgQPyF94).

I took stock MSR1s, created a config file in ESPHome under HA, added the hidden networks and the fast\_connect option, and installed via "plug into this computer." I plugged them into my desktop, downloaded the compiled firmware, and installed it via the web-ESPHome bit. Use "install," not "prepare for first use." The YAML file is below; the secrets file has the Wi-Fi info. After that, you can unplug it from your computer and plug it in somewhere else. (Please alter the "name" and "friendly name" to something unique for each of your MSR1 units in a way that works for you. In my example, this is my 6th unit.)

![Hidden SSID 1.png](../assets/hidden-ssid-1.png)

![Hidden SSID 2.png](../assets/hidden-ssid-2.png)

```
substitutions:
  name: apollo-msr1-06
  friendly_name: Apollo MSR1 06
packages:
  ApolloAutomation.MSR-1: github://ApolloAutomation/MSR-1/Integrations/ESPHome/MSR-1.yaml
esphome:
  name: ${name}
  name_add_mac_suffix: false
  friendly_name: ${friendly_name}
api:
  encryption:
    key: makeyourownrandomkeyhere=


wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  fast_connect: True
```

[Use this link for ESPHome web https://web.esphome.io/](https://web.esphome.io/)

![Hidden 3.png](../assets/hidden-3.png)

![Hidden 4.png](../assets/hidden-4.png)

![Hidden 1.png](../assets/hidden-1.png)