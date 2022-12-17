# Filename DragDots.py

import pygame # Настройка
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw") # Заголовок
keep_going = True
YELLOW = (255,255,0) # триплет RGB для ЖЕЛТОГО цвета
radius = 15
mousedown = False
while keep_going: # Игровой цикл 
	for event in pygame.event.get(): # Обработка события
		if event.type == pygame.QUIT:
			keep_going = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousedown = True
		if event.type == pygame.MOUSEBUTTONUP:
			mousedown = False
	if mousedown: # Рисование/обновление графики
		spot = pygame.mouse.get_pos()
		pygame.draw.circle(screen, YELLOW, spot, radius)
	pygame.display.update() # Обновить дисплей
pygame.quit() # Выход
