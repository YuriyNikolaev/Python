# filename craps_roller.py
# Кости
# Демонстрирует генерацию случайных чисел
import random
# создаем случайные числа из диапазона 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1 # здесь +1 т.к считывается диапазон от 0 до 5ти.
total = die1 + die2
print("При вашем броске выпало ", die1, "и ", die2, "очков. В сумме ", total)
# Выход
input("\n\nНажмите Ентер шобы выйти!") 
