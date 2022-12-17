# filename high_scores2.py 
# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != "0":
	print(
		"""
		Records
		0 - Exit
		1 - Viwe Records
		2 - Insert Records
		3 - Del Records
		4 - Sort list
		"""
	)
	choice = input("Your Choice: ")
	print()

	# Exit
	if choice == "0":
		print("Goodbuy.")
	# вывод таблицы рекордов
	elif choice == "1":
		print("Рекорды\n")
		print("ИМЯ\tРЕЗУЛЬТАТ")
		for entry in scores:
			score, name = entry
			print(name, "\t", score)
	# add a score
	elif choice == "2":
		name = input("Впиши имя игрока: ")
		score = int(input("Впишите его результат: "))
		entry = (score, name)
		scores.append(entry)	
		scores.sort(reverse=True)
		scores = scores[:5] # в списке остается только 5 рекордов
		# непонятный пользовательский ввод
	else:
		print("Извините нет такого пункта в меню", choice)

input("\n\nНажмите Enter, чтобы выйти.")


