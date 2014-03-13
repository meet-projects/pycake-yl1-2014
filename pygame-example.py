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
	myButton = Button(100, 100, 40, 40)
	myButton.draw(main_screen)

	while True:
		ev = pygame.event.poll()
		pygame.display.flip()
