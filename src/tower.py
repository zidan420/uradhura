import pygame
from config import *

class Tower:
	"""
	width of tower = 50
	height of tower = 80
	"""
	def __init__(self, x, y, color):
		self.rect = pygame.Rect(x, y, 50, 80)
		self.color = color
		self.hp = 1000

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

		# HP bar
		hp_ratio = self.hp / 1000
		pygame.draw.rect(surface, GREEN, (self.rect.x, self.rect.y - 10, 50 * hp_ratio, 5))
