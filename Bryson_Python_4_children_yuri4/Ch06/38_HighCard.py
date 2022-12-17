# Filename 38_HighCard.py

import random 

suits = ["пики", "бубны", "черви", "крести"]  # масть карты
faces = ["двойка", "тройка", "четверка", "пятерка", "шестерка", "семерка", \
"восьмерка", "девятка", "десятка", "валет", "дама", "король", "туз"] # номинал карты

keep_going = True

while keep_going:

	my_suit = random.choice(suits)
	my_face = random.choice(faces)

	your_suit = random.choice(suits)
	your_face = random.choice(faces)

	print("У меня ", my_face, " ", my_suit )
	print("У тебя ", your_face, " ", your_suit)

	if faces.index(my_face) > faces.index(your_face):
		print("Игрок победил")
	elif faces.index(my_face) < faces.index(your_face):
		print("Выиграл компьютер")

	answer = input("Нажмите [ENTER], чтобы продолжить или любую клавишу, чтобы выйти. ")
	#if answer == "":
	#	keep_going = True
	#else:
	#	keep_going = False
	keep_going = (answer == "")
