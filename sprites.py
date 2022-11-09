import pygame as pg
vec = pg.math.Vector2


player_img = pg.image.load("kar.PNG")
player_img = pg.transform.scale(player_img, (250,250))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()     #hitbox
        self.pos = vec(250,250)
        self.rect.center = self.pos
        self.speed = 3


    def update(self):
        self.rect.center = self.pos # holder rect på player hver frame
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_LSHIFT]:
            self.speed = 5
        else:
            self.speed = 3
            

        

        if self.pos.x > 770:
            self.pos.x = 770
        if self.pos.x < 45:
            self.pos.x = 45
        if self.pos.y > 717:
            self.pos.y = 717
        if self.pos.y < 45:
            self.pos.y = 45



