# 2_2_2-3.py
# Тема 2. Занятие 2. Этап 2. Задача 3

# num = input("Введите телефонный номер в формате х(ххх)ххххххх")
num = "8(914)2323232"
simbol = ['(', ')']

for elem in simbol:
    num = (num.replace(elem,""))
    if num.isdigit() and len(num) == 11:
        print(f"{num}", end='\n\n')
    else:
        print(f"Вы ввели не правильно тлф номер\n", end='\n\n')