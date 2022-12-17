# Filename 29_OldEnough.py

driving_age = eval(input("Каков минимаьный возраст для получения прав в вашей стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
    print("Вы достаточно взрослый для получения прав!")
if your_age < driving_age:
    print("Извините, вы не сможете водить еще", driving_age-your_age, "лет.")