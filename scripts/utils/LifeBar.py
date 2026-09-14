import pygame as pg

class LifeBar(pg.sprite.Sprite):
    def __init__(self, size, x , y, life):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((size, 10))
        self.image.fill = (0, 255, 0)
        self.life = life
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, x, life):
        self.image = pg.Surface((life, 10))
        self.image.fill = (0, 255, 0)
        self.rect = self.image.get_rect()
        self.rect.center(x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)