# Map editor helper !

The map editor helper provides an easy way to edit maps and save them in a format compatible with the polymod map loader.

## Usage

The map can be extend or reduced and the following tile properties modified :
 - Tribe (special tribes not available);
 - Terrain;
 - Ressource (boat and ship are placeholders for aquacrop and starfish respectively at the moment);
 - City/ruin (as of january the 9th polymod map loader does not place ruins);
 - Capitals (shown in the window title when on a capital tile).

For performance reasons, changes are not displayed by default.

### Keybindings and shortcuts

When on a tile:
 - Up raises the tile's altitude, and Down lowers it (forest is considered as being between field and mountain);
 - Left and Right cycle through ressources;
 - Space cycles through city/ruin/neither;
 - Tribe initials change the climate to the corresponding tribe.

Generally:
 - Ctrl-S saves;
 - Return updates the display.

With the mouse:
 - clicking on a tile moves to that tile;
 - double-clicking on a tile toogles it's status as a capital.

### Command-line argument

If a file name is passed as argument, that file will be opened. Otherwise a new, 1-tile map will be created.

### Caution

Deleted rows are lost completely. Use the Contract button with care.

Quitting does not save. Saving will overwrite the map.json file so make sure to rename the ones you want to keep.

## Contribution

Please tell me about any errors you might encounter.

If you think you can fix it yourself or have an idea for an improvement, feel free to open a pull request.

Current missing features are aquacrop, starfish and special tribe sprites.
