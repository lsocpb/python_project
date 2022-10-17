import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to bullet management"""

    def __init__(self, ai_settings, screen, ship):

        super(Bullet, ship).__init__()
        self.screen = screen
