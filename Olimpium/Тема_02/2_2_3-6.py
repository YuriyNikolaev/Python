# 2_2_3-6.py
# Тема 2. Занятие 3. Этап 2. Задача 6

# Удалить из строки все символы, заключенные в скобки.



my_string = "abcd(123)efg"
new_string = " "

for i in my_string:
    # print(i, end=",")
    if i == '(' or i == ')':
        continue
    else:
        new_string += i

print(new_string)

 


