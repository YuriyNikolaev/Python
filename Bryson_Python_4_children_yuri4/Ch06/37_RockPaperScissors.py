# Filename 37_RockPaperScissors.py

import random
choices = ["камень", "ножницы", "бумага"]
print("Камень давит ножницы. Ножницы режут бумагу. Бумага накрывает камень.")

player = input("выберите: камень, ножницы, бумага или выйти?  ")

while player != "выйти": # Играть, пока пользователь не выйдет 
	player = player.lower() # Поменять ввод пользователя
						    # на нижний регистр
	computer = random.choice(choices) # Выбрать один из предметов
	print("Твой выбор " + player + ", компьютер выбрал " + computer + ".")

	if player == computer:
		print("Ничья!")
	elif player == "камень":
		if computer == "ножницы":
			print("Вы победили!")
		else:
			print("Победил компьютер!")
	elif player == "бумага":
		if computer == "камень":
			print("Вы победили!")
		else:
			print("Победил компьютер!")
	elif player == "ножницы":
		if computer == "бумага":
			print("Вы победили!")
		else:
			print("Победил компьютер!")
	else:
		print("Произошла ошибка...")
	print() # Пропустить строку 
	player = input("Выберите: камень, ножницы, бумага или выйти?  ")