import pygame
from config import *

class Home:
	def __init__(self, game):
		self.game = game
		self.screen = game.screen

		# start btn
		start_btn_width, start_btn_height = 200, 60
		start_btn_x, start_btn_y = (WIDTH-start_btn_width)/2, (HEIGHT-start_btn_height)/2
		self.start_btn_rect = pygame.Rect(start_btn_x, start_btn_y, start_btn_width, start_btn_height)
	
	def home_setup(self):
		# draw home bg
		self.screen.fill(GREEN)

		# Draw Start Button Rect
		pygame.draw.rect(self.screen, self.color, self.start_btn_rect)           # Green button
		pygame.draw.rect(self.screen, (0, 255, 0), self.start_btn_rect, 4)        # Bright green border

		# Draw Start Button text
		font = pygame.font.SysFont("Arial", 36, bold=True)
		text_surface = font.render("START", True, (255, 255, 255))   # White text
		text_rect = text_surface.get_rect(center=self.start_btn_rect.center)

		self.screen.blit(text_surface, text_rect)

	def update(self):
		# start btn hover effect
		mouse_pos = pygame.mouse.get_pos()
		hovered = self.start_btn_rect.collidepoint(mouse_pos)
		self.color = (0, 220, 0) if hovered else (0, 180, 0)

	def run(self):
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game.running = False
				return
			# Left click
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if self.start_btn_rect.collidepoint(event.pos):
					from src.battle import Battle
					self.game.scene = Battle(self.game)
					return
		
		# update home page
		self.update()
	
		# Draw home page
		self.home_setup()
