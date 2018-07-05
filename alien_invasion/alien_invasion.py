import sys

import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    aliens = Group()

    bullets = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
