import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rain_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings

        # Load the raindrop image and set its rect attribute
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()

        #Start each raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the raindrop`s exact horizontal and vertical positions.
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """Shift raindrops one level below"""
        self.y += self.settings.rain_speed
        self.rect.y = self.y
        if self.rect.top >= self.screen.get_rect().bottom:
            self.y -= self.settings.screen_height 