number = input('Введите 1 - рекомендация, off - завершить: ')
while number != 'off':
    if number == '1':
        preference = input('Ваше настроение: ')
        if preference == 'весёлое':
            print('Мультфильм Шрек')
        else:
            print('Мультфильм Алладин')
    number = input('Введите 1 - рекомендация, off - завершить ')