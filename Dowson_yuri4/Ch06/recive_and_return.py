# filename recive_and_return.py
# Принимай - возвращая
# Демонстрирует параметры и возвращаемые значения

# функция принимает аргумент
def display(message):
	print(message)

# функция возвращает значение
def give_me_five():
	five = 5
	return five

# функция принимает аргумент и возвращает значение
def ask_yes_no(question):
	""" Задает вопрос с ответом 'да' или 'нет'. """
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response
	
# основная часть 

input("Продолжить ")

display("Вам сообщение.\n")

input("Продолжить ")

number = give_me_five()
print("Вот что возвратила функция give_me_five():", number)

input("Продолжить ")

answer = ask_yes_no("\nПожалуйста, введите 'y' или 'n': ")
print("Спасибо, что ввели: ", answer)

input("\n\nНажмите Enter, чтобы выйти.")
