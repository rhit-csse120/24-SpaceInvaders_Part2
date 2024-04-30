# Authors: Frodo, Pippin and Sam.

import pygame
from Fighter import Fighter
from Enemy import Enemy
from Missile import Missile
from Enemies import Enemies
from Missiles import Missiles


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.fighter = Fighter(screen)
        self.enemies = Enemies()
        self.missiles = Missiles()
        self.enemy = Enemy(screen)  # For testing
        self.missile = Missile(screen, 100, 300)  # For testing

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.fighter.draw()
        self.enemy.draw()
        self.missile.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # TODO: Use something like this, but for the objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)
