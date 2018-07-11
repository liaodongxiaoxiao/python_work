import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """键按下事件监听"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    """键抬起事件监听"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """响应按键和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """监测开始按钮点击事件"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏状态
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人和子弹列表
        bullets.empty()
        aliens.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collistions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collistions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        # 加速
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船相撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘，采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()

    aliens.draw(screen)

    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以显示多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """飞船被撞击"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        # 飞船撞击游戏结束，光标可见
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """检查外星人是否到屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break
