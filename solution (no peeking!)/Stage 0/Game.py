# TODO: Authors: Put your names here (entire team)

import pygame


# TODO: Put each class in its own file (module),
#  using the same name for the file and the class.
#  Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # TODO: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # TODO: Use something like this, but for the objects in YOUR game:
        #     self.fighter.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # TODO: Use something like this, but for the objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)
