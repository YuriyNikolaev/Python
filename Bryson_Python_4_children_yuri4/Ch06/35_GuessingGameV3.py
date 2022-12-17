# Filename 35_GuessingGameV3.py
# !!! РАБОТАЕТ
# Добавим внешний цикл, хочет ли юзер сыграть еще раз?

import random # обращаемся к модулую random

game_yes = input("Хотите сыграть? (д,н)").lower()
#guess = int(input("Угадайте число от 1 до 10: ")) # введите чисо наугад

while (game_yes != 'н'): 
	number_of_tries = 1  # Число попыток
	guess = int(input("Угадайте число от 1 до 10: ")) # введите чисо наугад
	the_number = random.randint(1, 10) # обращаемся к функции генерации случайных ЦЕЛЫХ цисел

	while guess != the_number:
		number_of_tries += 1
		if guess > the_number:
			print(guess, "Слишком велико. Попробуйте снова.")
		if guess < the_number:
			print(guess, "Слишком мало. Попробуйте снова.")
		guess = int(input("Еще одна попытка: "))

	print(guess, "Правильное число! Вы победили!")
	print("Количество попыток: ", number_of_tries)
	
	game_yes = 	input("Хотите сыграть еще? (д,н)").lower()

print("Спасибо за игру!")