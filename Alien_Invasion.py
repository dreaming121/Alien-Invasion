import sys

import pygame

from settings import Settings

from ships import Ships

import game_functions as gf

from pygame.sprite import Group


def run_game():
    #初始化屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ships(ai_settings, screen)
    bullets = Group()

    #开始游戏循环
    while True:
        #监视鼠标和键盘
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        #让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
