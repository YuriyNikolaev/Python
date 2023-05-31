# 3_1_5.py

# Напишите функцию, вычисляющую длину отрезка по координатам его концов. 
# Какие переменные вы используете в задаче: глобальные или локальные?

from math import *

# заготовка

first_x = float(input('Введите первую координату Х'))
first_y = float(input('Введите первую координату Y'))

prev_x = first_x
prex_y = first_y

line = input("Введите следующую координату Х (Enter, чтобы выйти): ")

while line != "":
    x = float(line)
    y = float(input("Введите следующую координату Y: "))
    
    dist = sqrt(pow((prev_x - x), 2) + pow((prex_y), 2))
    

dist = sqrt(pow((prev_x - x), 2) + pow((prex_y), 2))
perimetr = perimetr + dist

print("Периметр многоугольника равен", perimetr)