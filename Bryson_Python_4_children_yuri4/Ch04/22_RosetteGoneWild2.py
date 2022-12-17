# Filename 22 RosetteGoneWild.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "white", "gray"]
# Попросить пользователя задать количество кругов в розетке,
# по умолчанию 6
number_of_circles = int(turtle.numinput("Количество окружностей", "Сколько окружностей в вашей розетк?", 6))
for x in range(number_of_circles):
    t.pencolor(colors[x])
    t.circle(100+x*10)
    t.circle(100 - x*10)
    t.left(360/number_of_circles)
