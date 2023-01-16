# from math import *
# n, a = float(input()), float(input())
# ans = (n * pow(a, 2)) / (4 * tan(pi / n))
# print(ans)


# мой вариант
from math import *

print("Вычисляем площадь многугольника")
# a = 3
# n = 5
a = float(input("длина сторны a = "))
n = int(input("число сторон n = "))

area = (n * (a**2)) / (4 * tan(pi / n))

print(round(area, 2))