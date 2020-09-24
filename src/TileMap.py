class TileMap:
<<<<<<< Updated upstream
    
=======
    def __init__(self):
        self.tileset = TileSet("Utils\Pictures\TileMap.png", (255, 0, 255), 32, 32)
        self.tileset.add_tile("path", 0, 0)
        self.tileset.add_tile("mud", 32, 0)

        self.tile_list = list()

        self.tile_list.append("path")
        self.tile_list.append("mud")
       
        self.height = 50
        self.width = 50
    
    def render(self, screen):


        #zweidarray =  [][5]
        tilename = self.tile_list[0]
        tile = self.tileset.get_tile(tilename)
        for xpos in range(0,1200,self.width):
            for ypos in range(0,800,self.height):
                screen.blit(self.tileset.image, (xpos,ypos), tile.rect)
        

        
        
>>>>>>> Stashed changes
