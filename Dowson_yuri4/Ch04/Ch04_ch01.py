# filename Ch04_ch01.py
# Программа запрашивает нач и кон число и шаг, и выводит последовательность
# чисел от нач до кнечного с указанным шагом

start = int(input("Введите начальное число: "))
finish = int(input("Введите конечное число: "))
step = int(input("Введите шаг: "))

for item in range(start, finish, step):
	print(item)

input("\nНажмите Энтер, чтобы выйти")

