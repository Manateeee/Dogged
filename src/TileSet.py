from TileType import TileType
import Utils

class TileSet:
    def __init__(self, image, colorkey, tile_width, tile_height):
        self.image = Utils.load_image(image, colorkey)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_types = dict()

    def add_tile(self, name, start_x, start_y):
        self.tile_types[name] = TileType(name, start_x, start_y, self.tile_width, self.tile_height)

    def get_tile(self, name):
        try:
            return self.tile_types[name]
        except KeyError:
            return None