# 6 Filename 9 ColorCircleSpiral.py - Рисование квадратной спирали

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

for x in range (200):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)

