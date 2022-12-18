height = int(input("Введите рост в см: "))
weight = int(input("Введите вес в кг: "))

weightOptim = height - 100

if(weight < weightOptim):
    print("Вам нужно набрать вес")
elif(weight > weightOptim):
    print("Вам нужно сборосить")
else:
    print("Вес в норме")
