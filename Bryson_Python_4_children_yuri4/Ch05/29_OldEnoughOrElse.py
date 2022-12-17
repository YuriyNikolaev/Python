# Filename 29_OldEnoughOrElse.py

driving_age = eval(input("Какой минимальный возраст для получения прав в вашей стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
	print("Вы достаточно взрослый для получения прав!")
else:
	if driving_age - your_age > 4:
		print("Извините, вы не сможете водить еще", driving_age - your_age, "лет.")
	if driving_age - your_age == 1:
		print("Извините, вы не сможете водить еще", driving_age - your_age, "год.")
	if driving_age - your_age <= 4 and driving_age - your_age != 1:
		print("Извините, вы не сможете водить еще", driving_age - your_age, "года.")
