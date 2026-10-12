import pygame as pg

class LifeBar(pg.sprite.Sprite):
    def __init__(self, owner, width = 50, height = 5):
        pg.sprite.Sprite.__init__(self)

        ## Var from the father 
        self.owner = owner
        self.width = width
        self.height = height

        # position
        self.x = self.owner.rect.centerx - self.width // 2
        self.y = self.owner.rect.top - 10


        self.image = pg.Surface((width, height))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        
    def update(self):
        x = self.owner.rect.centerx - self.width // 2
        y = self.owner.rect.top - 10

        self.rect.x = x
        self.rect.y = y

        life = max(0, min(self.owner.life, self.owner.max_life))
        health_width = int((self.width * life) / self.owner.max_life)
        print(health_width)

        position_actual = self.rect.topleft

        if health_width >= 0:
            self.image = pg.transform.scale(self.image, (health_width, self.height))
            self.rect = self.image.get_rect(topleft=position_actual)
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)