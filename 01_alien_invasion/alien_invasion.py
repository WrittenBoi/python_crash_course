#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # init game
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode(
        (cfg.screen_width, cfg.screen_height))
    ship = Ship(screen, cfg)
    pygame.display.set_caption(cfg.game_title)

    # game main loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(cfg, screen, ship)


if __name__ == "__main__":
    run_game()
