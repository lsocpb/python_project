import pygame as pg

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # initializing the game
    pg.init()

    # Screen param
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
    pg.display.set_caption("Invasion")

    # Ship param
    ship = Ship(ai_settings, screen)

    # Bullets param
    bullets = Group()

    # Running the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
