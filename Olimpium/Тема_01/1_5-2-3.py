# 1_5-2-3.py
# решение присланное
# print("1-прямоугольник, 2-треугольник, 3-круг")
# figure = input("Выберите фигуру: ")
 
# if figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь: %.2f" % (a * b))
# elif figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     p = (a + b + c) / 2
#     from math import sqrt
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %.2f" % s)
# elif figure == '3':
#     r = float(input("Радиус круга R = "))
#     from math import pi
#     print("Площадь: %.2f" % (pi * r ** 2)) # округление до двух знаков после запятой
# else:
#     print("Ошибка ввода")

# мое решение
# 1-5-3
from math import *

print("Вычисляем площадь прямоугольника, треугольника или круга")
temp = input("Выберите, что будем считать. Введите: п, т или к")

if temp == "п":
    print("Считаем площадь прямоугольника")
    # areaRectacngle 
    # d = 3
    # e = 5
    d = int(input("d = "))
    e = int(input("e = "))
    areaRectacngle = d * e
    print("areaRectacngle = ", areaRectacngle)
    
elif temp == "т":
    print("Считаем площадь треугольника")
    #treangle
    # a = 3
    # b = 4
    # c = 5
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    p = (a + b + c) / 2
    areaTriangle = sqrt(p * (p - a) * (p - b) * (p - c))
    print("areaTriangle = ", areaTriangle)
    
elif temp == "к":
    print("Считаем площадь круга")
     # areaCircle 
    # radius = 3
    radius = int(input("radius = "))
    areaCircle = round((pi * (radius**2)), 2) 
    print("areaCircle = ", areaCircle)

else:
    print("Выберите, что считаем")
   
