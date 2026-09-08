import pygame as pg 
from scripts.screens.Screen import Screen

# Towers
from scripts.towers.Tower import Tower

#utils
from scripts.utils.Money import Money

class GameScreen(Screen):

    def __init__(self, game):
        super().__init__(game)

        # Towers creation
        self.ally_tower = Tower(60, 400)
        self.enemy_tower = Tower(1140, 400)

        # Utils
        self.money = Money()

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

        self.money.draw(screen)

