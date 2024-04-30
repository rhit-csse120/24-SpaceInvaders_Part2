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
        self.missiles = Missiles(screen)
        self.fighter = Fighter(screen, self.missiles)
        self.enemies = Enemies(screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.fighter.draw()
        self.enemies.draw()
        self.missiles.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        self.missiles.move()
        self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)
