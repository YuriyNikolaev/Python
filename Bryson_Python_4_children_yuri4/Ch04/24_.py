# Filename  24_.py

import turtle # Установка графики turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

name1 = turtle.textinput("Введите первое имя", "Имя1" )
name2 = turtle.textinput("Введите второе имя", "Имя2")
name3 = turtle.textinput("Введите третье имя", "Имя3")

names = [name1, name2, name3]

while names != "":
	for x in range(100):
		t.pencolor(colors[x%4])
		t.penup()
		t.forward(x*4)
		t.pendown()
		t.write(names[x%3], font=("Arial", int((x+4) / 4), "bold"))
		t.left(92)





