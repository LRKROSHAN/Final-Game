# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:19:43 2023

@author: parita, roshan, rintu
"""
import dialogueBox as db
import screen as s
import pygame


class DialogueBox_Implementation(db.Dialogue,s.Screen):
    def level1_dialogues(self):
        s.Screen.scrn.fill((106, 159, 181))
        dialogue_box = db.Dialogue(100, 100, 600, 100, text_speed=50)
        dialogue_box.display("Hello Akio! Welcome to this mistical world")
        pygame.time.delay(2000)  # wait for 2 seconds
        dialogue_box.display("Let us start the journey to defeat the enemies")
        pygame.time.delay(2000)
    def level2_dialogues(self):
        s.Screen.scrn.fill((106, 159, 181))
        dialogue_box = db.Dialogue(100, 100, 600, 100, text_speed=50)
        dialogue_box.display("Well Done! You have succefully completed Levle 1.")
        pygame.time.delay(2000)  # wait for 2 seconds
        dialogue_box.display("Level 2 will be more difficult, but I know that you can do it Akio")
        pygame.time.delay(2000)