# 1_6-2-5.py

# x = int(input())
# p = int(input())
# y = int(input())
# i = 0
# while x < y:
#     x *= 1 + p / 100
#     x = int(100 * x) / 100
#     i += 1
# print(i)

#мой вариант решения
x = 1000 # начальный вклад
p = 0.1 # проценты
y = 5000 # конечная цель вклада
i = 0
while x < y:
    x = int(x + p * x);
    i += 1
    print(x)
    print(i)