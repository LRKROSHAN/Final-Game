# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:00:57 2023

@author: parita, rintu, roshan
"""

#Screens implementations

import welcome_screen as w
import screen as s
import pygame
import gameover_screen as g

class Screen_impl:
    def welcome_scrn_impl(self):
        w.Welcome_Screen.wlcm_scrn.fill((18,18,18))
        button_img_start = pygame.image.load("Images/button.png").convert_alpha()
        button_start = w.Button(600,300,button_img_start,0.7)
        button_img_exit = pygame.image.load("Images/button_exit.png").convert_alpha()  
        button_exit = w.Button(600,450,button_img_exit,0.76)
        button_start.draw_btn_welcome()
        button_exit.draw_btn_welcome()
    

    #def gameover_scrn_impl_losing(self):
        
    #def gameover_scrn_impl_winning(self):
        
    #def main_scrn_impl(self):
        