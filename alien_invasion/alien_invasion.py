import pygame

from settings import Settings
from ship import Ship
from button import Button
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard

import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)

    aliens = Group()

    bullets = Group()

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
