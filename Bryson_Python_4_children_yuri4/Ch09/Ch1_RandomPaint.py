# Filename Ch1_RandomPaint.py

import pygame # Настройка
import random
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw") # Заголовок
keep_going = True

colors = (0,0,0)
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

	colors = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	if mousedown: # Рисование/обновление графики
		spot = pygame.mouse.get_pos()
		pygame.draw.circle(screen, colors, spot, radius)
	pygame.display.update() # Обновить дисплей
pygame.quit() # Выход
