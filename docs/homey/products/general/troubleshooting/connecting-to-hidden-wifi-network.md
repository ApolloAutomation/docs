# Connecting To Hidden Wi-Fi Network

!!! warning "Changing your Wi-Fi connection to fast_connect: true can lead to stability problems!"

    If you do set your device up with fast\_connect: true then it will just connect to the first access point it sees instead of scanning and connecting to the closest AP.

1\. <a target="_blank" rel="noreferrer nofollow noopener">Setup your device</a> using a regular wifi network

2\. Open your ESPHome Device Builder.

3\. Navigate to your sensor click on edit.

4\. Add the line at the bottom to your existing wifi configuration. Make sure to use the same spacing and caps just as shown below!

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  fast_connect: True
```

4\. Save and install to your device and now your device will be able to connect to hidden Wi-Fi networks!