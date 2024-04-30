# Author: Sam.

import pygame
from Missile import Missile
from Enemies import Enemies


class Missiles:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.list_of_missiles: list[Missile] = []

    def add_missile(self, missile: Missile):
        self.list_of_missiles.append(missile)

    def draw(self):
        for missile in self.list_of_missiles:
            missile.draw()

    def move(self):
        for missile in self.list_of_missiles:
            missile.move()

    def remove_dead_missiles(self):
        pass

    def handle_explosions(self, enemies: Enemies):
        pass


