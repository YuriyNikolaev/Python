# 1_6-4-3.py

# from math import sqrt
# # Переменная для хранения периметра многоугольника
# perimeter = 0

# # Запрашиваем координаты первой точки
# first_x = float(input("Введите первую координату X: "))
# first_y = float(input("Введите первую координату Y: "))
# # Инициализируем координаты предыдущей точки начальными значениями
# prev_x = first_x
# prev_y = first_y
# # Запрашиваем остальные координаты
# line = input("Введите следующую координату X (Enter для окончания ввода): ")
# while line != "":
#  # Преобразуем координату X в число и запрашиваем координату Y
#  x = float(line)
#  y = float(input("Введите следующую координату Y: "))
#  # Рассчитываем расстояние до предыдущей точки и добавляем к периметру
#  dist = sqrt((prev_x -x) ** 2 + (prev_y - y) ** 2)
#  perimeter = perimeter + dist
#  # Устанавливаем значения предыдущих координат
#  # для следующей итерации
#  prev_x = x
#  prev_y = y
#  # Запрашиваем следующую координату X
#  line = input("Введите следующую координату X (Enter для окончания ввода): ")
# # Рассчитываем расстояние от последней точки до первой и добавляем к периметру
# dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
# perimeter = perimeter + dist
# # Отображаем результат
# print("Периметр многоугольника равен", perimeter)


# мой вариант, он рабочий
from math import *

perimetr = 0

first_x = float(input('Введите первую координату Х'))
first_y = float(input('Введите первую координату Y'))

prev_x = first_x
prex_y = first_y

line = input("Введите следующую координату Х (Enter, чтобы выйти): ")

while line != "":
    x = float(line)
    y = float(input("Введите следующую координату Y: "))
    
    dist = sqrt(pow((prev_x - x), 2) + pow((prex_y), 2))
    perimetr = perimetr + dist
    
    prev_x = x
    prex_y = y
    
    line = input("Введите следующую координату Х (Enter, чтобы выйти): ")

dist = sqrt(pow((prev_x - x), 2) + pow((prex_y), 2))
perimetr = perimetr + dist

print("Периметр многоугольника равен", perimetr)
    