import pygame as pg

class CreateTroup(pg.sprite.Sprite):

    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((100,100))
        self.image.fill(color)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)