"""
The  Game (model)  file for the Model-View-Controller architecture for our game.
1. It constructs all the objects specific to this game.
2. Its   draw_game   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to draw themselves.
3. Its   run_one_cycle   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to do whatever needs to happen
   independently of events / user-input.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.
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
        # TODO: Implement this method.
