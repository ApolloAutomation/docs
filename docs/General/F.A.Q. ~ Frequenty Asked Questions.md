# F.A.Q. ~ Frequenty Asked Questions

#### This is where our most frequently asked questions will be for now!

#### Question:

How much power do your sensors use?

#### Answer:

All apollo sensors use 1amp or less, some of them 350-500mA.

---

#### Question:

What all can the MSR-2 LD2410B mmWave sensor go through?

#### Answer:

It can reliably go through drywall.

---

#### Question:

My MSR-2 is triggering and no one is there.

#### Answer:

We have seen this happen before - please first try to restart your radar, then factory reset your radar, then try a factory firmware flash. We also see success with users re-seating their LD2410B mmWave sensor.

---

#### Question:

How do I reset my Wi-Fi?

#### Answer:

Plug in your device then hold down the boot button for 10 seconds. The Wi-Fi credentials should be reset and it will broadcast its hotspot again.

---

#### Question:

My lux sensor doesn't seem to be working how do I fix it?

#### Answer:

The default update\_interval is 60 seconds which isnt great for automations revolving around measuring lux values. [Please follow this short guide](https://wiki.apolloautomation.com/books/general/page/how-to-edit-your-sensors-lux-update-interval "How to Edit your lux sensor update interval") to edit the lux update\_interval down to a more responsive 3-5seconds.

---

#### Question:

Do I need to push the "Clean" button for my Air-1 or setup an automation for it?

#### Answer:

No, your Air-1 will self-clean once a week per this [recommended documentation from the manufacturer.](https://sensirion.com/media/documents/6791EFA0/62A1F68F/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf)

---

#### Question:

Can your sensors be used with OpenHAB?

#### Answer:

Yes, please install [this binding](https://github.com/seime/openhab-esphome "OpenHAB-ESPHome") and then restart OpenHAB and our devices will show up to configure!

---

#### Question:

I am getting the error "Failed to import device" in ESPHome Dashboard when trying to adopt my Apollo device.

#### Answer:

Make sure you have enough free space in Home Assistant - Protip: check for old backups you can delete!

If your space is not an issue then please reboot or even try reinstalling the esphome addon and see if that helps!

---

#### Question:

#### Answer:

---

#### Question:

#### Answer:

---

### ~~General Troubleshooting Suggestions~~  


If your gates are acting strangely and reporting much more energy than they should, make sure there is no tension on the usb cable. One user reported still energy in gates 2 and 3 until the tension was removed from the cable.