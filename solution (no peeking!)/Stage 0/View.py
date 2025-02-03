"""
The  View  file for the Model-View-Controller architecture for our game.
Its   draw_everything   method is called repeatedly by the main game loop.
At each call, it displays a view of the game,
typically by asking the various objects of the Game to draw themselves.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

import pygame
from Game import Game


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background_color = pygame.Color("black")  # TODO: Choose own color

    def draw_everything(self):
        self.screen.fill(self.background_color)
        self.game.draw_game()
        pygame.display.update()
