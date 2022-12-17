# Filename 32_WhatsMyGrade.py

grade = eval(input("Введите количество баллов (0-100): "))
if grade >= 90:
	print("У вас 5!:)")
elif grade >=80:
	print("У вас 4!")
elif grade >=70:
	print("У вас 3.")
elif grade >=60:
	print("У вас 2...")
else:
	print("У вас 1. :(")