# 2_2-3.py
# Подсчитать количество гласных букв в строке.
s = "удаляя из него лишние пробелы"
# s = input("Ведите строку")

count = 0

alphabet = "aеийоуыэюя"

for i in s:
    if i in alphabet:
        count += 1
        # print(i, end="")
    # print(count)
print("гласных букв в строке = ", count)