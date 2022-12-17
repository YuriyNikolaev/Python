# filename high_scores.py 
# Рекорды
# Демонстрирует списочные методы
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
	# вывод результатов на экран
	elif choice == "1":
		print("Records")
		for score in scores:
			print(score)
	# добавление рекорда
	elif choice == "2":
		score = int(input("Впишите свой рекор: "))
		scores.append(score)
	elif choice == "3":
		score = int(input("WHich of the records you want to del?: "))
		if score in scores:
			scores.remove(score)
		else:
			print("Results ", score, "not in records list.")

	# сортировка списка рекордов
	elif choice == "4":
		scores.sort(reverse=True)
		for score in scores:
			print(score)
	
	# обработка ошибочного ввода
	else:
		print("Sorry, ther is no such item in menu ", choice)
		
input("\n\nPlease, click Enter if you whant to exit.")
