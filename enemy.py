# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:45:40 2023

@author: parita, roshan, rintu
"""
#enemy.py
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Images/Enemy/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movement = 1
        self.movement_count = 0
        self.tile_size = 64
        self.speed = 5




    def update(self,shift):
        self.rect.x += shift
        self.rect.x += self.movement
        self.movement_count += 1
        if self.movement_count > 64:
            self.movement *= -1
            self.movement_count *= -1

            if self.movement_count == -(self.movement_count):
                abs(self.movement_count)

