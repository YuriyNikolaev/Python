# filename ch1_surprise_my.py
import random

print("Сыграем в игру 'Сюрприз из пирожка'.")

while True:

	a = random.randint(1, 5)

	if a == 1:
		print("пирожок")
	elif a == 2:
		print("мячик")
	elif a == 3:
		print("мишка")
	elif a == 4:
		print("велик")
	else:
		print("луна")

	if input("Выйти? Набери 'д': ") == "д":
		break


input("\nНажмите Ентер шобы выйти!") 