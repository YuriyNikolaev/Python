# 02_rotate_sprite.py
# Крутящийся спрайт
# Демонстрирует вращени спрайта
from livewires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ship(games.Sprite):
	""" Вращающийся космический корабль. """
	def update(self):
		""" Вращает корабль определенным образом,
		исходя из нажатых клавиш."""
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += 1
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= 1
		if games.keyboard.is_pressed(games.K_1):
			self.angle = 0
		if games.keyboard.is_pressed(games.K_2):
			self.angle = 90
		if games.keyboard.is_pressed(games.K_3):
			self.angle = 180
		if games.keyboard.is_pressed(games.K_4):
			self.angle = 270

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
