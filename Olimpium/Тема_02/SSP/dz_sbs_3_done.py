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
count_win_user1 = 0
count_win_user2 = 0
count_win_pc = 0


# игровой цикл
while True:

    # проверка 1
    if user1 == 1 and user2 == 2:
        # win user1
        # user 1 vs pc
        if user1 == 1 and pc == 2:
            print("win user1")
            count_win_user1 += 1
            print("count_win_user1 = ", count_win_user1)
            print("count_win_user2 = ", count_win_user2)
            print("count_win_pc = ", count_win_pc)
        else:
            print("win pc")
            count_win_pc += 1
            print("count_win_user1 = ", count_win_user1)
            print("count_win_user2 = ", count_win_user2)
            print("count_win_pc = ", count_win_pc)

    # проверка 2
    elif user1 == 2 and user2 == 3:
        # win user1
        # user 1 vs pc
        if user1 == 2 and pc == 3:
            print("win user1")
            count_win_user1 += 1
            print("count_win_user1 = ", count_win_user1)
            print("count_win_user2 = ", count_win_user2)
            print("count_win_pc = ", count_win_pc)
        else:
            print("win pc")
            count_win_pc += 1
            print("count_win_user1 = ", count_win_user1)
            print("count_win_user2 = ", count_win_user2)
            print("count_win_pc = ", count_win_pc)

    # проверка 3
    elif user1 == 3 and user2 == 1:
        # win user1
        # user 1 vs pc
        if user1 == 3 and pc == 1:
            print("win user1")
            count_win_user1 += 1
            print("count_win_user1 = ", count_win_user1)
            print("count_win_user2 = ", count_win_user2)
            print("count_win_pc = ", count_win_pc)
        else:
            print("win pc")
            count_win_pc += 1
            print("count_win_user1 = ", count_win_user1)
            print("count_win_user2 = ", count_win_user2)
            print("count_win_pc = ", count_win_pc)
    
    else:
        print("win user2")
        count_win_user2 += 1
        print("count_win_user1 = ", count_win_user1)
        print("count_win_user2 = ", count_win_user2)
        print("count_win_pc = ", count_win_pc)

    if count_win_user1 > (games - 1) or count_win_user2 > (games - 1) or count_win_pc > (games - 1):
        break

    # выбор компьютера
    pc = randrange(1, 4, 1)

    # выбор игроков
    user1 = int(input("USER1, Введите 1 - камень, 2 - ножницы, 3 - бумага  "))
    user2 = int(input("USER2, Введите 1 - камень, 2 - ножницы, 3 - бумага  "))

    

print("======")
print("Итого:")
print("count_win_user1 = ", count_win_user1)
print("count_win_user2 = ", count_win_user2)
print("count_win_pc = ", count_win_pc)
