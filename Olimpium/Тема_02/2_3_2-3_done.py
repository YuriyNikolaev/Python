# 2_3_2-3.py
# Найти в списке наибольший и наименьший элементы. Вывести их индексы на экран.

numbers = [1, 2, 3, 4, 5, 6]

# находим максимально большой элемент списка
max_num = max(numbers)

# находим его индекс
max_index = numbers.index(max_num)

print("max_num = ", max_num,", ", "max_index = ", max_index)

# находим минимальный элемент списка
min_num = min(numbers)

# находим его индекс
min_index = numbers.index(min_num)

print("min_num = ", min_num,", ",  "min_index = ", min_index)