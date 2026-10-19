---
title: Flash your lights when your team scores
description: Make your room celebrate with the Game Day Scoreboard on your M-1 by flashing your lights every time your team scores.
---
# Flash your lights when your team scores

<span class="difficulty lvl-3">Difficulty: Level 3</span>

In football, baseball, hockey, and soccer, your Apollo M-1 already throws a splash in your team's color when they score. This automation brings the rest of the room along: every time your team puts points on the board, your lights flash. The opponent's scores, kickoff, halftime, and the final leave the lights alone.

!!! warning "Not for basketball"

    A basketball game has around a hundred scoring plays, so the panel only celebrates the win, and this automation would flash your lights on almost every basket. Use it for NFL, college football, MLB, NHL, MLS, and Premier League teams.

!!! note "Before you start"

    - Your M-1 runs Game Day Scoreboard and follows your team, in **My team** or **Favorite teams**. See [Getting started (Game Day Scoreboard)](/products/m1/setup/getting-started-m1-game-day.md).
    - The scoreboard is added to Home Assistant through the ESPHome integration.
    - A light in Home Assistant that you want to flash.

## How it knows your team scored

The scoreboard's **Game Status** entity sums up the game in one line, with the team the panel follows first:

| The panel shows | Game Status reads |
| --- | --- |
| A game to come | `DAL vs PHI | Wed 7:20 PM` |
| A game in progress | `Live | DAL 14, PHI 7` |
| Halftime | `Halftime | DAL 14, PHI 7` |
| The final | `Final | DAL 31, PHI 28` |

Game Status changes when a game starts, when someone scores, and when it ends, not on every play. The automation compares the old and new value, and runs only when the same game is still live and the first score, your team's, went up. When the panel switches to a different game, the lights stay off.

!!! tip "Live games mode"

    In **Live games** the panel follows a game picked for you, and the first team listed is whichever side it follows, so the automation flashes for that team. The panel moves to another game when that game ends or after **Switch every** minutes; a switch to a different game never flashes the lights.

## Find your Game Status entity

The automation watches one entity on your scoreboard. Copy its ID now so you can paste it into the automation in the next section.

1. Go to **Settings → Devices & services** and open the **ESPHome** integration.

    [![Open your Home Assistant instance and show an integration.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=esphome)

2. Open your scoreboard's device and click **Game Status**.
3. Click the gear icon and copy the **Entity ID**. It ends with `_game_status`.

## Create the automation

This is where your lights join the celebration. You paste a ready-made automation, then point it at your Game Status entity and the light you want to flash.

1. Go to **Settings → Automations & scenes** and click **Create automation**, then **Create new automation**.

    [![Open your Home Assistant instance and show your automations.](https://my.home-assistant.io/badges/automations.svg)](https://my.home-assistant.io/redirect/automations/)

2. Open the three-dot menu in the top right and choose **Edit in YAML**.
3. Paste the automation below over what's there.
4. Replace `sensor.game_day_scoreboard_2f6a70_game_status` with your Game Status entity ID, and `light.living_room` with the light you want to flash.
5. Click **Save** and give the automation a name.

```yaml title="Flash the lights when my team scores"
alias: Flash the lights when my team scores
description: Flashes a light when the team the Game Day Scoreboard follows scores.
triggers:
  - trigger: state
    entity_id: sensor.game_day_scoreboard_2f6a70_game_status
    # Only state changes, not attribute changes
    to: ~
conditions:
  - condition: template
    value_template: >-
      {% set before = trigger.from_state.state.split(' | ') if trigger.from_state else [] %}
      {% set after = trigger.to_state.state.split(' | ') if trigger.to_state else [] %}
      {% if before | length >= 2 and after | length >= 2
            and before[0] in ['Live', 'Halftime'] and after[0] in ['Live', 'Halftime'] %}
        {% set old_line = before[1].split(', ') %}
        {% set new_line = after[1].split(', ') %}
        {% if old_line | length == 2 and new_line | length == 2 %}
          {% set old_team = old_line[0].rsplit(' ', 1) %}
          {% set new_team = new_line[0].rsplit(' ', 1) %}
          {{ new_team[0] == old_team[0]
             and new_line[1].rsplit(' ', 1)[0] == old_line[1].rsplit(' ', 1)[0]
             and (new_team[-1] | int(0)) > (old_team[-1] | int(0)) }}
        {% else %}
          false
        {% endif %}
      {% else %}
        false
      {% endif %}
actions:
  - action: light.turn_on
    target:
      entity_id: light.living_room
    data:
      flash: long
mode: single
```

Your lights now celebrate with the panel. The next time your team scores, the M-1 shows its splash and your light flashes.

!!! tip "Make it your own"

    - **Not every light can flash.** If yours ignores `flash: long`, swap the action for a scene in your team's colors, or a short color change followed by a delay and a scene that puts the room back.
    - **Football's extra point** counts as its own score, so a touchdown and the extra point after it flash twice. Add a delay of a minute at the end of the actions and keep `mode: single` to flash once per score drive.
    - **Play a sound too** by adding a `media_player.play_media` action to the same automation.
