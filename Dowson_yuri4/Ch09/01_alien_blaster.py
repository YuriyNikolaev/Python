# filename 01_alien_blaster.ру
# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Player(object):
	"""Игрок в экшн-игре"""
	def blast(self, enemy):
		print("Игрок стреляет во врага. \n")
		enemy.die()

class Alien(object):
	"""Враждебный пришелец-инопланетянин в экшн-игре"""
	def die(self):
		print("Тяжело дыша пришелец произносит: 'Ну вот и все. Спета моя песенка. \n'"\
			"Уже в глазах темнее... Передай полутора миллионам моих личинок, что я любил их \n"\
			"Прощай, безжалостный мир.")

# основная часть программы
print("\t\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
input("\n\nНажмите Enter, чтобы выйти.")

	
		
	
		
