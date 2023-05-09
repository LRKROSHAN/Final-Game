# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:54:02 2023

@author: parita, rintu, roshan
"""
#game.py
import screen as sc
import pygame
#from pygame import mixer
import Level1_map as l1
import Level2_map as l2
import Level_final 
import dialoguebox_impl as db
import screens_impl as s
from akio import Hero
import background as bg

FramePerSec = pygame.time.Clock()
FPS = 180
current_level = 0
background_sprite = pygame.image.load('./Images/img_1.png')
class Game(sc.Screen):
    def __init__(self):
        pygame.init()
        #Audio Configuration
        self.level_music = pygame.mixer.Sound(r"Music/bgMusic.wav")
        self.wgr_music = pygame.mixer.Sound(r"Music/wgrMusic.wav")
        self.db_music = pygame.mixer.Sound(r"Music/dbMusic.wav")
        



    def run(self):
        clock = pygame.time.Clock()

        welcome_screen = True
        self.wgr_music.play(loops = -1)

        screen_impl = s.Screen_impl()
        while welcome_screen == True:
            screen_impl.welcome_scrn_impl()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    welcome_screen = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    btn_start = screen_impl.check_Ip(pygame.mouse.get_pos())
                    btn_exit = screen_impl.check_Ip(pygame.mouse.get_pos())
                    if btn_start == "start":
                        welcome_screen = False
                        running_level1 = True
                        self.wgr_music.stop()
                    if btn_exit == "exit":
                        self.wgr_music.stop()
                        pygame.quit()

            pygame.display.flip()
            sc.Screen.clock.tick(3600)
        
        #Dialogu box before level 1
        db.DialogueBox_Implementation.level1_dialogues(self)
            
        #Level 1 implementation
        level = Level_final.Level(l1.level_map,sc.Screen.scrn,0)
        window = pygame.display.set_mode((1200, 700))
        bg = pygame.transform.scale(background_sprite, (1200, 700))
        i = 0
        
        if current_level == 0:
            while running_level1:
                window.fill((0, 0, 0))
                window.blit(bg, (i, 0))
                window.blit(bg, (1200 + i, 0))

                if (i == -1200):
                    window.blit(bg, (1200 + i, 0))
                    i = 0
                i -= 1


                clock.tick(80)
                self.level_music.play(loops = -1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.level_music.stop()
                        running_level1 = False

                # if Level_final.Level.check_trophy_collision(self) == 0:
                #    running_level1 = False
                #    running_level2 = True
                   # level.akio.sprite.reset_health()

                # if Level_final.Level.check_trophy_collision(self, current_level="level1") == "level1":
                #     running_level1 = False
                #     running_level2 = True
                    # level.akio.sprite.reset_health()
                   # Reset health after Level 1
                # bg.Background.draw_background(self,sc.Screen.scrn)



                level.run()
                

                pygame.display.update()
                sc.Screen.clock.tick(80)
                FramePerSec.tick(FPS)
            
        if current_level == 1:       
            #Level 2 implementation    
            db.DialogueBox_Implementation.level2_dialogues(self)
        
            level = Level_final.Level(l2.level_map, sc.Screen.scrn,1)
            #running_level2 = True
            while running_level2:
                clock.tick(180)
                self.level_music.play(loops = -1)
        
                for event in pygame.event.get():
                    # if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT or level.level_end():
                        self.level_music.stop()
                        running_level2 = False
                        level.akio.sprite.reset_health()  # Reset health after Level 2

                # sc.Screen.scrn.fill((106, 159, 181))
                level.run()

                pygame.display.update()
                sc.Screen.clock.tick(180)
                FramePerSec.tick(FPS)
            
        
        pygame.quit()