import pygame
from TileSet import TileSet

class TileMap:
    def __init__(self):
        self.tileset = TileSet("Pygame-Tutorial_Tileset.jpg", (255, 0, 255), 32, 32)
        self.tileset.add_tile("grass", 0, 0)
        self.tileset.add_tile("mud", 32, 0)
        self.tileset.add_tile("water", 64, 0)
        self.tileset.add_tile("block", 0, 32)