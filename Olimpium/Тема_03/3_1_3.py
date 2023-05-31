# 3_1_3.py
# Написать функцию, которая выводит только гласные символы введенной строки

s = "удаляя из него лишние пробелы"


alphabet = "aеийоуыэюя"

def abc(s):
    new_s = ""
    for i in s:
        if i in alphabet:
            new_s = new_s + i
    print(new_s)
    
abc(s)