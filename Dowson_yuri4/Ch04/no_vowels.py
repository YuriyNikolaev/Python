# filename no_vowels.py
# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for
message = input("Введите текст: ")
new_message = "" # создается пустая ~ для текста ответного сообщения
VOWELS = "aeiouaеёиоуыэюя" # строка всех гласных
print()
for letter in message:
	if letter.lower() not in VOWELS:
		new_message += letter
		print("создана новая строка: ", new_message)
print("\nВот ваш текст с изъятыми гласными буквами: ", new_message)
input("\nДля выхода нажмите Энтер")