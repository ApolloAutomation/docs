# DEV board pinouts

Generates the DEV-1 and DEV-2 pinout diagrams used on the wiki:

- `docs/assets/apollo-dev-1-pinout.webp`
- `docs/assets/apollo-dev-2-pinout.webp`

The label style follows [boardgen](https://github.com/kuba2k2/boardgen).

## Fix a label

1. Edit the pin table in `boards.json`. Each pad is a list of `kind:text` tags, listed from the board outward. The kinds are `power`, `ground`, `gpio`, `adc`, `i2c`, `uart`, `spi` and `led`.
2. Run `python tools/pinouts/make_pinout.py` from the repo root. You can also pass one board, such as `dev-2`.
3. Commit the updated `boards.json` and the regenerated `.webp` files.

Requirements: Python with [Pillow](https://pypi.org/project/Pillow/), plus Chrome or Edge to render the SVG.

Pin numbers are GPIO numbers, not module pin numbers. Check any new label against the module datasheet ([ESP32-C3-MINI-1](https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf), [ESP32-C6-MINI-1](https://www.espressif.com/sites/default/files/documentation/esp32-c6-mini-1_mini-1u_datasheet_en.pdf)).

## Board art

`dev1-board.png` and `dev2-board.png` are the EasyEDA 3D renders in `renders/`, cropped to the PCB. Only rerun `python tools/pinouts/prep_renders.py` if a render changes. If the board art moves, the pad positions in `boards.json` (`x`, `y0`, `pitch`) have to be remeasured.
