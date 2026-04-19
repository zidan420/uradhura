from config import *
import pygame

"""
Strength depends on color:
limegreen
forestgreen
black
"""
class Unit:
	def __init__(self, game, x, y, color, width, height):
		"""
		x and y are the top/facing coord of triangles
		"""
		self.game = game
		self.screen = game.screen
		self.speed = 1
		self.color = color
		self.height = height
		self.width = width
		self.points = [(x, y), (x-self.width/2,y+self.height), (x+self.width/2,y+self.height)]

	def draw(self):
		pygame.draw.polygon(self.screen, BLACK, self.points, 5)
		pygame.draw.polygon(self.screen, self.color, self.points)
