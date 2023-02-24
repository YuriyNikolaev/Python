# камень ножницы бумага
# на два игрока и комп, т.е на 3и игрока

from random import *

# кол-во раундов
# games = int(input("До скольки побед играем? "))
games = 3

# выбор игрока
# камень = 1, ножницы = 2, бумага = 3
user1 = int(input("USER1, Введите 1 - камень, 2 - ножницы, 3 - бумага  "))
user2 = int(input("USER2, Введите 1 - камень, 2 - ножницы, 3 - бумага  "))

# выбор компьютера
pc = randrange(1, 3, 1)

# кол-во побед
win_user1 = 0
win_user2 = 0
win_pc = 0


# игровой цикл
while win_user1 < games and win_user2 < games and win_pc < games:

    # проверка условий
    if user1 == pc and user2 == pc and user1 == user2:
        print("Ничья!")
    elif user1 == 1 and pc == 2:
        print("Выиграл игрок1")
        win_user1 += 1
    elif user1 == 2 and pc == 3:
        print("Выиграл игрок1")
        win_user1 += 1
    elif user1 == 3 and pc == 1:
        print("Выиграл игрок1")
        win_user1 += 1

    else:
        print("Выиграл комп1")
        win_pc += 1

        # выбор компьютера
    pc = randrange(1, 4, 1)

    # выбор игрока
    user = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага:  "))

print("======")
print("Итого:")
print("win_user1 = ", win_user1)
print("win_user2 = ", win_user2)
print("win_pc = ", win_pc)
