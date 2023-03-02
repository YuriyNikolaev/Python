# 2_2_4-4.py
# Тема 2. Занятие 4.Этап 2. Задача 4

# Дана строка, в которой буква h встречается как минимум два раза. 
# Разверните последовательность символов, заключенную между первым 
# и последним появлением буквы h, 
# в противоположном порядке.

my_string = "Build, run, and share Python code online for free with the help of online-integrated"

a = my_string.find('h')
b = my_string.rfind('h')
c = my_string[a:b]
d = my_string[b:a-1:-1]

print(c)
print(d)