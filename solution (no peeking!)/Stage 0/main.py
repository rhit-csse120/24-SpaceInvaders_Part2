"""
The  main  file for the Model-View-Controller (MVC) architecture for our game.
It:
   1. Initializes pygame, the screen and a Clock (for the frame rate).
   2. Constructs a Game (model), View and Controller.
   3. Runs the game loop, which repeatedly (per the frame rate):
      -- Asks the Controller object to get and respond to events.
      -- Asks the Game object to run one cycle.
      -- Asks the View object to draw everything.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

import pygame
from Game import Game
from Controller import Controller
from View import View


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))  # TODO: Choose your own size
    pygame.display.set_caption("My Game Name")  # TODO: Choose your own title
    clock = pygame.time.Clock()
    frame_rate = 60  # TODO: Choose your own frame rate

    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    while True:
        clock.tick(frame_rate)

        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()


main()
