# dz_103_2.py
# Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал
# орел, а сколько - решка.

import random

reshka = 0
orel = 0

for i in range(100):
	coin = random.randrange(0,2)
	if coin == 1:
		reshka += 1 
	else:
		orel += 1
	#print("решка =", reshka)
	#print("орел = ", orel)


print("Решка выпала ", reshka, "раз.")
print("Орел выпал  ", orel, "раз.")
