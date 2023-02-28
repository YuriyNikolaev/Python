# ссылка https://python-scripts.com/creating-game-in-30-minutes#install-pygame-zero

import pgzrun  # может быть предупреждение, но код работает
import random
import math

TITLE = "Arkanoid Clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

bar = Actor("element_blue_rectangle_glossy.png")
bar.x = 120
bar.y = 100


def draw():
    screen.blit("background.png", (0, 0))
    bar.draw()
    paddle.draw()
    ball.draw()
    bar_x = 120
    bar_y = 100
    for i in range(8):
        bar = Actor("element_blue_rectangle_glossy.png")
        bar.x = bar_x
        bar.y = bar_y
        bar.draw()

        bar_x += 70


def update():
    pass


pgzrun.go()
