n= float(input("Введите начальную дистанцию "))
k= int(input("Введите количество дней "))
for i in range (k):
    n+=n**0.1
print("конечная дистанция ", n)