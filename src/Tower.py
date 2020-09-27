from TileType import TileType

class Tower:
    def __init__(self, name, damage, price, attack_speed, aoe_range, range_tiles, placement_width, placement_height, x_position, y_position):
        self.name = name
        self.damage = damage
        self.price = price
        self.range_tiles = range_tiles
        self.attack_speed = attack_speed
        self.aoe_range = aoe_range
        self.tiletype = TileType(name, x_position, y_position, placement_width, placement_height) 