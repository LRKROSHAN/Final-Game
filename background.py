# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:06:54 2023

@author: parita, roshan, rintu
"""
import pygame
class Background:
    
    def draw_background(self,screen):
        bg_surface = screen
        tile_size = 32
        bg_map = [[0 for j in range(1300 // tile_size)] for i in range(800 // tile_size)]
        tile_colors = [(255, 255, 255), (200, 200, 200)]
    
        for i in range(len(bg_map)):
            for j in range(len(bg_map[0])):
                bg_map[i][j] = tile_colors[(i + j) % 2]
        for i in range(len(bg_map)):
            for j in range(len(bg_map[0])):
                rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)
                pygame.draw.rect(bg_surface, bg_map[i][j], rect)

