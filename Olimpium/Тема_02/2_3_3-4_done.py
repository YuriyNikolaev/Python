# 2_3_3-4.py
# 

# Разработать программу, в которой у  пользователя будет запрошен список слов, 
# пока он не оставит строку ввода пустой. После этого на экране должны быть 
# показаны слова, введенные пользователем, но без повторов, – каждое по одному разу. 
# При этом слова должны быть отображены в том же порядке, в  каком их вводили с клавиатуры

user_list = []
# user_list = ['first', 'second', 'first', 'third', 'second']

word = input("Введите слово ")

while word != '':
	user_list.append(word)
	word = input("Введите слово ")

temp_list = []

for word in user_list:
    if word not in temp_list:
        temp_list.append(word)

user_list = temp_list

user_list.sort()

print(user_list)