# Filename RandomSmileys.py

import turtle
import random

t = turtle.Pen()
t.speed(0)
t.hideturtle() #скрывает черепашку с экрана + увеличивает скорость отрисовки

turtle.bgcolor("black")

def draw_smiley(x, y):
	t.penup()
	t.setpos(x, y)
	t.pendown()

	# Код отрисовки
	# Голова
	t.pencolor("yellow")  # устанавливаем желтый цвет ручки
	t.fillcolor("yellow") # устанавливаем желтый цвет заливки
	t.begin_fill()		  # сообщаем, что хотим залить окружность желтым цв.
	t.circle(50) 		  # рисуем окружность радиусом 50 пикселей
	t.end_fill()		  # заливаем окружность желт цветом

	# Левый глаз
	t.setpos(x-15, y+60)
	t.fillcolor("blue")
	t.begin_fill()
	t.circle(10)		  # рисуем окружность радиусом 10 пикселей
	t.end_fill()

	# Правый глаз
	t.setpos(x+15, y+60)
	t.fillcolor("blue")
	t.begin_fill()
	t.circle(10)		  # рисуем окружность радиусом 10 пикселей
	t.end_fill()

	# Рот
	t.setpos(x-25, y+40)
	t.pencolor("black")  # меняем цвет ручки на черный
	t.width(10)			 # устанавливаем толщину ручки 10
	t.goto(x-10, y+20)	 # перемещает ручку в нужные координаты
	t.goto(x+10, y+20)
	t.goto(x+25, y+40)
	t.width(1)			 # устанавливает толщину ручки обратно на 1 ед.

for n in range(50):
	x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
	y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)

	draw_smiley(x, y)