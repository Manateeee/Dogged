import pygame

class TowerType:
    def __init__(self, name, damage, price, attack_speed, aoe_range, range_tiles, x_position, y_position, projectile, width, length):
        self.name = name
        self.damage = damage
        self.price = price
        self.attack_speed = attack_speed
        self.aoe_range = aoe_range
        self.range_tiles = range_tiles
        self.projectile = projectile
        self.rect = pygame.rect.Rect(x_position, y_position, width, length)