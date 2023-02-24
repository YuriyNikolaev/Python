# dz_sbs_2.py -- До 3х побед Камень ножницы бумага
from random import *

# кол-во раундов
# games = int(input("До скольки побед играем? "))
games = 3

# выбор игрока
# камень = 1, ножницы = 2, бумага = 3
user = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага  "))

# выбор компьютера
pc = randrange(1, 3, 1)

# кол-во побед
win_user = 0
win_pc = 0


# игровой цикл
while win_user < games and win_pc < games:

    # проверка условий
    if user == pc:
        print("Ничья!")
    elif user == 1 and pc == 2:
        print("Выиграл игрок")
        win_user += 1
    elif user == 2 and pc == 3:
        print("Выиграл игрок")
        win_user += 1
    elif user == 3 and pc == 1:
        print("Выиграл игрок")
        win_user += 1
    else:
        print("Выиграл комп")
        win_pc += 1

        # выбор компьютера
    pc = randrange(1, 4, 1)

    # выбор игрока
    user = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага:  "))

print("======")
print("Итого:")
print("win_user = ", win_user)
print("win_pc = ", win_pc)
