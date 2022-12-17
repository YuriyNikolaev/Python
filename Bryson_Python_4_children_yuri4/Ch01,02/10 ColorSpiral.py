# 6 Filename 10 ColorSpiral.py - Рисование квадратной спирали

import turtle

t = turtle.Pen()

turtle.bgcolor("black")

# Вы можете задать от 2х до 6ти граней - и получить крутые фигуры!

sides = 6

colors = ["red", "yellow", "blue", "orange","green", "purple"]

for x in range (360):
    t.pencolor(colors[x%sides])
    t.forward(x*6/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

