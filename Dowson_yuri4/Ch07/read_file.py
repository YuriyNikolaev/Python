# filename read_file.py
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