import pygame
from config import *

class Tower:
	def __init__(self, x, y, color, width, height):
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color

		# hp bar
		self.maxhp = 1000
		self.currenthp = 1000
		self.towerGap = 10
		self.hp_height = 5
		self.hp_width = 50
		self.hp_inwidth = 46
		self.hp_inheight = 3

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

		# HP bar border
		pygame.draw.rect(surface, DARKGREEN, (self.rect.x, self.rect.y - self.towerGap, 
											self.hp_width, self.hp_height))
		# HP bar
		pygame.draw.rect(surface, GREEN, (self.rect.x+(self.hp_width - self.hp_inwidth)/2, 
						self.rect.y - self.towerGap + (self.hp_height - self.hp_inheight)/2, 
						self.hp_inwidth*self.currenthp/self.maxhp, self.hp_inheight))
