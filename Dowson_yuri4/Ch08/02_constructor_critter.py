# filename constructor_critter.py
# Зверюшка с конструктором
# Демонстрирует метод-конструктор
class Critter(object):
	"""Виртуальный питомец"""
	def __init__(self): # при появлении (инициализации) объекта, будет печататься текст из print
		print("Появилась на свет новая зверюшка!")
	def talk(self):
		print("\nПривет. Я зверюшка - экземпляр класса Critter.")
# основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input("\n\nНажмите Enter, чтобы выйти.")
