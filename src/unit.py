import pygame
from config import *

class Unit:
	def __init__(self, x, y, target_y, color):
		self.x = x
		self.y = y
		self.radius = 10
		self.color = color
		self.speed = 2
		self.target_y = target_y
		self.hp = 100
		self.damage = 5
		self.range = 20
		self.attack_cooldown = 30
		self.attack_timer = 0

	def update(self):
		# Move vertically toward target
		if self.y > self.target_y:
			self.y -= self.speed
		elif self.y < self.target_y:
			self.y += self.speed

	def draw(self, surface):
		pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
