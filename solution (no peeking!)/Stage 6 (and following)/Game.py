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

        self.sound_to_play_when_win = pygame.mixer.Sound("../assets/win.wav")
        self.sound_to_play_when_lose = pygame.mixer.Sound("../assets/lose.wav")
        self.game_over_image = pygame.image.load("../assets/gameover.png")
        self.position_for_game_over_image = (170, 200)
        self.game_is_over = False
        self. enemy_fleet_was_destroyed = False

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.fighter.draw()
        self.enemies.draw()
        self.missiles.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        if not self.game_is_over:
            self.missiles.move()
            self.enemies.move()
            self.missiles.handle_explosions(self.enemies)
            self.handle_fighter_is_hit()
            self.handle_enemy_fleet_destroyed()

    def handle_fighter_is_hit(self):
        for enemy in self.enemies.list_of_enemies:
            if self.fighter.is_hit_by(enemy):
                self.fighter.explode()
                print("Player loses!")
                self.game_is_over = True
                self.sound_to_play_when_lose.play()
                return

    def handle_enemy_fleet_destroyed(self):
        if self.enemy_fleet_was_destroyed:
            self.enemy_fleet_was_destroyed = False
            channel = self.sound_to_play_when_win.play()
            self.game_is_over = True
        elif len(self.enemies.list_of_enemies) == 0:
            # Just set a flag for the next iteration of run_one_cycle,
            # so that any events not yet processed can be processed.
            self.enemy_fleet_was_destroyed = True


    def start_a_new_game(self, enemy_rows=5):
        # To be implemented later.
        pass