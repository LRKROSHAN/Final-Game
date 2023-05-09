import pygame


class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = pos)

	def update(self, shift):
		self.rect.x += shift

# class End_level(pygame.sprite.Sprite):
#     def __init__(self,pos,size):
#         super().__init__()
#         self.image = pygame.image.load("Images/trophy.png")
#         self.image = pygame.transform.scale(self.image,(size,size))
#         self.rect = self.image.get_rect()
#         self.rect = self.image.get_rect(topleft = pos)
#     def update(self, shift):
#         self.rect.x += shift
        