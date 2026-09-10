import pygame as pg

class NormalTroup(pg.sprite.Sprite):
    def __init__(self, x ,y ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((16,16))
        self.image.fill((15,56,31))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center =  (self.x, self.y)

        self.life = 100
        self.speed = 5

        self.damage = 10

        self.attack = False

    def update(self):
        self.rect.x += self.speed

        if self.life <= 0:
            self.kill()

        self.receive_damage()

    def attack(self):
        self.attack = True

    def receive_damage(self, damage):
        self.life -= damage

    def draw(self, screen):
        screen.blit(self.image, self.rect)