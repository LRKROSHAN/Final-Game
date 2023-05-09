# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:38 2023

@author: parita, roshan, rintu
"""

import screen as s
import pygame

class Welcome_Screen(s.Screen):
        
    pygame.init()
    wlcm_scrn = pygame.display.set_mode((1200,700))
    pygame.display.set_caption(s.Screen.title)
    text = s.Screen.font.render(s.Screen.title, True, (255,255,255), (18,18,18))
    #pygame.display.set_icon(s.Screen.icon)

class GameOver_Screen(s.Screen):
    pygame.init()
    gameover_scrn = pygame.display.set_mode((1200,700))
    pygame.display.set_caption(s.Screen.title)
    
class Button(Welcome_Screen, GameOver_Screen):

    def __init__(self,x,y,img,scale):
        self.x_pos = x
        self.y_pos = y

        #Resizing the image of Button
        w = img.get_width()
        h = img.get_height()
        self.image = pygame.transform.scale(img,(int(w*scale),int(h*scale)))
        self.btn_rect = self.image.get_rect(center=(self.x_pos,self.y_pos))

        #Adding Text to the button
        #self.text_input = text_input
        #self.text = Welcome_Screen.main_font.render(self.text_input, True, (255,255,255))
        #self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw_btn_welcome(self):
        Welcome_Screen.wlcm_scrn.blit(Welcome_Screen.text,(100,150))
        Welcome_Screen.wlcm_scrn.blit(self.image, self.btn_rect)
        #Welcome_Screen.wlcm_scrn.blit(self.text,self.text_rect)
        
    def draw_btn_gameover(self):
        GameOver_Screen.gameover_scrn.blit(GameOver_Screen.text,(100,150))
        GameOver_Screen.gameover_scrn.blit(self.image,self.btn_rect)

    def checkIp(self,position):
        if position[0] in range(self.btn_rect.left, self.btn_rect.right) and position[1] in range(self.btn_rect.top, self.btn_rect.bottom):
            return True