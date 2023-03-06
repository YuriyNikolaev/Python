# 2_3_2-5.py
# Найти сумму элементов массива, находящимися между наибольшим и наименьшим.

numbers = [1, 2, 3, 4, 5, 6]

# находим максимально большой элемент списка
max_num = max(numbers)

# находим минимальный элемент списка
min_num = min(numbers)


max_index = numbers.index(max_num)
min_index = numbers.index(min_num)


spisok = numbers[min_index + 1 : max_index]

print(sum(spisok))