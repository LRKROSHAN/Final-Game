# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:00:57 2023

@author: parita, rintu, roshan
"""

#Screens implementations

import welcome_screen as w
import pygame

class Button(w.Welcome_Screen, w.GameOver_Screen,w.Restart_Level_Screen):

    def __init__(self,x,y,img,scale):
        self.x_pos = x
        self.y_pos = y

        #Resizing the image of Button
        w = img.get_width()
        h = img.get_height()
        self.image = pygame.transform.scale(img,(int(w*scale),int(h*scale)))
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))

    def draw(self,screen):
       screen.blit(self.image, self.rect)
        

class Screen_impl(Button):
    def __init__(self):
        pygame.init()
        self.button_img_start = pygame.image.load("Images/button.png").convert_alpha()
        self.button_img_exit = pygame.image.load("Images/button_exit.png").convert_alpha()
        self.button_start = Button(600,300,self.button_img_start,0.7)
        self.button_exit = Button(600,450,self.button_img_exit,0.76)

    def welcome_scrn_impl(self):
        w.Welcome_Screen.wlcm_scrn.fill((18,18,18))
        w.Welcome_Screen.wlcm_scrn.blit(w.Welcome_Screen.text, (100,150))
        self.button_start.draw(w.Welcome_Screen.wlcm_scrn)
        self.button_exit.draw(w.Welcome_Screen.wlcm_scrn)
        

    def gameover_scrn_impl(self):
        w.GameOver_Screen.gameover_scrn.fill((18,18,18))
        w.Welcome_Screen.gameover_scrn.blit(w.Welcome_Screen.text, (100,150))
        self.button_start.draw(w.GameOver_Screen.gameover_scrn)
        self.button_exit.draw(w.GameOver_Screen.gameover_scrn)

    def restart_level(self):
        w.Restart_Level_Screen.restart_scrn.fill((18,18,18))
        #self.button_exit = Button(600,450,self.button_img_exit,0.76)
        self.button_start.draw(w.Restart_Level_Screen.restart_scrn)
        self.button_exit.draw(w.Restart_Level_Screen.restart_scrn)

    def check_Ip(self, pos):
        if self.button_start.rect.collidepoint(pos):
            return "start"
        elif self.button_exit.rect.collidepoint(pos):
            return "exit"
        else:
            return None
        