import pygame

class Button(object):
	def __init__(self, x, y, x2, y2,text, num1, num2, num3):
		self.x = x
		self.y = y
		self.x2 = x2
		self.y2 = y2
		self.myRec = pygame.Rect(self.x, self.y, self.x2, self.y2)
		self.mySurface = pygame.Surface([self.x2, self.y2])
		self.mySurface.fill((num1,num2,num3))
		self.text=text
	def draw(self, a):
		a.blit(self.mySurface, self.myRec)
		#a.blit(pygame.Surface([2, 2]),pygame.Rect(self.x, self.y, 2, 2))
		myfont = pygame.font.SysFont("monospace", 15)
		label = myfont.render(self.text, 1, (36,62,74))
		main_screen.blit(label, (self.x+5, self.y+5))
flavor=""
def goToBirthday():
	main_screen.fill((91, 196, 201))
	myfont = pygame.font.SysFont("monospace", 45)
	label = myfont.render("BIRTHDAY CAKE:", 1, (196,148,71))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("monospace", 35)
	label = myfont.render("Flavor : "+flavor, 1, (196,148,71))
	main_screen.blit(label, (10, 50))
def goToWedding():
	main_screen.fill((91, 196, 201))
	myfont = pygame.font.SysFont("monospace", 45)
	label = myfont.render("WEDDING CAKE:", 1, (196,148,71))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("monospace", 35)
	label = myfont.render("Flavor : "+flavor, 1, (196,148,71))
	main_screen.blit(label, (10, 50))

if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((700, 600))
	main_screen.fill((91, 196, 201))
	placeX = 100
	placeY = 200
	Chocolate = Button(placeX, placeY, 90, 80,"Chocolate",120,92,80)
	Chocolate.draw(main_screen)
	Vanilla = Button(300, 200, 90, 80, "Vanilla", 194, 185, 172)
	Vanilla.draw(main_screen)
	Strawberry = Button(500, 200, 90, 80, "Strawberry", 194, 21, 64)
	Strawberry.draw(main_screen)
	myfont = pygame.font.SysFont("monospace", 45)
	label = myfont.render("Welcome to PyCake!", 1, (196,148,71))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("monospace", 35)
	label = myfont.render("Choose a flavor:", 1, (196,148,71))
	main_screen.blit(label, (10, 100))

	myfont = pygame.font.SysFont("monospace", 35)
	label = myfont.render("Choose your event:", 1, (196,148,71))
	main_screen.blit(label, (10, 300))
	Birthday = Button(100, 400, 150, 80, "Birthday", 91, 227, 93)
	Birthday.draw(main_screen)
	Wedding = Button(350, 400, 150, 80, "Wedding", 153, 103, 199)
	Wedding.draw(main_screen)
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
            		if Chocolate.myRec.collidepoint(x, y):
            			print "hi"
            			flavor="chocolate"
            		if Vanilla.myRec.collidepoint(x, y):
            			print "hi2"
            			flavor="vanilla"
            		if Strawberry.myRec.collidepoint(x, y):
            			print "hi3"
            			flavor="strawberry"
            		if Birthday.myRec.collidepoint(x, y):
            			goToBirthday()
            		if Wedding.myRec.collidepoint(x, y):
            			goToWedding()


    
				
		pygame.display.flip()
