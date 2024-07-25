# Authors: Frodo, Pippin and Sam.

import pygame
from Game import Game
from Controller import Controller
from View import View


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    frame_rate = 60

    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    while True:
        clock.tick(frame_rate)

        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()


main()
