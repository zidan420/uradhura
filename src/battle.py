import pygame
from config import *
from src.tower import Tower
from src.unit import Unit

class Battle:
	def __init__(self, game):
		self.game = game
		self.screen = game.screen

		# Create Towers
		towerWidth, towerHeight = 50, 80
		yMargin = 20
		self.holderHeight = 100
		self.enemyTower = Tower((WIDTH-towerWidth)/2, yMargin, RED, towerWidth, towerHeight)
		self.myTower = Tower((WIDTH-towerWidth)/2, HEIGHT-yMargin-towerHeight-self.holderHeight, BLUE, 
							towerWidth, towerHeight)

		# Cards
		self.cards = []

		self.card_col = 3
		self.card_gap = 5
		self.card_height = self.holderHeight - self.card_gap*2
		self.card_width = (WIDTH - self.card_gap*(self.card_col+1))/self.card_col

		firstcard = pygame.Rect(self.card_gap, HEIGHT - self.holderHeight + self.card_gap, 
											self.card_width, self.card_height)
		secondcard = pygame.Rect(self.card_gap*2+self.card_width, 
											HEIGHT - self.holderHeight + self.card_gap, 
											self.card_width, self.card_height)
		thirdcard = pygame.Rect(self.card_gap*3+self.card_width*2, 
											HEIGHT - self.holderHeight + self.card_gap, 
											self.card_width, self.card_height)
		self.cards.append([GOLD, firstcard])
		self.cards.append([GOLD, secondcard])
		self.cards.append([GOLD, thirdcard])

		# Card icons
		iconwidth, iconheight = self.card_width-20, self.card_height-20
		y = HEIGHT-self.holderHeight+self.card_gap+5

		limex = self.card_gap+self.card_width/2
		self.limegreencard = Unit(self.game, limex, y, LIMEGREEN, iconwidth, iconheight)

		forestx = self.card_gap*2+self.card_width*3/2
		self.forestgreencard = Unit(self.game, forestx, y, FORESTGREEN, iconwidth, iconheight)

		blackx = self.card_gap*3+self.card_width*5/2
		self.blackcard = Unit(self.game, blackx, y, BLACK, iconwidth, iconheight)

	def draw_battle(self):
		# draw home bg
		self.screen.fill(DARKYELLOW)

		# create separation
		pygame.draw.line(self.screen, ORANGEYELLOW, (0, (HEIGHT-self.holderHeight)/2), 
						(WIDTH, (HEIGHT-self.holderHeight)/2), 5)

		# draw towers
		self.enemyTower.draw(self.screen)
		self.myTower.draw(self.screen)

		# draw card placeholder
		pygame.draw.rect(self.screen, WHITE, (0, HEIGHT - self.holderHeight, WIDTH, self.holderHeight))

		# draw cards
		for color, card in self.cards:
			pygame.draw.rect(self.screen, color, card)

		# draw card icons
		self.limegreencard.draw()
		self.forestgreencard.draw()
		self.blackcard.draw()


	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		for index, (color, card) in enumerate(self.cards):
			hovered = card.collidepoint(mouse_pos)
			self.cards[index][0] = ORANGEYELLOW if hovered else color

	def run(self):
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game.running = False
				return
			# Left click
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pass

		self.update()
		self.draw_battle()
