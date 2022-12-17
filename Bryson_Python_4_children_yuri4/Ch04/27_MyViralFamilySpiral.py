# Filename 27_MyViralFamilySpiral.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

family = []

name = turtle.textinput("Моя семья", "Введите имя или нажмите [ENTER], чтобы выйти:")


while name != "":
    family.append(name)

    name = turtle.textinput("Моя семья", "Введите имя или нажмите [ENTER], чтобы выйти:")

for m in range(100):
    t.forward(m*4)
    position = t.position() # Запомнить этот угол спирали
    heading = t.heading()   # Запомнить направление следования

    for n in range(int(m/2)):
        t.pencolor(colors[n%len(family)])
        t.pendown()
        t.forward(n*4)
        t.write(family[n % len(family)], font=("Arial", int((m + 4) / 4), "bold"))
        t.left(360 / len(family) - 2)  # Повернуть влево
        t.penup()

    t.setx(position[0])  # Вернуться в положение х спирали
    t.sety(position[1])  # Вернуться в положение у спирали
    t.setheading(heading)  # Указать на направление большой спирали
    t.left(360 / len(family) + 2)  # Нацелиться на следующую точку большой спирали
