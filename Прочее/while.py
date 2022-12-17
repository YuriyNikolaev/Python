number = 23
running = True

while running:
    guess = int(input('Введите число :'))

    if guess == number:
        print('Вы угадали.')
        running = False #Это останавливает цикл
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл закончен.')
    #Здесь можно выполнить еще все, что вам нужно

print('Завершение.')
