# -*- coding: utf-8 -*-
"""
Created on Fri May  4 17:06:53 2023

@author: parita, roshan, rintu
"""

import pygame


class UI:
    
    def __init__(self, screen):
        self.display_screen = screen
        self.font = pygame.font.Font(None, 24)
        
    def show_health_text(self, current, full):
        health_text = f"Health: {current}/{full}"
        health_surf = self.font.render(health_text, False, "#dc4949")
        self.display_screen.blit(health_surf, (20, 10))