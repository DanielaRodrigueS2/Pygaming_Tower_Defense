import pygame as pg
from scripts.utils.LifeBar import LifeBar

class Tower(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((50,100))
        self.image.fill((255,0,255))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y) 
        self.money = 0
        self.life = 500
        self.lifeBar = LifeBar(70, self.x, self.y - 70, self.life)

    def update(self):
        self.lifeBar.update(self.x, self.life)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.lifeBar.draw(screen)

    def gain_money(self, money):
        self.money += money