# 6 Filename 10 ColorSpiral.py - Рисование квадратной спирали

import turtle

sides = eval(input("Введите число граней от 2х до 6ти:"))

t = turtle.Pen()

turtle.bgcolor("black")

colors = ["red", "yellow", "blue", "orange","green", "purple"]

for x in range (360):
    t.pencolor(colors[x%sides])
    t.forward(x*6/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)

