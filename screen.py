# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:11:06 2023

@author: parita, rintu, roshan
"""

import pygame


#Generalized block of screen
class Screen():

    pygame.init()
    
    #Giving the title
    title = "Isekai Chronicles of the Summoned Hero"
    pygame.display.set_caption(title)
    
    font = pygame.font.Font('freesansbold.ttf', 50)

    scrn = pygame.display.set_mode((1200,700))
    
    clock = pygame.time.Clock()
    
    
    
        
        
        