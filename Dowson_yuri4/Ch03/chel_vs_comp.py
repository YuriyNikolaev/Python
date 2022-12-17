# filename chel_vs_comp.py
import random
a = 1
b = 100

while True:
    number = random.randrange(a, b)
    print("Я думаю это ", number)
    otvet = input("это загаданное число? ")
    
    if otvet == "д":
        print("Я угадал!")
        break
    else:
        print("Угадываю дальше.")
        #continue
    # число больше?
    more = input("Число больше?  ")
    if more == "д":
        a = number
    # число меньше?
    else:
        b = number
        print("Значит оно меньше!")