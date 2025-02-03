# Author: Pippin.

import pygame
from Missile import Missile


class Enemy:
    def __init__(self, screen: pygame.Surface, x=100, y=50):
        self.screen = screen
        self.image = pygame.image.load("../media/badguy.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.h_speed = None  # Increase speeds to make the game harder.
        self.v_speed = None
        self.direction = None
        self.original_x = None
        self.is_off_the_screen = None
        self.has_exploded = None
        self.explosion_sound = None

    def draw(self):
        """ Draw (blit) the image of this Fighter. """
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        """
        Move this Enemy left/right (per its direction) and down as needed.
        """

    def is_hit_by(self, missile: Missile):
        """ True if this Enemy and the given Missile overlap. """

    def explode(self):
        """ This Enemy explodes: Play a sound and set has_exploded to True. """
