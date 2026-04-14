import pygame
from config import *
from src.tower import *
from src.unit import *
import random

def distance(u1, u2):
	return ((u1.x - u2.x) ** 2 + (u1.y - u2.y) ** 2) ** 0.5

if __name__ == "__main__":
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Ura Dhura")
	clock = pygame.time.Clock()
	running = True

	units = []
	enemy_spawn_timer = 0

	while running:
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				# Only allow spawn on player's half
				if y > HEIGHT // 2:
					units.append(Unit(x, y, 50, BLUE))

		enemy_spawn_timer += 1

		if enemy_spawn_timer > 120:  # every ~2 seconds
			x = random.randint(100, WIDTH - 100)
			units.append(Unit(x, 50, HEIGHT - 50, RED))
			enemy_spawn_timer = 0
		# fill the screen with a color to wipe away anything from last frame
		screen.fill("purple")

		# draw arena separation
		pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)

		# Create Towers
		player_tower = Tower(WIDTH // 2 - 25, HEIGHT - 100, BLUE)
		enemy_tower = Tower(WIDTH // 2 - 25, 20, RED)

		# Draw Towers
		player_tower.draw(screen)
		enemy_tower.draw(screen)

		# draw units
		for unit in units:
			unit.attack_timer += 1

			target = None

			for other in units:
				if other != unit and other.color != unit.color:
					if distance(unit, other) < unit.range:
						target = other
						break

			if target:
				if unit.attack_timer >= unit.attack_cooldown:
					target.hp -= unit.damage
					unit.attack_timer = 0
			else:
				unit.update()
			unit.draw(screen)

		units = [u for u in units if u.hp > 0]
		
		# flip() the display to put your work on screen
		pygame.display.flip()

		clock.tick(FPS)  # limits FPS to 60

	pygame.quit()
