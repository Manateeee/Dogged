from Projectile import Projectile
from TowerType import TowerType
import Utils
from Utils import load_image

class Tower:
    def __init__(self, image, colorkey, tower_width, tower_height):
        #tower attributes
        self.image = load_image(image, colorkey)
        self.tower_width = tower_width
        self.tower_height = tower_height
        self.tower_dict = dict()


    def attack(self):
        pass


    def add_tower(self, name, damage, price, attack_speed, aoe_range, range_tiles, x_position, y_position, projectile):
        self.tower_dict[name] = TowerType(
            name, 
            damage,
            price, 
            attack_speed,
            aoe_range,
            range_tiles,
            x_position, 
            y_position,
            projectile, 
            self.tower_width, 
            self.tower_height,
            )
    

    #get tower TileType
    def get_tower(self, name):
        try:
            return self.tower_dict[name]
        except KeyError:
            return None

