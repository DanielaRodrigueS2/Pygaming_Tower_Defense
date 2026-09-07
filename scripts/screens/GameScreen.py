import pygame as pg 
from scripts.screens.Screen import Screen

from scripts.towers.Tower import Tower

class GameScreen(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.ally_tower = Tower(60, 400)
        self.enemy_tower = Tower(1140, 400)

    def update(self):
        pass

    def handle_events(self, event):
        pass

    def check_collisions(self):
        pass

    def draw(self, screen):

        screen.fill((50,100,100))

        self.ally_tower.draw(screen)
        self.enemy_tower.draw(screen)

