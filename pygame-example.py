import pygame

class Button(object):
	def __init__(self, x, y, x2, y2):
		self.x = x
		self.y = y
		self.x2 = x2
		self.y2 = y2
		self.myRec = pygame.Rect(self.x, self.y, self.x2, self.y2)
		self.mySurface = pygame.Surface([self.x2, self.y2])
	def draw(self, a):
		a.blit(self.mySurface, self.myRec)

if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 600))
	main_screen.fill((255, 255, 255))
	placeX = 100
	placeY = 100
	myButton = Button(placeX, placeY, 40, 40)
	myButton.draw(main_screen)

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
            		if myButton.myRec.collidepoint(x, y):
				if placeX <= 540:
					placeX += 40
				else:
					if placeY < 540:
						placeX -= 40
						placeY += 40
					if placeY == 540:
						placeX -= 40
				


				myButton = Button(placeX, placeY, 40, 40)
				myButton.draw(main_screen)
				
		pygame.display.flip()
