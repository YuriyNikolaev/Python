x = 50

def func():
    global x

    print('х равен', x)
    x = 2
    print('Заменяем глоабльное значение х на', x)

func()
print('Значение х составляет', x)
