# Filename 24_SpiralFamily.py

import turtle # Настройка графики Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "brown", "gray", "pink"]
family = [] # Создать пустой список для имен родственников
# Запросить первое имя

name = turtle.textinput("Моя семья", "Введите имя или нажмите [ENTER], чтобы выйти:")
# Продолжить заправшивать имена
while name != "":  # Создаем цикл "Пока", он заполняет список имен
    family.append(name) # Добавить имя к пустому списку
    # Запросить еще одно имя или выйти
    name = turtle.textinput("Моя семья", "Введите имя или нажмите [ENTER], чтобы выйти:")

# Нарисовать на экране спираль из имен
for x in range(100): # Это второй цикл, который подставляет имена из первого цикла и ристует спираль
    t.pencolor(colors[x%len(family)]) # Переключение цветов
    t.penup() # Не рисовать обычные прямые линии
    t.forward(x*4) # Просто передвинуть черепашку по экрану
    t.pendown() # Нарисовать соедующее имя родственника
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/len(family) + 2) # Повернуть влево
