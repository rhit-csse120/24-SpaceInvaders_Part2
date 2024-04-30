# Author: Frodo.

import pygame
from Enemy import Enemy


class Fighter:
    """ The player can move the Fighter left/right and shoot missiles. """

    def __init__(self, screen: pygame.Surface, speed=5):
        self.screen = screen
        self.image = pygame.image.load("../assets/fighter.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Fighter starts centered horizontally, near the bottom of screen.
        image_at_bottom = self.screen.get_height() - self.height
        distance_from_bottom = 5
        self.x = (self.screen.get_width() - self.width) // 2
        self.y = image_at_bottom - distance_from_bottom

        self.speed = speed
        self.fire_sound = pygame.mixer.Sound("../assets/pew.wav")
        self.explosion_sound = pygame.mixer.Sound("../assets/explosion.wav")
        self.has_exploded = False

        self.missiles = None  # Temporary value

    def draw(self):
        """ Draw (blit) the image of this Fighter. """
        self.screen.blit(self.image, (self.x, self.y))

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


