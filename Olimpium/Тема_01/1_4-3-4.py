a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
string = input("Введите операцию (+, -, *, /): ")

if(string == "+"):
    print("a + b =", a+ b)
elif(string == "-"):
    print("a - b =", a - b)
elif(string == "*"):
    print("a * b =", a * b)  
elif(string == "/"):
    if( a == 0 or b == 0):
        print("На ноль делить нельзя")
    else:
        print("a / b =", a / b)  
else:
    print("Неверная операция")