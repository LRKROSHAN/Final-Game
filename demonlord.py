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
boss_sprite = pygame.image.load('boss.png')
# Boss class
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = boss_sprite
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        
pygame.quit()