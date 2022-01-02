import pygame
import sys

def getSurface(width, height, fullscreen):
	if fullscreen:
		surface = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
	else:
		surface = pygame.display.set_mode((width, height))
	
	return surface

def endProgram():
	pygame.display.quit()
	pygame.quit()
	sys.exit()