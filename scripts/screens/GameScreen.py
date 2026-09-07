import pygame as pg 
from scripts.screens.Screen import Screen

class GameScreen(Screen):

    def __init__(self, game):
        super().__init__(game)

    def update(self):
        pass

    def handle_events(self, event):
        pass

    def check_collisions(self):
        pass

    def draw(self, screen):

        screen.fill((50,100,100))

        