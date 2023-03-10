# filename dz_103_3-1.py
# на основе guess_my_number.py
# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число, и компьютер говорит,
# предположение больше/меньше, чем загаданное число,
# или попал в точку
# 
# МОДИФИКАЦТЯ 1
#  Измените программу «Отгадай число» таким образом, чтобы у игрока было ограниченное количество попы­
# ток. Если игрок не укладывается в заданное чисnо (и проигрывает), то программа должна выводить сколь
# возможно суровый текст.

import random

print("Добро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за максимум 10 попыток.\n")

# начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 1
max_tries = 10

# цикл угадывания
while guess != the_number:
	if guess > the_number:
		print("Меньше...")
	else:
		print("Больше...")
	guess = int(input("Ваше предположение: "))
	tries += 1

	if tries == max_tries:
		#print("У вас кончились попытки.")
		break
	

if guess != the_number:
	print("У вас кончились попытки.")
	print("Вы затратили на отгадывание ", tries, "попыток!\n")

else:
	print("Вам удалось отгадать число! Это в самом деле ", the_number)
	print("Вы затратили на отгадывание всего лишь ", tries, "попыток!\n")

input("\nНажмите Ентер шобы выйти!") 