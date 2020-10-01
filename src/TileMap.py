from pygame import rect
from TileSet import TileSet
import numpy as np

class TileMap:
    def __init__(self, map_file):
        self.tileset = TileSet("Utils\Pictures\TileMap.png", (255, 0, 255), 50, 50)
        self.tileset.add_tile("1", 0, 0)
        self.tileset.add_tile("2", 50, 0)

        self.map_file = map_file
        
        #höhe breite der tiles
        self.height = 50
        self.width = 50

        #Map größe sollte teilbar mit heigth, width sein
        self.map_height = 1000
        self.map_width = 1000

        #Tileslist namen laden
        self.tile_list = list()
        self.tile_list.append("1")
        self.tile_list.append("2")
    
    
    def render(self, screen):
        #lade map namen in 2D array 
        map = self.loadMap(self.map_file)
        
        #Felder besetzen 
        for x in range(0, self.map_height, self.width):
            for y in range(0, self.map_width, self.height):
                tile = self.tileset.get_tile(map[int(y/self.height)][int(x/self.width)])
                screen.blit(self.tileset.image, (x,y), tile.rect)

        """
        #Tests
        screen.blit(self.tileset.image, (0,0), tile.rect)
        screen.blit(self.tileset.image, (32,32), tile.rect)
        screen.blit(self.tileset.image, (150,150), tile.rect)
        """
        
    
    #load map from txt file
    def loadMap(self, file):
        tile_field = list()

        #open map txt file
        text_file = open(file, 'r')

        #fill tile_field array with text file values
        for rows in text_file:
            row = rows.replace("\n", "")
            row = list(row)
            tile_field.append(row)
                
        
        text_file.close()

        return tile_field
        