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

        print("Constructed a Missile.")  # Temporary

    def draw(self):
        """ Draw this Missile as a vertical line. """

    def move(self):
        """
        Move this Missile up, unless it is off the screen
        (and if so, set is_off_the_screen to True.
        """

    def explode(self):
        """ This Missile explodes: set has_exploded to True. """
