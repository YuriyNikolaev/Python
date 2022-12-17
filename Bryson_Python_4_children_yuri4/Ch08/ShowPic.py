# Filename ShowPic.py

import pygame # Настройка
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("CrzySmile.bmp")

while keep_going: #Игровой цикл
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False
	screen.blit(pic, (100,100))
	pygame.display.update()

pygame.quit() # Выход

	