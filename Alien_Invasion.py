import sys

import pygame

from settings import Settings

from ships import Ships

import game_functions as gf


def run_game():
    #初始化屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ships(ai_settings, screen)

    #开始游戏循环
    while True:
        #监视鼠标和键盘
        gf.check_event(ship)
        ship.update()
        #让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship)


run_game()
