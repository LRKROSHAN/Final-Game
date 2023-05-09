# # -*- coding: utf-8 -*-
# """
# Created on Thu Mar 16 12:11:06 2023

# @author: parita, rintu, roshan
# """

# import pygame
# from Anime import import_folder

# # Initialize pygame
# #pygame.init()

# # Screen dimensions
# # WIDTH = 800
# # HEIGHT = 600
# #load hero sprite
# # hero_sprite = pygame.image.load('./Images/Character/Idle/1.png')
# fps = 60


# #Player Class

# class Akio(pygame.sprite.Sprite):
#     def __init__(self,pos):
#         super().__init__()
#         self.import_character()
#         self.frame_index = 0
#         self.animation_speed = 0.021
#         self.image = self.animations['Idle'][self.frame_index]
#         # self.image = pygame.Surface((32, 64))
#         # self.image.fill('red')
#         self.rect = self.image.get_rect(topleft=pos)
#         self.facing_right = True

#         self.direction = pygame.math.Vector2(0,0)
#         self.speed = 8
#         self.gravity = 0.05
#         self.jump_speed = -4
#         self.fall_count = 0
#         self.on_ground = False
#         self.on_ceiling = False
#         self.jumped = False


#     def import_character(self):
#         character_path = './Images/Character/'
#         self.animations = {'Idle':[],'run':[],'jump':[],'fall':[]}

#         for animation in self.animations.keys():
#             full_path = character_path + animation
#             print(full_path)
#             self.animations[animation] = import_folder(full_path)

#     def char_ground(self):
#         if self.on_ground:
#             self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
#         elif self.on_ceiling:
#             self.rect = self.image.get_rect(midtop=self.rect.midtop)
#         else:
#             self.rect = self.image.get_rect(center=self.rect.center)

#     def animate(self):
#         animation = self.animations['Idle']

#         self.frame_index += self.animation_speed
#         if self.frame_index >= len(animation):
#             self.frame_index = 0

#         image = animation[int(self.frame_index)]
#         if self.facing_right:
#             self.image = image
#         else:
#             facing_left= pygame.transform.flip(image,True,False)
#             self.image = facing_left


#     def get_input(self):
#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_RIGHT]:
#             self.direction.x = 1
#             self.facing_right = True
#         elif keys[pygame.K_LEFT]:
#             self.direction.x = -1
#             self.facing_right = False
#         else:
#             self.direction.x = 0

#         if keys[pygame.K_SPACE] and self.on_ground and self.jumped == False:
#             self.jump()
#         if keys[pygame.K_SPACE] == False:
#             self.jumped = False


#     def get_gravity(self):
#         self.direction.y += self.gravity
#         self.rect.y += self.direction.y

#     def jump(self):
#         self.direction.y = self.jump_speed

#     def update(self):
#         self.get_input()
#         self.animate()
    
#     def status_of_player(self):
#         if self.direction.y < 0:
#             self.status = 'jump' 
#         elif self.direction.y > 1:
#             self.status = 'fall' 
#         else:
#             if self.direction.x != 0:
#                 self.status = 'run'
#             else:
#                 self.status = 'idle'
                
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:11:06 2023

@author: parita, rintu, roshan
"""
#akio.py
import pygame
import math

from Anime import import_folder
import random

# Initialize pygame
#pygame.init()

# Screen dimensions
# WIDTH = 800
# HEIGHT = 600
#load hero sprite
# hero_sprite = pygame.image.load('./Images/Character/Idle/1.png')
FPS = 60
#hero class
class Hero(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character()
        self.frame_index = 0
        self.animation_speed = 7.0
        self.image = self.animations['Idle'][self.frame_index]
        # self.image = pygame.Surface((32, 64))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.facing_right = True

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.7 
        self.jump_speed = -14
        self.fall_count = 0
        self.on_ground = False
        self.on_ceiling = False
        self.jumped = False
        self.health = 100
        


    def import_character(self):
        character_path = './Images/Character/'
        self.animations = {'Idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            print(full_path)
            self.animations[animation] = import_folder(full_path)


    def char_ground(self):
        if self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center=self.rect.center)

    def animate(self):
        animation = self.animations['Idle']

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            facing_left= pygame.transform.flip(image,True,False)
            self.image = facing_left


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = self.speed
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -self.speed
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground and self.jumped == False:
            self.jump()
        if keys[pygame.K_SPACE] == False:
            self.jumped = False

    def take_damage(self, damage, knockback, direction):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        knockback_vector = pygame.math.Vector2(direction.x * knockback, direction.y * knockback)
        self.rect.x += knockback_vector.x
        self.rect.y += knockback_vector.y

    def reset_health(self):
        self.health = 100
        
    def get_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()
    
    def status_of_player(self):
        if self.direction.y < 0:
            self.status = 'jump' 
        elif self.direction.y > 1:
            self.status = 'fall' 
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
                

        

