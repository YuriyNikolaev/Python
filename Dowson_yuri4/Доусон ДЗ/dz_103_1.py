# dz_103_1.py
# Программа-симулятор пирожка с «сюрпризом»,
# При запуске она отображает один из
# пяти различных «Сюрпризов», выбранный случайным образом.
# Реализовал путем создания списка сюрпризов
# и выбор сюрприза через функцию random.choice()


import random

surprises = ["сюрприз1", "сюрприз2", "сюрприз3", "сюрприз4", "сюрприз5"]

random_surprise = random.choice(surprises)

print("Ваш сюрприз, это ", random_surprise)


