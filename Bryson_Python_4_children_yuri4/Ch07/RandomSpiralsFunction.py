# Filename RandomSpiralsFunction.py

import random
import turtle

t = turtle.Pen()
t.speed(0) # сам добавил
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

def random_spiral(): # Определили функцию random_spiral
	t.pencolor(random.choice(colors)) # Выбрать случайный цвет
	size = random.randint(10, 40) 	  # Задать случайный размер спирали
	# Сгенерировать случайную (х, у) координату на экране
	x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
	y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)

	t.penup()
	t.setpos(x,y)
	t.pendown()

	for m in range(size):
		t.forward(m*2)
		t.left(91)

for n in range(50): # Применяем нашу функцию random_spiral в цикле отрисовки спирали
	random_spiral()