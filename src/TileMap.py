from pygame import rect
from TileSet import TileSet
import numpy as np

class TileMap:
    def __init__(self, map_file):
        self.tileset = TileSet("Utils\Pictures\TileMap.png", (255, 0, 255), 32, 32)
        self.tileset.add_tile("path", 0, 0)
        self.tileset.add_tile("mud", 32, 0)

        self.map_file = map_file
        
        #höhe breite der tiles
        self.height = 50
        self.width = 50

        #Map größe sollte teilbar mit heigth, width sein
        self.map_height = 250
        self.map_width = 250

        #Tileslist namen laden
        self.tile_list = list()
        self.tile_list.append("path")
        self.tile_list.append("mud")
    
    
    def render(self, screen):
        #lade map namen in 2D array 
        map = self.loadMap(self.map_file)
        
        #Felder besetzen 
        for x in range(0, self.map_height, self.width):
            for y in range(0, self.map_width, self.height):
                tile = self.tileset.get_tile(map[int(x/50)][int(y/50)])
                screen.blit(self.tileset.image, (x,y), tile.rect)

        """
        #Tests
        screen.blit(self.tileset.image, (0,0), tile.rect)
        screen.blit(self.tileset.image, (32,32), tile.rect)
        screen.blit(self.tileset.image, (150,150), tile.rect)
        """
        
    
    #load map from txt file
    def loadMap(self, file):
        #import to create 2D Array 5*5
        tile_field = np.empty((5,5), dtype=object)
        counter = 0
        counter2 = 0
        #open map txt file
        text_file = open(file, 'r')

        #fill tile_field array with text file values
        for rows in text_file:
            if(counter >= 5):
                counter=0
                counter2+=1
            tile_field[counter][counter2] = rows.replace("\n", "")
            counter+=1
        
        text_file.close()

        return tile_field
        