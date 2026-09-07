import pygame as pg

class Tower(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((50,100))
        self.image.fill((255,0,255))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y) 

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)