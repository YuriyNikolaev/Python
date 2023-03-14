# 2_2_5-7.py
# Напишите программу, которая принимает строку и две подстроки 
# start и end, а затем определяет, начинается ли строка с фрагмента start, 
# и заканчивается ли подстрокой end. Регистр не учитывать.
# Пример ввода:
# Программирование на Python - лучшее хобби
# про
# про
# Вывод:
# True
# False


text, start, end = input().lower(), input(), input()
print(text.startswith(start))
print(text.endswith(end))