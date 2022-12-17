# Filename 29_OldEnough_dop.py

driving_age = eval(input("Каков минимаьный возраст для получения прав в вашей стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
    print("Вы достаточно взрослый для получения прав!")
if your_age < driving_age:
    if driving_age - your_age > 4:
        print("Извините, вы не сможете водить еще", driving_age-your_age, "лет.")
    if driving_age - your_age == 1:
        print("Извините, вы не сможете водить еще", driving_age - your_age, "год.")
    if driving_age - your_age != 1 and driving_age - your_age <= 4:
        print("Извините, вы не сможете водить еще", driving_age - your_age, "года.")