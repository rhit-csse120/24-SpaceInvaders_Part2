# Author: Sam.

import pygame


class Missile:
    def __init__(self, screen: pygame.Surface, x, y, color="red", width=4,
                 height=8, speed=5):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.speed = speed
        self.is_off_the_screen = False
        self.has_exploded = False

    def draw(self):
        """ Draw this Missile as a vertical line. """
        pygame.draw.line(self.screen, self.color,
                         (self.x, self.y),
                         (self.x, self.y + self.height), self.width)

    def move(self):
        """
        Move this Missile up, unless it is off the screen
        (and if so, set is_off_the_screen to True.
        """
        self.y = self.y - self.speed
        if self.y + self.height <= 0:
            self.is_off_the_screen = True

    def explode(self):
        """ This Missile explodes: set has_exploded to True. """
