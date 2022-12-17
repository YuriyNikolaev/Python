# Filename 40_Kaleidoscope_v2.py
# добавил случайное количество сторон спирали
# доавил случайную толщину спиралей

import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

for i in range(50):

	t.pencolor(random.choice(colors))
	size = random.randint(10, 40) # размер спирали
	sides = random.randint(3, 8) # количество сторон спирали
	thick = random.randint(1, 6) # толщина линий
	x = random.randrange(0, turtle.window_width()//2)
	y = random.randrange(0, turtle.window_height()//2)

	# Первая спираль
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.width(thick)

	for m in range(size):
		t.forward(m*2)
		t.left(360/sides + 1)

	# Вторая спираль
	t.penup()
	t.setpos(-x,y)
	t.pendown()
	t.width(thick)

	for m in range(size):
		t.forward(m*2)
		t.left(360/sides + 1)

	# Третья спираль
	t.penup()
	t.setpos(x,-y)
	t.pendown()
	t.width(thick)

	for m in range(size):
		t.forward(m*2)
		t.left(360/sides + 1)

	# Четвертая спираль
	t.penup()
	t.setpos(-x,-y)
	t.pendown()
	t.width(thick)

	for m in range(size):
		t.forward(m*2)
		t.left(360/sides + 1)