# filename read_it.py
# Прочитаем
# Демонстрирует чтение из текстового файла
t = '/home/yurich/Desktop/Python/Доусон/Ch07/read_it1.txt'
print("Открываю и закрываю файл.")
input("нажмите")
text_file = open(t, "r", encoding='utf-8')
text_file.close()

input("нажмите")

print("\nЧитаю файл посимвольно.")
input("нажмите")
text_file = open(t, "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

input("нажмите")

print("\nЧитаю файл целиком.")
input("нажмите")
text_file = open(t, "r", encoding='utf-8')
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

input("нажмите")

print("\nЧитаю одну строку посимвольно.")
input("нажмите")
text_file = open(t, "r", encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

input("нажмите")

print("\nЧитаю одну строку целиком.")
input("нажмите")
text_file = open(t, "r", encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

input("нажмите")

print("\nЧитаю весь файл в список.")
input("нажмите")
text_file = open(t, "r", encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
	print(line)
text_file.close()

input("нажмите")

print("\nПеребираю файл построчно.")
input("нажмите")
text_file = open(t, "r", encoding='utf-8')
for line in text_file:
	print(line)
text_file.close()

input("нажмите")

input("\n\nНажмите Enter, чтобы выйти.")




