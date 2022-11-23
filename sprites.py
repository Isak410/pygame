import pygame as pg
from random import randint
vec = pg.math.Vector2


player_img = pg.image.load("kar.PNG")
player_img = pg.transform.scale(player_img, (150,150))
player_img1 = pg.image.load("tt.png")
player_img1 = pg.transform.scale(player_img1, (100,200))

enemy_img = pg.image.load("enemy.PNG")
enemy_img = pg.transform.scale(enemy_img, (150,150))
enemy_img1 = pg.image.load("test1.jpg")
enemy_img1 = pg.transform.scale(enemy_img1, (200,200))

enemy2_img = pg.image.load("goofy.jpg")
enemy2_img = pg.transform.scale(enemy_img, (150,150))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()     #hitbox
        self.pos = vec(250,250)
        self.rect.center = self.pos
        self.speed = 3
        self.life = 100

    def update(self):
        self.rect.center = self.pos # holder rect på player hver frame

        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            self.image = player_img1
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

        
class Enemy(pg.sprite.Sprite):
    def __init__(self1):
        pg.sprite.Sprite.__init__(self1)
        self1.image = enemy_img
        self1.rect = self1.image.get_rect()     #hitbox
        self1.pos = vec(1700,randint(0,600))
        self1.rect.center = self1.pos
        self1.speed = 3
    
        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            self1.image = enemy_img1

    def update(self):
        self.rect.center = self.pos # holder rect på player hver frame
        self.pos.x -= 4

        if self.pos.x < -125:
            self.pos.x = 1700
            self.pos.y = randint(100,800)

class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()     #hitbox
        self.pos = vec(randint(0,800), -100)
        self.rect.center = self.pos
        self.speed = 3

    def update(self):
        self.rect.center = self.pos # holder rect på player hver frame
        self.pos.y += 4

        if self.pos.y < 900:
            self.pos.y = -125
            self.pos.x = randint(100,700)


        
        
        
        



