# filename heros_inventory.py
# Арсенал героя
# Демонстрирует создание кортежа
# создадим пустой кортэж
inventory = ()
# рассмотрим его как условие
if not inventory:
	print("Вы безоружны.")
input("\nНажмите Enter, чтобы продолжить.")
# теперь создадим кортеж с несколькими элементами
inventory = ("меч", 
			 "кольчуга",
			 "щит",
			 "целебное снадобье")
# выведем этот кортэж на экран
print("\nСодержимое кортежа: ")
print(inventory)
# выведем все элементы последовательно
print("\nИтак в вашем арсенале: ")
for item in inventory:
	print(item)
input("\nДля выхода нажмите Энтер")