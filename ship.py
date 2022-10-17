import pygame as pg
from pygame import rect


class Ship:

    def __init__(self, ai_settings, screen):
        # Screen appearing
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading the ship
        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Centralizing the ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = self.rect.centerx


        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship place on screen"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Method that shows ship on screen"""
        self.screen.blit(self.image, self.rect)
