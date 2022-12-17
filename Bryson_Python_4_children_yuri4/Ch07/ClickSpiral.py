# Filename ClickSpiral.py
import random
import turtle

t = turtle.Pen()
t.speed(0) 
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]


def spiral(x, y): # Определили функцию spiral
	t.pencolor(random.choice(colors)) # Выбрать случайный цвет
	size = random.randint(10, 40) 	  # Задать случайный размер спирали
	t.penup()
	t.setpos(x,y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(91)
		
turtle.onscreenclick(spiral)