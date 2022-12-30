# filename ch2_orel_reshka.py
import random

brosok = 0
orel = 0
reshka = 0

while brosok != 100:
	monetka = random.randint(0,1)
	if monetka == 0:
		orel += 1
	else:
		reshka += 1
	brosok += 1

print("Бросков всего: ", brosok)
