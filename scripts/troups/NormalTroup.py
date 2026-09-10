import pygame as pg

class NormalTroup(pg.sprite.Sprite):
    def __init__(self, x ,y ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15,15))
        self.image.fill((15,56,31))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center =  (self.x, self.y)

        self.life = 100
        self.speed = 5

    def update(self, event, tower_x):
        if self.rect.x < tower_x:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)