import emptyTile
import redTile
import blueTile
import greenTile


def getTile(tile, x, y, size):
    if tile == "empty":
        return emptyTile.EmptyTile(x, y, size)
    if tile == "red":
        return redTile.RedTile(x, y, size)
    if tile == "blue":
        return blueTile.BlueTile(x, y, size)
    if tile == "green":
        return greenTile.GreenTile(x, y, size)