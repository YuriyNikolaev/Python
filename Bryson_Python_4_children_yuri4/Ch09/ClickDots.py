# Filename ClickDots.py

import pygame # Настройка
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and Draw") # Заголовок
keep_going = True
RED = (255,0,0) # триплет RGB для КРАСНОГО цвета
radius = 15
while keep_going: # Игровой цикл 
	for event in pygame.event.get(): # Обработка события
		if event.type == pygame.QUIT:
			keep_going = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			spot = event.pos
			pygame.draw.circle(screen, RED, spot, radius)
		pygame.display.update() # Обновить дисплей
pygame.quit() # Выход