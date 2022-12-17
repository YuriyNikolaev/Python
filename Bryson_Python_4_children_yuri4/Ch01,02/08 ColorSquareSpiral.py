# 6 Filename 8 ColorSquareSpiral.py - Рисование квадратной спирали

import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]

for x in range (100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)

