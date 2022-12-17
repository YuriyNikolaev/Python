# Filename colorspiral.py

"""Модуль для рисования цветных спиралей до 6 граней"""
import turtle
def cspiral(sides=6, size=360, x=0, y=0):
	"""Рисует цветную спираль на черном фоне.

	Аргументы:
	sides - количество граней спирали (по умолчанию 6)
	size - длина последней грани (по умлочанию 360)
	x, y - местоположение спирали от центра экрана
	"""
	t = turtle.Pen()
	t.speed(0)
	t.penup()
	t.setpos(x,y)
	t.pendown()
	turtle.bgcolor("black")
	colors = ["red", "yellow", "blue", "orange", "green", "purple"]
	for n in range(size):
		t.pencolor(colors[n%sides])
		t.forward(n * 3/sides + n)
		t.left(360 / sides + 1)
		t.width(n*sides / 100)
