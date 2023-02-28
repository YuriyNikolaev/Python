# dz_sbs_4.py
# камень ножницы бумага
# на одного игрока, комп и 5ть элементов

from random import *


# кол-во побед
win_user = 0
win_pc = 0

# выбор игрока
user = int(input("Введите число (0 - выход, 1 - камень, 2 - ножницы, 3 - бумага, 4 - огонь, 5 - колодец): "))

# выбор компьютера
pc = randrange(1, 6, 1)

print("user choice = ", user)
print("pc choice = ", pc)

# игровой цикл
while win_user < 3 and win_pc < 3:

	if user == 0:
		break
	elif user not in range(1, 6):
		print("Неверный ход")
	

    # проверка условий
	if user == pc:
		print("Ничья!")
	elif any((user == 1 and pc == 2,
			  user == 1 and pc == 4,
			  user == 2 and pc == 3,
			  user == 2 and pc == 5,
			  user == 3 and pc == 1,
			  user == 3 and pc == 5,
			  user == 4 and pc == 2,
			  user == 4 and pc == 3,
			  user == 5 and pc == 1,
			  user == 5 and pc == 4)):
		print("партию выиграл игрок")
		win_user += 1
	else:
		print("партия за компом")
		win_pc += 1



    # выбор компьютера
	pc = randrange(1, 6, 1)

    # выбор игрока
	user = int(input("Введите число (0 - выход, 1 - камень, 2 - ножницы, 3 - бумага, 4 - огонь, 5 - колодец): "))

print("win_user = ", win_user)
print("win_pc = ", win_pc)
print("До свидания!")



"""
камень
ножницы
бумага
огонь
колодец

─	Камень тупит ножницы и гасит огонь, но тонет в колодце и заворачивается бумагой.

─	Бумага заворачивает камень и накрывает колодец, но горит в огне и режется ножницами.

─	Огонь плавит ножницы и сжигает бумагу, но тушится колодцем или камнем.

─	Ножницы режут бумагу и колодезную верёвку, но тонут в воде и плавятся в огне.

─	Колодец топит камень и гасит огонь, но накрывается бумагой, а ножницы режут его верёвку.


"""


