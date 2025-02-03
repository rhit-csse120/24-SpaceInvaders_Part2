# Author: Pippin.

import pygame
from Missile import Missile


class Enemy:
    def __init__(self):
        self.screen = None
        self.image = None
        self.width = None
        self.height = None
        self.x = None
        self.y = None
        self.h_speed = None
        self.v_speed = None
        self.direction = None
        self.original_x = None
        self.is_off_the_screen = None
        self.has_exploded = None
        self.explosion_sound = None

        print("Constructed an Enemy.")  # Temporary

    def draw(self):
        """ Draw (blit) the image of this Fighter. """

    def move(self):
        """
        Move this Enemy left/right (per its direction) and down as needed.
        """

    def is_hit_by(self, missile: Missile):
        """ True if this Enemy and the given Missile overlap. """

    def explode(self):
        """ This Enemy explodes: Play a sound and set has_exploded to True. """
