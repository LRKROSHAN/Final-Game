# -*- coding: utf-8 -*-
"""
Created on Sat May  6 18:34:07 2023

@author: parita
"""
#level_final.py
import pygame
from Tile import Tile
from End_level import End_level
from Level2_map import tile_size,screen_width, screen_height
from akio import Hero
from enemy import Enemy
import screen as s
import screens_impl as sc
import Game as g
import Level1_map as l1
import Level2_map as l2
import math

class Level(s.Screen):
    def __init__(self,level_data,surface, current_level):
        self.done = False
        self.enemy_sprites = pygame.sprite.Group()  
        self.platform_sprites = pygame.sprite.Group()
        self.akio = Hero
        self.screen = surface  # Add this line
        self.display_surface = surface
        self.setup_level(level_data)
        self.screen_shift = 9
        self.win_height = 700
        self.win_width = 1200
        self.current_level = current_level
        self.health_bar_bg = pygame.Surface((300, 20))
        self.health_bar_bg.set_alpha(100)  

    def setup_level(self,layout):
        self.Tile = pygame.sprite.Group()
        self.akio = pygame.sprite.GroupSingle()
        self.enemy_grp = pygame.sprite.Group()
        self.End_level = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, colm in enumerate(row):
                if colm == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile_sprite = Tile((x,y),tile_size)
                    self.Tile.add(tile_sprite)

                if colm == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Hero((x,y))
                    self.akio.add(player_sprite)

                if colm == 'E':
                    
                    enemy_sprite1 = Enemy(col_index * tile_size ,row_index * tile_size + 15)
                    self.enemy_grp.add(enemy_sprite1)
                
                if colm == 'W':
                    #end_rect = pygame.Rect(col_index, row_index, tile_size, tile_size)
                    #pygame.draw.rect(s.Screen.scrn, (255,0,0), end_rect)
                    #pygame.display.flip()
                    x = col_index * tile_size
                    y = row_index * tile_size
                    trophy_sprite = End_level((x,y),tile_size)
                    self.End_level.add(trophy_sprite)
                    #s.Screen.scrn.blit(end_img,end_rect)

    def draw_health_bar(self):
        health_ratio = self.akio.sprite.health / 100
        green_bar_width = int(300 * health_ratio)
        red_bar_width = 300 - green_bar_width

        pygame.draw.rect(self.health_bar_bg, (0, 255, 0), (0, 0, green_bar_width, 20))
        pygame.draw.rect(self.health_bar_bg, (255, 0, 0), (green_bar_width, 0, red_bar_width, 20))

        self.screen.blit(self.health_bar_bg, (10, 10))
        self.screen.blit(self.font.render(f'HP: {self.akio.sprite.health}', True, (255, 255, 255)), (320, 10))


    def scroll(self):
        player = self.akio.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x

        if player_x < screen_width/2 and direction_x < 0:
            self.screen_shift = 12
            player.speed = 0
        elif player_x > screen_width - (screen_width/2) and direction_x > 0:
            self.screen_shift = -12
            player.speed = 0
        else:
            self.screen_shift = 0
            player.speed = 6
    
    def horizontal_collision(self):
        player = self.akio.sprite
        player.rect.x += player.direction.x

        for sprite in self.Tile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right

                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.akio.sprite
        player.get_gravity()

        for sprite in self.Tile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def show_message_box(self, message, title):
        # Create a pop-up window with the specified message and title
        pygame.init()
        pygame.display.set_caption(title)
        #message_box = pygame.display.set_mode((400, 200))
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 255, 255))
    
        restart_level = True
        screen_impl = sc.Screen_impl()
        screen_impl.restart_level()  # Add this line
    
        while restart_level:
            # screen_impl.restart_level()  
            for event in pygame.event.get():
                # screen_impl.restart_level()  
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        btn_start = screen_impl.check_Ip(pygame.mouse.get_pos())
                        btn_exit = screen_impl.check_Ip(pygame.mouse.get_pos())
                        if btn_start == "start":
                    
                            restart_level = False
                            #running_level1 = True
                            self.wgr_music.stop()
                        if btn_exit == "exit":
                            self.wgr_music.stop()
                            pygame.quit()
                        pygame.display.update()
        pygame.quit()
            
    def fall_void_space(self):
        player = self.akio.sprite
        player_y = player.rect.centery
        if player_y > self.win_height:
            if self.current_level == 0:
                #self.show_message_box("You fell into the void! Restarting level 1...", "Level 1 Restart")
                self.setup_level(l1.level_map)  # restart level 1
            
            elif self.current_level == 1:
                #self.show_message_box("You fell into the void! Restarting level 2...", "Level 2 Restart")
                self.setup_level(l2.level_map)  # restart level 2 
            #sc.Screen_impl().restart_level()  
        self.akio.update()
    def level_check(self):
        return
    def game_reset(self):
        return
    def check_enemy_collision(self):
        player = self.akio.sprite
        for enemy in self.enemy_grp.sprites():
            if player.rect.colliderect(enemy.rect):
                # If the player is above the enemy and falling, the enemy dies
                if player.direction.y > 0 and player.rect.bottom - enemy.rect.top <= 10:
                    self.enemy_grp.remove(enemy)
                else:
                    # Take damage and apply knockback
                    player_direction = pygame.math.Vector2(-math.copysign(5, player.direction.x), 0)
                    player.take_damage(1, 1, player_direction)


    def check_trophy_collision(self):
        player = self.akio.sprite
        trophy = self.End_level.sprite
        if player.rect.colliderect(trophy.rect):
                # If the player is above the enemy and falling, the enemy dies
                if player.direction.y > 0 and player.rect.bottom - trophy.rect.top <= 10:
                    self.End_level.remove(trophy)
                    self.show_message_box("Congratulations! You won the game.", "Game Over") 
    
    def show_message_box(self, message, title):
        pygame.init()
        pygame.display.set_caption(title)
        font = pygame.font.Font(None, 20)
        text = font.render(message, True, (255, 255, 255))

        message_box = pygame.Surface((400, 200))
        message_box.blit(text, (50, 50))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(message_box, (self.screen.get_width() // 2 - 200, self.screen.get_height() // 2 - 100))
            pygame.display.flip()
        pygame.quit()


    def run(self):
        # while not self.done:
        #     # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True

            # Update the game state
            self.akio.update()
            self.enemy_grp.update(self.screen_shift)  # Pass the screen_shift value
            self.Tile.update(self.screen_shift)  # Pass the screen_shift value
            self.End_level.update(self.screen_shift)

            # Collisions
            self.horizontal_collision()
            self.vertical_collision()
            self.check_enemy_collision()

            self.check_trophy_collision()

            # Update the scrolling
            self.scroll()

            # Clear the screen
            # self.display_surface.fill((0, 0, 0))

            # Draw platforms, enemies and player
            self.Tile.draw(self.display_surface)
            self.enemy_grp.draw(self.display_surface)
            self.akio.draw(self.display_surface)
            self.End_level.draw(self.display_surface)

            # Draw the health bar
            self.draw_health_bar()

            # Update the display
            pygame.display.update()

            # Check for the level end condition
            # self.level_end():
            #     self.done = True

            # Check for falling into void
            self.fall_void_space()

            # Limit the frame rate
            pygame.time.Clock().tick(60)


        # def run(self):
        #     self.Tile.update(self.screen_shift)
        #     self.Tile.draw(self.display_surface)
        #     self.scroll()
        #     #AKIO
        #     self.akio.update()
        #     self.horizontal_collision()
        #     self.vertical_collision()
        #     self.check_enemy_collision()

        #     self.akio.draw(self.display_surface)
        #     self.fall_void_space()
        #     self.akio.update()
        #     #Enemy
        #     self.enemy_grp.update(self.screen_shift)
        #     self.enemy_grp.draw(self.display_surface)
        #     #Trophy
        #     self.End_level.update(self.screen_shift)
        #     ##HP
        #     while not self.done:
        #         self.event_loop()
        #         self.update()
        #         self.draw()

        #         self.draw_health_bar()  # Add this line here

        #         pygame.display.update()
        #         self.clock.tick(60)
