# Author: Frodo.

import pygame
from Enemy import Enemy


class Fighter:
    """ The player can move the Fighter left/right and shoot missiles. """

    def __init__(self):
        self.screen = None
        self.image = None
        self.width = None
        self.height = None

        self.x = None
        self.y = None

        self.speed = None
        self.fire_sound = None
        self.explosion_sound = None
        self.has_exploded = None

        self.missiles = None  # Temporary value

        print("Constructed a Fighter.")  # Temporary

    def draw(self):
        """ Draw (blit) the image of this Fighter. """

    def move_left(self):
        """ Move this Fighter left, unless doing so would go past the edge. """

    def move_right(self):
        """ Move this Fighter right, unless doing so would go past the edge. """

    def fire(self):
        """
        Fires a missile: constructs it (placing it at the top of this Fighter,
        centered horizontally on this Fighter), adds it to the Missiles object
        (per the method in Missiles for doing so), and plays its "fire" sound.
        """

    def is_hit_by(self, enemy: Enemy):
        """ True if this Fighter and the given Enemy overlap. """

    def explode(self):
        """ This Fighter explodes: Play a sound and set has_exploded to True. """


