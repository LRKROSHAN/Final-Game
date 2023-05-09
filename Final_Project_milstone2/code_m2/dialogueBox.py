# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:34:46 2023

@author: parita, roshan, rintu
"""
import pygame
import screen as s

class Dialogue(s.Screen):
    def __init__(self, x, y, width, height, text_speed=50):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_speed = text_speed

    def display(self, text):
        FONT = pygame.font.SysFont("arial", 20)
        pygame.draw.rect(s.Screen.scrn, (0,0,0), self.rect)
        # Animate the text in the dialogue box
        words = text.split()
        FONT = pygame.font.SysFont("arial", 20)
        space_width = FONT.size(' ')[0]
        space_gap = space_width * 2
        x = self.rect.x + space_gap
        y = self.rect.y + space_gap
        max_width = self.rect.width - space_gap * 2
        text_surface = pygame.Surface((max_width, self.rect.height - space_gap * 2))
        text_surface.fill((0,0,0))
        word_index = 0
        
        while word_index < len(words):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            text_surface.fill((0,0,0))

            words_per_line = []
            line_widths = []
            current_width = 0
            for i in range(word_index, len(words)):
                word_surface = FONT.render(words[i], True, (255,255,255))
                word_width, word_height = word_surface.get_size()
                if current_width + word_width + space_width <= max_width:
                    words_per_line.append(words[i])
                    current_width += word_width + space_width
                else:
                    line_widths.append(current_width)
                    current_width = 0
                    break
                if i == len(words) - 1:
                    line_widths.append(current_width)

            current_x, current_y = 0, 0
            for i in range(len(words_per_line)):
                word_surface = FONT.render(words_per_line[i], True, (255,255,255))
                word_width, word_height = word_surface.get_size()
                if current_x + word_width <= max_width:
                    text_surface.blit(word_surface, (current_x, current_y))
                    current_x += word_width + space_width
                else:
                    current_x = 0
                    current_y += word_height + space_gap
                    text_surface.blit(word_surface, (current_x, current_y))
                    current_x += word_width + space_width

            self.draw_border()
            s.Screen.scrn.blit(text_surface, (x, y))
            pygame.display.update()

            word_index += len(words_per_line)

            s.Screen.clock.tick(self.text_speed)

    def draw_border(self):
        # Draw the border of the dialogue box
        border_rect = pygame.Rect(self.rect.x - 5, self.rect.y - 5, self.rect.width + 10, self.rect.height + 10)
        pygame.draw.rect(s.Screen.scrn, (255,255,255), border_rect, 5)

