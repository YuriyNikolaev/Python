# ссылка https://python-scripts.com/creating-game-in-30-minutes#install-pygame-zero

import pgzrun  # может быть предупреждение, но код работает
import random
import math

TITLE = "Arkanoid Clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblu.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

bar = Actor("element_blue_rectangle_glossy.png")
bar.x = 120
bar.y = 100

bars_list = []


def draw():
    screen.blit("background.png", (0, 0))
    bar.draw()
    paddle.draw()
    ball.draw()
    place_blue_bars()

def place_blue_bars():
    bar_x = 120
    bar_y = 100
    for i in range(8):
        bar = Actor("element_blue_rectangle_glossy.png")
        bar.x = bar_x
        bar.y = bar_y
        bar.draw()

        bar_x += 70

def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)



def update():
    pass


coloured_box_list = ["element_blue_rectangle_glossy.png", 
                    "element_green_rectangle_glossy.png", 
                    "element_red_rectangle_glossy.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()
