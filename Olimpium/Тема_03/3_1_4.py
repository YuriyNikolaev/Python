# 3_1_4.py
# В зависимости от выбора пользователя вычислить площадь круга, 
# прямоугольника или треугольника. 
# Для вычисления площади каждой фигуры должна быть написана 
# отдельная функция.


from math import *

# функция расчета площади круга
def circle_sqr(r):
    areaCircle = round((pi * (radius**2)), 2) 
    print("areaCircle = ", areaCircle)


print("Вычисляем площадь прямоугольника, треугольника или круга")
temp = input("Выберите, что будем считать. Введите: п, т или к: ")

# площадь прямоугольника 
if temp == "п":
    print("Считаем площадь прямоугольника")
    # areaRectacngle 
    # d = 3
    # e = 5
    d = int(input("d = "))
    e = int(input("e = "))
    areaRectacngle = d * e
    print("areaRectacngle = ", areaRectacngle)

# площадь треугольника  
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
    circle_sqr(radius)
    

else:
    print("Выберите, что считаем")