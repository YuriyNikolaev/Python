# Ch_05DZ01.py
# программа должна выводить слова из списка в случайном порядке

import random

words = ["собака", "сова", "слух", "уху", "ежик", "собака", "ухо", "сова"]
used = []

for word in words:
	#print(word)
	word = random.choice(words)
	if word not in used:
		print(word)
	used.append(word)
print("\nКоличество слов в списке: ", len(words))
#print(used)
#print("\nКоличество повторов: ", len(used))

input("\n\nНажмите Enter, чтобы выйти.")