from TileType import TileType
from Projectile import Projectile

class Tower:
    def __init__(self, name, damage, price, attack_speed, aoe_range, range_tiles, placement_width, placement_height, x_position, y_position):
        self.tiletype = TileType(name, x_position, y_position, placement_width, placement_height)
        
        #tower attributes
        self.damage = damage
        self.price = price
        self.range_tiles = range_tiles
        self.attack_speed = attack_speed
        self.aoe_range = aoe_range
        
        self.tower_dict = dict()

    def attack(self):
        pass


    def add_tower(self):
        pass
    

    #get tower TileType
    def get_tower(self, name):
        try:
            return self.tile_types[name]
        except KeyError:
            return None