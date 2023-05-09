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
    
    #Puttong icon of the game
    #icon = pygame.image.load(r'Images/pong.ico')
    #pygame.display.set_icon(icon)
    
    font = pygame.font.Font('freesansbold.ttf', 50)

    scrn = pygame.display.set_mode((1200,700))
    
    clock = pygame.time.Clock()
        
        
        