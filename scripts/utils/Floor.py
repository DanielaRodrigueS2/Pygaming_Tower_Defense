import pygame as pg

class Floor(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1200, 50))
        self.image.fill((0,0,0))
        self.x = 600
        self.y = 475
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)