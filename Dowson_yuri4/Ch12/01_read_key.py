# filename 01_read_key.py
# Читаю с клавиатуры
# Демонстрирует чтение с клавиатурного ввода
from livewires import games
games.init(screen_width = 640, screen_height = 480, fps =50) # инициализация экрана

class Ship(games.Sprite):
	""" Подвижный космический корабль. """
	def update(self):
		""" Перемещает корабль определенным образом, 
		исходя из нажатых клавиш. """
		if games.keyboard.is_pressed(games.K_w):
			self.y -= 1
		if games.keyboard.is_pressed(games.K_s):
			self.y += 1
		if games.keyboard.is_pressed(games.K_a):
			self.x -= 1
		if games.keyboard.is_pressed(games.K_d):
			self.x += 1

def main():
	nebula_image = games.load_image("nebula.jpg", transparent = False) # загружаем фоновое изображение
	games.screen.background = nebula_image # ставим загруженное изображение фоном

	ship_image = games.load_image("ship.bmp") # загружаем картинку корабля
	the_ship = Ship(image = ship_image,       
					x = games.screen.width/2,
					y = games.screen.height/2)  # создаем объект корабль
	games.screen.add(the_ship) # добавляем объект корабль на экран

	games.screen.mainloop() # запускаем игровой цикл

main()