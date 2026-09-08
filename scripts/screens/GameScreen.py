import pygame as pg 
from scripts.screens.Screen import Screen

# Towers
from scripts.towers.Tower import Tower

#utils
from scripts.utils.Money import Money
from scripts.utils.Floor import Floor

class GameScreen(Screen):

    GAIN_MONEY_ALLY = pg.USEREVENT + 1
    GAIN_MONEY_ENEMY = pg.USEREVENT + 2

    def __init__(self, game):
        super().__init__(game)

        # Events timer
        pg.time.set_timer(self.GAIN_MONEY_ALLY, 2000)
        pg.time.set_timer(self.GAIN_MONEY_ENEMY, 2000)

        # Font
        self.font = pg.font.SysFont('Comic Sans MS', 32)

        # Towers creation
        self.ally_tower = Tower(60, 400)
        self.enemy_tower = Tower(1140, 400)

        # Utils
        self.money = Money()
        self.floor = Floor()

    def update(self):
        pass

    def handle_events(self, event):

        if event.type == self.GAIN_MONEY_ALLY:
            self.ally_tower.gain_money(10)

        if event.type == self.GAIN_MONEY_ENEMY:
            self.enemy_tower.gain_money(10)

    def check_collisions(self):
        pass

    def draw(self, screen):

        screen.fill((50,100,100))

        # Towes
        self.ally_tower.draw(screen)
        self.enemy_tower.draw(screen)

        # Utils
        self.money.draw(screen)
        self.floor.draw(screen)

        # Font
        money_text = self.font.render(f'{self.ally_tower.money}', True, (255,255,255))
        money_rect = money_text.get_rect(midright=(self.money.rect.left - 10, self.money.rect.centery))
        screen.blit(money_text, money_rect)

