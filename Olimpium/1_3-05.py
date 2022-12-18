# num = 12441
num = int(input("Введите сумму: "))

thousands = num // 1000
hundreds = (num - thousands * 1000) // 100
dozen = (num - thousands * 1000 - hundreds * 100) // 10
one = (num - thousands * 1000 - hundreds * 100 - dozen * 10)

print(one, " - по 1 руб")
print(dozen, " - по 10 руб")
print(hundreds,  " - по 100 руб")
print(thousands,  " - по 1000 руб")