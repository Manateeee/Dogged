import pygame
from pygame import rect
from TileSet import TileSet
import random

class TileMap:
    def __init__(self):
        self.tileset = TileSet("Utils\Pictures\TileMap.png", (255, 0, 255), 32, 32)
        self.tileset.add_tile("path", 0, 0)
        self.tileset.add_tile("mud", 32, 0)

        self.tile_list = list()

        self.tile_list.append("path")
        self.tile_list.append("mud")
       
        self.height = 25
        self.width = 30
    
    def render(self, screen):
        
        tilename = self.tile_list[0]
        tile = self.tileset.get_tile(tilename)
        screen.blit(self.tileset.image, (0,0), tile.rect)
        