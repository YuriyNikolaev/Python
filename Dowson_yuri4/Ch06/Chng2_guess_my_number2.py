# filename Chng2_guess_my_number2.py
# Отгадай число

import random
# начальные значения

print("Добро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток.\n")

# начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 0

def gues_number(guess, the_number):
	global tries
	# цикл угадывания
	while guess != the_number:
		if guess > the_number:
			print("Меньше...")
		else:
			print("Больше...")
		guess = int(input("Ваше предположение: "))
		tries += 1
	return the_number, tries 

gues_number(guess, the_number)

print("Вам удалось отгадать число! Это в самом деле ", the_number)
print("Вы затратили на отгадывание всего лишь ", tries, "попыток!\n")
input("\nНажмите Ентер шобы выйти!") 