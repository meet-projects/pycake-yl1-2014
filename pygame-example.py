import pygame
import sys

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
		myfont = pygame.font.SysFont("Purisa", 15)
		label = myfont.render(self.text, 1, (36,62,74))
		main_screen.blit(label, (self.x+10, self.y+10))
price = 0
flavor=""
gender =""
layer =""
myType=""
placeX = 100
placeY = 200
female = Button(100, 200, 150, 80, "Female", 245, 113, 179)
male = Button(300, 200, 150, 80, "Male", 113, 161, 245)
layer1 = Button(100, 200, 80, 80, "1", 153, 103, 199)
layer2 = Button(200, 200, 80, 80, "2", 153, 103, 199)
layer3 = Button(300, 200, 80, 80, "3", 153, 103, 199)
layer4 = Button(400, 200, 80, 80, "4", 153, 103, 199)
layer5 = Button(500, 200, 80, 80, "5", 153, 103, 199)
submit = Button(300, 500, 150, 80, "Submit", 153, 103, 199)
cancel = Button(500, 500, 150, 80, "Cancel", 153, 103, 199)
Chocolate = Button(placeX, placeY, 90, 80,"Chocolate",120,92,80)
Vanilla = Button(300, 200, 90, 80, "Vanilla", 194, 185, 172)
Strawberry = Button(500, 200, 90, 80, "Strawberry", 194, 21, 64)
Birthday = Button(100, 400, 150, 80, "Birthday", 91, 227, 93)
Wedding = Button(350, 400, 150, 80, "Wedding", 153, 103, 199)
startOver  = Button(500, 500, 150, 80, "Start Again", 153, 103, 199)
def goToBirthday():
	myType="birthday"
	main_screen.fill((91, 196, 201))
	myfont = pygame.font.SysFont("Purisa", 45)
	label = myfont.render("BIRTHDAY CAKE:", 1, (196,148,71))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("Purisa", 35)
	label = myfont.render("Flavor : "+flavor, 1, (196,148,71))
	main_screen.blit(label, (10, 80))
	label = myfont.render("Choose your gender:", 1, (196,148,71))
	main_screen.blit(label, (10, 140))
	female.draw(main_screen)
	male.draw(main_screen)
	submit.draw(main_screen)
	cancel.draw(main_screen)
def goToWedding():
	main_screen.fill((91, 196, 201))
	myfont = pygame.font.SysFont("Purisa", 45)
	label = myfont.render("WEDDING CAKE:", 1, (196,148,71))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("Purisa", 35)
	label = myfont.render("Flavor : "+flavor, 1, (196,148,71))
	main_screen.blit(label, (10, 80))
	label = myfont.render("Choose number of layers:", 1, (196,148,71))
	main_screen.blit(label, (10, 140))
	layer1.draw(main_screen)
	layer2.draw(main_screen)
	layer3.draw(main_screen)
	layer4.draw(main_screen)
	layer5.draw(main_screen)
	submit.draw(main_screen)
	cancel.draw(main_screen)
def submitButton():
	main_screen.fill((91, 196, 201))
	myfont = pygame.font.SysFont("Purisa", 45)
	label = myfont.render("YOUR ORDER", 1, (196,148,71))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("Purisa", 35)
	label = myfont.render("Flavor : "+flavor, 1, (196,148,71))
	main_screen.blit(label, (10, 80))
	label = myfont.render("Event : "+myType, 1, (196,148,71))
	main_screen.blit(label, (10, 140))
	if myType=="wedding":
		label = myfont.render("Layers : "+layer, 1, (196,148,71))
		main_screen.blit(label, (10, 200))
	else:
		label = myfont.render("Gender : "+gender, 1, (196,148,71))
		main_screen.blit(label, (10, 200))
	label = myfont.render("Price = " + str(price) + " dollars", 1, (196,148,71))
	main_screen.blit(label, (10,260)) 
	myfont = pygame.font.SysFont("Purisa", 45)
	label = myfont.render("THANK YOU!", 1, (196,148,71))
	main_screen.blit(label, (10, 400))
	startOver.draw(main_screen)
	picture = pygame.image.load("cake.jpg")
	picture = pygame.transform.scale(picture, (200,150))
	main_screen.blit(picture,(450,200))
def mainScreen():
	main_screen.fill((91, 196, 201))
	placeX = 100
	placeY = 200
	Chocolate.draw(main_screen)
	Vanilla.draw(main_screen)
	Strawberry.draw(main_screen)
	myfont = pygame.font.SysFont("Purisa", 45)
	label = myfont.render("Welcome to PyCake!", 1, (0,0,0))
	main_screen.blit(label, (10, 10))
	myfont = pygame.font.SysFont("Purisa", 35)
	label = myfont.render("Choose a flavor:", 1, (0,0,0))
	main_screen.blit(label, (10, 100))
	myfont = pygame.font.SysFont("Purisa", 35)
	label = myfont.render("Choose your event:", 1, (0,0,0))
	main_screen.blit(label, (10, 300))
	Birthday.draw(main_screen)
	Wedding.draw(main_screen)

if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((700, 600))
	mainScreen()
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
            		if Chocolate.myRec.collidepoint(x, y) and myType=="":
						price = 200
						flavor="chocolate"
						picture = pygame.image.load("chocolatecake.jpg")
						picture = pygame.transform.scale(picture, (90,80))
						main_screen.blit(picture,(100,200))
						Strawberry.draw(main_screen)
						Vanilla.draw(main_screen) 
            		if Vanilla.myRec.collidepoint(x, y) and myType=="":
						price = 300 
						picture = pygame.image.load("vanillacaketibah.jpg")
						picture = pygame.transform.scale(picture, (90,80)) 
						main_screen.blit(picture,(300,200)) 
						Chocolate.draw(main_screen)
						Strawberry.draw(main_screen)
						flavor="vanilla"
            		if Strawberry.myRec.collidepoint(x, y) and myType=="":
						price = 400
						picture = pygame.image.load("strawberrycake.jpg")
						picture = pygame.transform.scale(picture, (90,80)) 
						main_screen.blit(picture,(500,200)) 
						Chocolate.draw(main_screen)
						Vanilla.draw(main_screen)
						flavor="strawberry"
            		if Birthday.myRec.collidepoint(x, y):
				myType="birthday"
            			goToBirthday()
            		if Wedding.myRec.collidepoint(x, y):
				myType="wedding"
            			goToWedding()

            		if female.myRec.collidepoint(x, y) and myType=="birthday":
            			gender="female"
            			female = Button(100, 200, 150, 80, "Female", 255,255,255)
            			male = Button(300, 200, 150, 80, "Male", 113, 161, 245)
            			female.draw(main_screen)
            			male.draw(main_screen)
			if male.myRec.collidepoint(x, y) and myType=="birthday":
            			gender="male"
            			male = Button(300, 200, 150, 80, "Male", 255,255,255)
            			female = Button(100, 200, 150, 80, "Female", 245, 113, 179)
            			female.draw(main_screen)
            			male.draw(main_screen)
			if layer1.myRec.collidepoint(x, y) and myType=="wedding":
				price = price*1
            			layer= "1 layer"
            			layer1 = Button(100, 200, 80, 80, "1", 255,255,255)
            			layer2 = Button(200, 200, 80, 80, "2", 153, 103, 199)
            			layer3 = Button(300, 200, 80, 80, "3", 153, 103, 199)
            			layer4 = Button(400, 200, 80, 80, "4", 153, 103, 199)
            			layer5 = Button(500, 200, 80, 80, "5", 153, 103, 199)
            			layer1.draw(main_screen)
            			layer2.draw(main_screen)
            			layer3.draw(main_screen)
            			layer4.draw(main_screen)
            			layer5.draw(main_screen)
			if layer2.myRec.collidepoint(x, y) and myType=="wedding":
				price = price*2
            			layer= "2 layers"
            			layer1 = Button(100, 200, 80, 80, "1", 153, 103, 199)
            			layer2 = Button(200, 200, 80, 80, "2", 255,255,255)
            			layer3 = Button(300, 200, 80, 80, "3", 153, 103, 199)
            			layer4 = Button(400, 200, 80, 80, "4", 153, 103, 199)
            			layer5 = Button(500, 200, 80, 80, "5", 153, 103, 199)
            			layer1.draw(main_screen)
            			layer2.draw(main_screen)
            			layer3.draw(main_screen)
            			layer4.draw(main_screen)
            			layer5.draw(main_screen)
			if layer3.myRec.collidepoint(x, y) and myType=="wedding":
				price = price*3
            			layer= "3 layers"
            			layer1 = Button(100, 200, 80, 80, "1", 153, 103, 199)
            			layer2 = Button(200, 200, 80, 80, "2", 153, 103, 199)
            			layer3 = Button(300, 200, 80, 80, "3", 255,255,255)
            			layer4 = Button(400, 200, 80, 80, "4", 153, 103, 199)
            			layer5 = Button(500, 200, 80, 80, "5", 153, 103, 199)
            			layer1.draw(main_screen)
            			layer2.draw(main_screen)
            			layer3.draw(main_screen)
            			layer4.draw(main_screen)
            			layer5.draw(main_screen)
			if layer4.myRec.collidepoint(x, y) and myType=="wedding":
				price = price*4
            			layer= "4 layers"
            			layer1 = Button(100, 200, 80, 80, "1", 153, 103, 199)
            			layer2 = Button(200, 200, 80, 80, "2", 153, 103, 199)
            			layer3 = Button(300, 200, 80, 80, "3", 153, 103, 199)
            			layer4 = Button(400, 200, 80, 80, "4", 255,255,255)
            			layer5 = Button(500, 200, 80, 80, "5", 153, 103, 199)
            			layer1.draw(main_screen)
            			layer2.draw(main_screen)
            			layer3.draw(main_screen)
            			layer4.draw(main_screen)
            			layer5.draw(main_screen)
			if layer5.myRec.collidepoint(x, y) and myType=="wedding":
				price = price*5
            			layer= "5 layers"
            			layer1 = Button(100, 200, 80, 80, "1", 153, 103, 199)
            			layer2 = Button(200, 200, 80, 80, "2", 153, 103, 199)
            			layer3 = Button(300, 200, 80, 80, "3", 153, 103, 199)
            			layer4 = Button(400, 200, 80, 80, "4", 153, 103, 199)
            			layer5 = Button(500, 200, 80, 80, "5", 255,255,255)
            			layer1.draw(main_screen)
            			layer2.draw(main_screen)
            			layer3.draw(main_screen)
            			layer4.draw(main_screen)
            			layer5.draw(main_screen)
			if submit.myRec.collidepoint(x, y):
            			submitButton()
			if cancel.myRec.collidepoint(x, y):
            			flavor=""
				gender =""
				layer =""
				myType=""
				price = 0
				mainScreen()
			if startOver.myRec.collidepoint(x, y):
            			flavor=""
				gender =""
				layer =""
				myType=""
				mainScreen()
				




    
				
		pygame.display.flip()
