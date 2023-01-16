m = int(input("Введите вес тора в граммах: "))
topping = input(("Нужна ли начинка? Введите 'нет', 'фрукты' либо что-то другое: "))
price1 = 3000
price2 = 5000

if(topping == "фрукты"):
    price = 1000
    if(m < 2000):
        price = price + price1
        print("цена = ", price)
    else:
        price = price + price2
        print("цена = ", price)

elif(topping == "нет"):
    price = 0
    if(m < 2000):
        price = price + price1
        print("цена = ", price)
    else:
        price = price + price2
        print("цена = ", price)
else:
    price = 500
    if(m < 2000):
        price = price + price1
        print("цена = ", price)
    else:
        price = price + price2
        print("цена = ", price)