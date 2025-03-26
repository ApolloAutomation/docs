# OPNsense mDNS Auto Discover Issue

\*\*If mDNS is unchecked then Home Assistant and ESPHome will not auto discover new devices. Also, if you have different networks that Home Assistant and ESPHome devices are on, then you will need mDNS on both networks and firewall rules between them.

Install the mDNS Repeater

1\.	Click System -&gt; Click Firmware -&gt; Click Plugins -&gt; Search for "mdns" -&gt; Click the “+” symbol to install os-mdns-repeater.

![](../../../assets/opnsense-mdns-guide-pic-1.png)

2\. Confirm that the installation was successful.

![](../../../assets/opnsense-mdns-guide-pic-2.png)

3\. Refresh the page and then go to Services -&gt; mDNS Repeater (if it isn't there after refreshing your screen, verify the plugin install was successful.)-&gt; Check off "enable" -&gt; select your networks containing Home Assistant / ESPHome IoT devices -&gt; click save.

![](../../../assets/opnsense-mdns-guide-pic-3.png)

Now the Home Assistant/ESPHome auto-discover issue should be fixed!