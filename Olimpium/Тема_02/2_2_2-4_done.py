# 2_2_2-4.py
# Тема 2. Занятие 2. Этап 2. Задача 4

# заменить пробелы знаком тире "–"
# также заменить на "–" несколько пробелов
s = ' В строке заменить  пробелы   знаком тире '
new_s1 = " ".join(s.split())

new_s2 = new_s1.replace(" ", "-")
print(s)
print(new_s1)
print(new_s2)
