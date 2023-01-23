# 2_2-6.py
# является ли введенная строка палиндромом

# s = input("Введите строку")
# s = "какая-то строка"
s = "Аргентина манит негра"
revers_s = ""

for i in range(len(s), 0, -1):
    revers_s += s[i - 1]

if s == revers_s:
    print("Polindrome")
else:
    print("Not Polindrome")

    