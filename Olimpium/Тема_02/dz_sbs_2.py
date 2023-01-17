# dz_sbs_2.py
# камень ножницы бумага
from random import *


# камень = 1
# ножницы = 2
# бумага = 3

# выбор игрока
# user = 0
user = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага"))

# выбор компьютера
pc = randrange(1, 3, 1)

# кол-во побед
win_user = 0
win_pc = 0


# игровой цикл
while user != 0:
	# проверка условий
	# игрок выбрал камень
	# если игрок = камень и комп = камень, тогда - ничья444
	if user == 1 and pc == 1:
		print("Ничья: Камень-Камень")
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# если игрок = камень и комп = ножницы, тогда - выиграл игрок
	elif user == 1 and pc == 2:
		print("Выиграл игрок. Игрок = камень, комп = ножницы")
		win_user = win_user + 1
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# если игрок = камень и комп = бумага, тогда - выиграл комп 
	elif user == 1 and pc == 3:
		print("Выиграл комп. Игрок = камень, комп = бумага")
		win_pc = win_pc + 1
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)


	# игрок выбрал ножницы
	# если игрок = ножницы и комп = камень, тогда - выиграл комп
	if user == 2 and pc == 1:
		print("Выиграл комп. Игрок = ножницы, комп = камень")
		win_pc = win_pc + 1
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# если игрок = ножницы и комп = ножницы, тогда - ничья
	elif user == 2 and pc == 2:
		print("Ничья. Ножницы - ножницы")
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# если игрок = ножницы и комп = бумага, тогда - выиграл игрок
	elif user == 2 and pc == 3:
		print("Выиграл игрок. Игрок = ножницы, комп = бумага")
		win_user = win_user + 1
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# игрок выбрал бумагу
	# если игрок = бумага и комп = камень, тогда - выиграл игрок
	if user == 3 and pc == 1:
		print("Выиграл игрок. Игрок = бумага, комп = камень")
		win_user = win_user + 1
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# если игрок = бумага и комп = ножницы, тогда - выиграл комп
	elif user == 3 and pc == 2:
		print("Выиграл комп. Игрок = бумага, комп = ножницы")
		win_pc = win_pc + 1
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)

	# если игрок = бумага и комп = бумага, тогда - ничья 
	elif user == 3 and pc == 3:
		print("Ничья. Бумага - бумага")
		print("win_user = ", win_user)
		print("win_pc = ", win_pc)


	# для тестов
	print("==========")
	print("pc = ", pc)
	print("user = ", user)

	# выбор компьютера
	pc = randrange(1, 4, 1)
	
	# выбор игрока
	user = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага, 0 - выход"))




# print("win_user = ", win_user)
# print("win_pc = ", win_pc)
print("До свидания!")