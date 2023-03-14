# 2_2_4-3.py
# Тема 2. Занятие 4.Этап 2. Задача 3

# На вход программе подается строка текста. 
# Напишите программу, которая выводит индекс второго вхождения буквы «р». 
# Если буква «р» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.


my_string = "базовую и расширенную версию строки "
# my_string = "базовую и версию"
# my_string = "базовую и "

# вариант 1
count = 0

for i in range(0, len(my_string)):
    # print(i, end=" ")
    if my_string[i] == 'р':
        count += 1
        print("i = ",i, "count = ", count)

if 0 < count <= 2:
    print("-1")
elif count == 0:
    print("-2")
else:
    print(count)


# вариант 2
my_string = input() 
# if my_string.count('p')==1:
#     print(-1)
# elif my_string.count('p')==0:
#     print(-2)
# else:
#     my_string = my_string.replace('p', '*' , 1)
#     print(my_string.find('p'))
