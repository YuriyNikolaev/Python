# Filename DiskoDot.py

import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True

#R = 0
#G = 0
#B = 0
radius = 0
x = 0
y = 0
BLACK = (0,0,0) # устанавливаем черный цвет для заливки экрана
timer = pygame.time.Clock() # Таймер для замедления fps

while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False

	x = random.randrange (50,700) # случайным образом гереним координаты
	y = random.randrange (50, 500) # точки отрисовки
	radius = random.randint(5, 100)
	#R = random.randint(0, 255)
	#G = random.randint(0, 255)
	#B = random.randint(0, 255)
	color = ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
	screen.fill(BLACK) # заливает экран черным после отрисовки
	#pygame.draw.circle(screen, GREEN, (500,100), radius)
	pygame.draw.circle(screen, color, (x, y), radius) # рисуем окружность
	pygame.display.update() # обновляем экран
	timer.tick(1)# Используем таймер

pygame.quit()
