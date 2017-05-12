import pygame
import sys


def main():
	pygame.init()

	windowSize = (800, 600)
	screen = pygame.display.set_mode(windowSize)
	myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
	helloWorld = myriadProFont.render("Hello World", 1, (255,0,255),(255,255,255))

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.blit(helloWorld, (0,0))
		pygame.display.update()


if __name__ == '__main__':
	main()