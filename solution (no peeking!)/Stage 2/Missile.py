# Author: Sam.

import pygame


class Missile:
    def __init__(self):
        self.screen = None
        self.x = None
        self.y = None
        self.color = None
        self.width = None
        self.height = None
        self.speed = None
        self.is_off_the_screen = None
        self.has_exploded = None

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
