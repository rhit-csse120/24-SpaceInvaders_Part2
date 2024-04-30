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
        for k in range(len(self.list_of_missiles) - 1, -1, -1):
            missile = self.list_of_missiles[k]
            if missile.is_off_the_screen or missile.has_exploded:
                del self.list_of_missiles[k]

    def handle_explosions(self, enemies: Enemies):
        for missile in self.list_of_missiles:
            for enemy in enemies.list_of_enemies:
                if enemy.is_hit_by(missile):
                    missile.explode()
                    if not enemy.has_exploded:
                        enemy.explode()
                    break  # Assumes Missile cannot explode more than one Enemy.
        self.remove_dead_missiles()
        enemies.remove_exploded_enemies()
