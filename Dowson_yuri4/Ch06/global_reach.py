# global_reach.py
# Доступ отовсюду
# Демонстрирует работу с глобальными переменными
def read_global():
	print("В области видимости функции read_global() значение value равно", value)

def shadow_global():
	value = -10
	print("В области видимости функции shadow_global() значение value равно", value)

def change_global():
	global value
	value = -10
	print("В области видимости функции change_global() значение value равно", value)

# основная часть
# value - глобальная переменная, потому что сейчас мы находимя в глобальной области видимости
value = 10
print("В глобальной области видимости значение переменной value сейчас стало равным", value, "\n")
input()
read_global()
input()
print("Вернемся в глобальную область видимости. Здесь value по-прежнему равно", value, "\n")
input()
shadow_global()
input()
print("Вернемся в глобальную область видимости. Здесь value по-прежнему равно", value, "\n")
input()
change_global()
input()
print("Вернемся в глобальную область видимости. Значеие value изменилось на", value)

input("\n\nНажмите Enter, чтобы выйти.")


