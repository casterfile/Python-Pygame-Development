import pygame
import sys


def main():
	pygame.init()
	pygame.mixer.init() #Adding functions to enable the sound

	windowSize = (800, 600)
	screen = pygame.display.set_mode(windowSize)
	helloWorld = pygame.image.load("PS circle.png")
	helloWorldSize = helloWorld.get_size();	
	sound = pygame.mixer.Sound("sound.mp3")#importing the sound

	pygame.mouse.set_visible(0)
	x,y = 0,0
	directionX = 1
	directionY = 1
	clock = pygame.time.Clock()
	while 1:
		clock.tick(40)#this will make use the this run 40/frames/second

		for event in pygame.event.get(): #this will handel all the event
			if event.type == pygame.QUIT: sys.exit()#this will quit the application

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					x += 15
				if event.key == pygame.K_LEFT:
					x -= 15

				if event.key == pygame.K_DOWN:
					y += 15
				if event.key == pygame.K_UP:
					y -= 15
		
		screen.fill((0,0,0))
		
		#mousePosition = pygame.mouse.get_pos()
		#x,y = mousePosition

		if x + helloWorldSize[0] > 800:
			x = 800 - helloWorldSize[0]
			sound.stop()
			sound.play()

		if y + helloWorldSize[1] > 600:
			y = 600 - helloWorldSize[1]
			sound.stop()
			sound.play()

		if x <= 0:
			x = 0
			sound.stop()
			sound.play()

		if y <= 0:
			y = 0
			sound.stop()
			sound.play()


		screen.blit(helloWorld, (x,y))

		pygame.display.update()#this will display the Windows


if __name__ == '__main__':
	main()