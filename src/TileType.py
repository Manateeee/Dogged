import pygame

class TileType:
    def __init__(self, name, x_pos, y_pos, width, length):
        self.name = name 
        self.rect = pygame.rect.Rect(x_pos, y_pos, width, length)