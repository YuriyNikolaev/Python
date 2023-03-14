# 2_3_1-5.py
# Задать числовой список случайным образом.
# Заменить значение элементы в списке на их квадраты.

from random import randint

z = [randint(-10, 10) for i in range(10)]
print(z)
print("новыйсписок:")
z = [x * x for x in z]
print(z)
