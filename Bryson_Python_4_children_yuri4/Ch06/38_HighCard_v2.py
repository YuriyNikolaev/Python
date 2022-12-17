# Filename 38_HighCard_v2.py

import random

suits = ["пики", "бубны", "черви", "крести"]  # масть карты
faces = ["двойка", "тройка", "четверка", "пятерка", "шестерка", "семерка", \
"восьмерка", "девятка", "десятка", "валет", "дама", "король", "туз"] # номинал карты

keep_going = True
hands = 0
my_win = 0      # Побед игрока
your_win = 0	# Побед компьютера
drown_games = 0 # Количество ничейных игр
total_games = 0 # Всего игр

while keep_going and (hands < 26):
	hands += 1

	my_suit = random.choice(suits)
	my_face = random.choice(faces)

	your_suit = random.choice(suits)
	your_face = random.choice(faces)

	print("У меня ", my_face, " ", my_suit)
	print("У тебя ", your_face, " ", your_suit)
	print()

	if faces.index(my_face) > faces.index(your_face):
		my_win += 1 + drown_games
		drown_games = 0
		total_games += 1
		print("Игрок победил")
		print()

	elif faces.index(my_face) < faces.index(your_face):
		your_win += 1 + drown_games
		drown_games = 0
		total_games += 1
		print("Выиграл компьютер")
		print()
		

	#else faces.index(my_face) == faces.index(your_face):
	else:
		total_games += 1
		drown_games += 1 
		print("Ничья!")
		print()

		
	print("Всего игр: ", total_games, "Счет: Компьютер", your_win, ", Игрок", my_win)

	answer = input("Нажмите [ENTER]б чтобы продолжить или любую клавишу, чтобы выйти. ")
	keep_going = (answer =="")

print("Game over")
print()
if my_win > your_win:
	print("Я выиграл игру!")
elif my_win < your_win:
	print("Выиграл чертов комп!")
else:
	print("Это была ничья!")

