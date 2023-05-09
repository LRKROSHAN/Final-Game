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
        self.db_music.play(loops = -1)
        s.Screen.scrn.fill((106, 159, 181))
        dialogue_box = db.Dialogue(100, 100, 600, 100, text_speed=50)
        dialogue_box.display("Hello Akio! Welcome to this mistical world!")
        pygame.time.delay(2000)  
        dialogue_box.display("Get ready to explore a new world filled with challenges!")
        pygame.time.delay(2000)
        self.db_music.stop()
        
    def level2_dialogues(self):
        self.db_music.play(loops = -1)
        s.Screen.scrn.fill((106, 159, 181))
        dialogue_box = db.Dialogue(100, 100, 600, 100, text_speed=50)
        dialogue_box.display("Well done! You've proven that you have what it takes to be a hero. You've completed the first level, but the journey ahead won't be easy.")
        pygame.time.delay(2000)  # wait for 1.5 seconds
        self.db_music.stop()
