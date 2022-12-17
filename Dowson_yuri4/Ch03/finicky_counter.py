# filename finicky_counter.py
# Привередливая считалка
# Демонстрирует работу команды break и continue
count = 0
while True:
	count += 1
	# завершщить цикл, если count принимате значение больше 10
	if count > 10:
		break
	# пропустить 5
	if count == 5:
		continue # возвращается в начало цикла, при выпадении цифры 5
	print(count)
	
input("\nНажмите Энтер, чтобы выйти.")