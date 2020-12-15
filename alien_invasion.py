import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # 初始化背景设置
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景颜色
    bg_color = (230, 230, 230)

    # 创建一艘飞船、一个子弹和一个外星人编组
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的数组
    bullets = Group()
    aliens = Group()

    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
