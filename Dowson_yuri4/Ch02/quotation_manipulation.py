# filename quotation_manipulation.py
# Манипулирует с цитатами
# Демонстрирует строковые методы
# Цитата из Томаса Уотсона, который в 1943г. был директором IBM
quote = "Думаю, на мировом рынке можно будет продать штук пять компьютеров."
print("Исходная цитата: ")
print(quote)
print("\nОна же в верхнем регистре: ")
print(quote.upper())
print("\nОна же в нижнем регистре: ")
print(quote.lower())
print("\nКак заголовок: ")
print(quote.title())
print("\nС ма-а-ленькой заменой: ")
print(quote.replace("штук пять", "несколько миллионов"))

#print(quote.swapcase())

#print(quote.capitalize())

print(quote.strip())

print("\nА вот опять исходная цитата")
print(quote)
print("\n\nНажмите Ентер, чтобы выйти.")
