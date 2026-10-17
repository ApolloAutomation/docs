---
title: Air Quality Notification Example
description: Build a Homey Advanced Flow that turns your AIR-1's light red and notifies everyone at home when CO2 climbs past your limit, then turns it green when the air clears.
---
# Air quality notification

<span class="difficulty lvl-1">Difficulty: Level 1</span>

This flow watches the CO2 reading on your Apollo AIR-1 and tells you when the air in your home is less than ideal. When CO2 rises above 999 ppm, the AIR-1's light turns red and everyone who's home gets a push notification with the current reading. When CO2 drops below 900 ppm, the light turns green, and 5 minutes later the flow turns it off.

!!! note "Before you start"

    This guide uses the Homey web app in a web browser, because the flow is built with Homey's Advanced Flow editor.

## Add the CO2 triggers

Start with two trigger cards: one for when CO2 gets too high, and one for when it comes back down.

1\. Open a web browser, such as Firefox, and go to <a href="https://my.homey.app" target="_blank" rel="noreferrer nofollow noopener">the Homey webapp</a>. Click the **Flow** tab on the left side.

2\. Click **New Flow**, then **Advanced Flow**.

![Homey Create a new Flow dialog with Advanced Flow selected](/assets/homey-flow-example-pic-1.png)

3\. Click **Add** and select **When**.

![Homey Advanced Flow Add menu with When highlighted](/assets/homey-flow-example-pic-2.png)

4\. In the search bar at the top, type `co2 becomes` and select the card for the sensor you want to track. This guide uses **CO2 becomes greater than** for the Apollo AIR-1 device.

![Homey card search for co2 becomes, selecting the AIR-1 CO2 becomes greater than card](/assets/homey-flow-example-pic-3-1.png)

5\. Left-click on your flow area to place the card. Your flow canvas now shows this card:

![AIR-1 CO2 becomes greater than ppm card placed on the Homey flow canvas](/assets/homey-flow-example-pic-4-1.png)

6\. Select **ppm** and type in your value. This guide uses 999.

![AIR-1 CO2 becomes greater than 999 ppm card in Homey](/assets/homey-flow-example-pic-7.png)

7\. Repeat steps 4 and 5, but this time select **CO2 becomes less than** and place it on your flow canvas. Fill in your less-than ppm value, such as 900.

![AIR-1 CO2 cards for greater than 999 ppm and less than 1000 ppm in Homey](/assets/homey-flow-example-pic-5-1.png)

!!! tip "Use 900, even though the screenshots show 1000"

    From step 7 on, the screenshots show 1000 ppm on the less-than card; use 900. The gap between 900 and 999 keeps the light from flickering between red and green when CO2 hovers around 1000 ppm.

Both triggers are now on your canvas.

## Set the light color

Next, link each trigger to a color on the AIR-1's light: red for high CO2, green once it drops.

8\. Click **Add**, select **Then**, search for `set a color`, and choose the AIR-1 device option.

![Homey card search for set a color with the AIR-1 card highlighted](/assets/homey-flow-example-pic-6.png)

9\. Draw a line from **CO2 becomes greater than 999 ppm** to the **Set a color** card. Click the 3 dots and select a color. This guide uses red to indicate a problem.

![Homey flow linking CO2 greater than 999 ppm to an AIR-1 Set a color card set to red](/assets/homey-flow-example-pic-8.png)

10\. Repeat steps 8 and 9 for the other trigger: add another **Set a color** card, connect it to **CO2 becomes less than 900 ppm**, and select green.

![Homey flow setting red above 999 ppm CO2 and green below 1000 ppm CO2 on the AIR-1](/assets/homey-flow-example-pic-10.png)

The light now turns red when CO2 is high and green when it drops.

## Send a push notification

Now add a message that tells everyone at home what the CO2 level is and what to do about it.

11\. Click **Add**, select **Then**, search for `push`, and choose **Send message to user**.

![Homey card search for push with the Send message to user card highlighted](/assets/homey-flow-example-pic-9.png)

12\. Draw a line from the red **Set a color** card to the push notification card. Then write the message:

- Type `The CO2 level in the bedroom is currently CO2 ppm. Open the Window, turn on HVAC, etc to lower this value!`
- Delete the second `CO2` (the one right before `ppm`) and leave your cursor in its place.
- Click the small tag icon, type `CO2`, and select the blue **CO2** option under **Apollo AIR-1**. The tag puts the live CO2 reading into the message.

![Homey push notification message box with the cursor on the tag icon](/assets/homey-flow-example-pic-12.png)![Homey tag search for co2 with the AIR-1 CO2 tag selected](/assets/homey-flow-example-pic-13.png)

![Homey flow sending a push notification with the AIR-1 CO2 tag after the red color card](/assets/homey-flow-example-pic-11.png)

13\. Click **User** and choose **Everyone who's home** or your preferred option.

![Homey push notification user list with Everyone who's home highlighted](/assets/homey-flow-example-pic-18.png)

High CO2 now sends the alert along with the red light.

## Turn the light off after 5 minutes

Finally, switch the light off 5 minutes after it turns green, so it doesn't stay on once the air is clear.

14\. Click **Add**, select **Delay**, and place it on your flow canvas. Change it to minutes and enter 5 for a 5 minute delay. Then drag a line from the green **Set a color** card to the delay.

![Homey flow with the green Set a color card connected to a 5 minute delay](/assets/homey-flow-example-pic-15.png)

15\. Click **Add**, select **Then**, search for `turn off`, and choose the AIR-1 device option.

![Homey card search for turn off with the AIR-1 card highlighted](/assets/homey-flow-example-pic-14.png)

16\. Drag a line from the delay you added in step 14 to the **Turn off** card. Click **Save** at the top and give your flow a name. Your finished flow looks like this:

![Completed Homey Advanced Flow for AIR-1 CO2 alerts with colors, a notification, and turn off](/assets/homey-flow-example-pic-16-1.png)

17\. Optional: add a note that reminds you what this flow does. Click **Add**, then **Note**, and type `CO2 level alert with RGB LEDs` on the note. Your flow now looks like this:

![Homey Advanced Flow with a CO2 level alert with RGB LEDs note added](/assets/homey-flow-example-pic-17-1.png)

You're done! Your flow is saved, and the next time CO2 rises above 999 ppm, your AIR-1 turns red and everyone who's home gets the alert.

[Run into issues? Join our Discord for fast support! :simple-discord:](https://link.apolloautomation.com/discord){ .md-button .md-button--primary }
