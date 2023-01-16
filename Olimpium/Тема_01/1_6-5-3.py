# number = input('Введите 1 - рекомендация, off - завершить: ')
# while number != 'off':
#     if number == '1':
#         preference = input('Ваше настроение: ')
#         if preference == 'весёлое':
#             print('Мультфильм Шрек')
#         else:
#             print('Мультфильм Алладин')
#     number = input('Введите 1 - рекомендация, off - завершить ')


# мой вариант
a = input("enter 1 or off")

while a != "off":
    if a == '1':
        mood = input("enter mood ")
        if mood == "веселое":
            print("Шрек")
        elif mood == '':
            break
        else:
            print("Алладин")