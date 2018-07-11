import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类"""

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        """初始化飞船，并设置初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图片，及捕获其外接矩形

        self.image = pygame.image.load_basic('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.moving_right = False
        self.moving_left = False

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 向右移动飞船
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕中间"""
        self.center = self.screen_rect.centerx
