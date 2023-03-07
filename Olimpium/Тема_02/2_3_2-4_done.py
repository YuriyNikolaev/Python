# 2_3_2-4.py
# Можно ли выполнить решение предыдущей задачи без встроенных функций? т.е.
# Найти в списке наибольший и наименьший элементы. Вывести их индексы на экран.

numbers = [1, 2, 3, 4, 5, 6]
max_num = 0
max_i = 0

min_num = 0
min_i = 0

for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_i = i
    if numbers[i] < min_num:
        min_num = numbers[i]
        min_i = i
        
print('max_num = ', max_num, ', ' 'max_i = ', max_i)
print('min_num = ', min_num, ', ' 'min_i = ', min_i)
    