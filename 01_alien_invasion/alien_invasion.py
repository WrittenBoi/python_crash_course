#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # init game
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode(
        (cfg.screen_width, cfg.screen_height))
    ship = Ship(screen, cfg)
    bullets = Group()
    pygame.display.set_caption(cfg.game_title)

    # game main loop
    while True:
        try:
            gf.check_events(cfg, screen, ship, bullets)
        except:
            return
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(cfg, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
