import pygame
import gameutils
import constants as c

# Global Variables
running = True
pygame.init()
win = gameutils.getSurface(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.FULLSCREEN)
pygame.display.set_caption("Pygame Template")

while running:
	events = pygame.event.get()

	for event in events:
		if event.type == pygame.QUIT:
			running = False

gameutils.endProgram()