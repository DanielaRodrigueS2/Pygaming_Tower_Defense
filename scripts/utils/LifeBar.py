import pygame as pg

class LifeBar(pg.sprite.Sprite):
    def __init__(self, size, x , y, max_life):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pg.Surface((self.size, 10))
        self.image.fill((0, 255, 0))
        self.max_life = max_life
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, x, life):
        life = max(0, min(life, self.max_life))
        width =int((self.size * life) / self.max_life)
        self.image = pg.Surface((width, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)