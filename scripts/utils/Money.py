import pygame as pg

class Money(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((20,20))
        self.image.fill((255,255,0))
        self.x = 1150
        self.y = 40
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)