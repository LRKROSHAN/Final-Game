# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:11:06 2023

@author: parita, rintu, roshan
"""

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
#load hero sprite
mob1_sprite = pygame.image.load('mob1.png')
mob2_sprite = pygame.image.load('mob2.png')
# Mob class
class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_type):
        super().__init__()
        if mob_type == 1:
            self.image = mob1_sprite
        else:
            self.image = mob2_sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)


pygame.quit()
