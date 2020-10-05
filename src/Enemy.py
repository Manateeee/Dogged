
import pygame


class Enemy:
    
    def __init__(self,name, damage ,speed , health , x_pos , y_pos , width, height):
        self.damage = damage
        self.name = name
        self.speed = speed
        self.health = health
        self.rectangle = pygame.rect.Rect(x_pos,y_pos,width,height)