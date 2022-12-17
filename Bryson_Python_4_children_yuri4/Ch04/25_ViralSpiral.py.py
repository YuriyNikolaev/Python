# Filename 25_ViralSpiral.py

import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")

sides = int(turtle.numinput("Количество сторон", "Сколько будет сторон у \
 вашей спирали (2-6)?", 4, 2, 6))
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

for m in range(100):
    t.forward(m*4)
    position = t.position() # Запомнить этот угол спирали
    heading = t.heading() # Запомнить направление следования

    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0]) # Вернуться в положение х спирали
    t.sety(position[1]) # Вернуться в положение у спирали
    t.setheading(heading) # Указать на направление большой спирали
    t.left(360/sides + 2) # Нацелиться на следующую точку большой спирали



