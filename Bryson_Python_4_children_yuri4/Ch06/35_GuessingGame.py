# Filename 35_GuessingGame.py

import random # обращаемся к модулую random
the_number = random.randint(1, 10) # обращаемся к функции генерации случайных ЦЕЛЫХ цисел
guess = int(input("Угадайте число от 1 до 10: ")) # введите чисо наугад
while guess != the_number:
	if guess > the_number:
		print(guess, "Слишком велико. Попробуйте снова.")
	if guess < the_number:
		print(guess, "Слишком мало. Попробуйте снова.")
	guess = int(input("Еще одна попытка: "))
print(guess, "Правильное число! Вы победили!")