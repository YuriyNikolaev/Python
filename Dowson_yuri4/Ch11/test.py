# filename test.py
# Ничего себе результат!
# Демонстрирует отображение текста на графическом экране
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image, 
					x = 100, 
					y = 100,
					dx = 1,
					dy = 1)
games.screen.add(pizza)


score = games.Text(value = 1756521,
					size = 60, 
					color = color.blue,
					x = 550,
					y = 30)
games.screen.add(score)

won_message = games.Message(value = "Победа!",
							size = 100,
							color = color.red,
							x = games.screen.width/2,
							y = games.screen.height/2,
							lifetime = 250,
							after_death = games.screen.quit
							)

games.screen.add(won_message)

games.screen.mainloop()