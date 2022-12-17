# Filename ShowDot.py

import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

keep_going = True
GREEN = (225, 225, 225) # Три цвета RGB для зеленого (GREEN) цвета

radius = 50

while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False
	pygame.draw.circle(screen, GREEN, (500,100), radius)
	pygame.display.update()

pygame.quit()
