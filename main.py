import pygame
from config import *
from src.home import Home

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Ura Dhura")
		self.running = True

	def run(self):
		clock = pygame.time.Clock()

		home = Home(self)
		self.scene = home

		while self.running:
			self.scene.run()

			# flip() the display to put your work on screen
			pygame.display.flip()

			clock.tick(FPS)  # limits FPS to 60

		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()
