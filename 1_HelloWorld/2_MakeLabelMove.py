import pygame
import sys


def main():
	pygame.init()

	windowSize = (800, 600)
	screen = pygame.display.set_mode(windowSize)
	myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
	helloWorld = myriadProFont.render("Hello World", 1, (255,0,255),(255,255,255))

	x,y = 0,0
	clock = pygame.time.Clock()
	while 1:
		clock.tick(40)#this will make use the this run 40/frames/second

		for event in pygame.event.get(): #this will handel all the event
			if event.type == pygame.QUIT: sys.exit()#this will quit the application

		screen.fill((0,0,0))
		screen.blit(helloWorld, (x,y))

		x += 5

		pygame.display.update()#this will display the Windows

if __name__ == '__main__':
	main()