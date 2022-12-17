# Filename Ch2_ColorPaint.py
import pygame # Настройка
import random
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw, using up to 3 mouse buttons") # Заголовок
keep_going = True
ORANGE = (255,255,0)
GREEN = (0,255,0)
PURPLE = (128,0,128)
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
	if mousedown:      # рисуем/обновляем графику
		spot = pygame.mouse.get_pos() 
		if pygame.mouse.get_pressed()[0]: # булево для кнопки 1
			button_color = ORANGE	
		elif pygame.mouse.get_pressed()[1]:  # булево для кнопки 2
			button_color = GREEN
		else:    # должно быть для кнопки 3
			button_color = PURPLE
		pygame.draw.circle(screen, button_color, spot, radius)
	pygame.display.update() # Обновить дисплей
	
pygame.quit() # Выход
