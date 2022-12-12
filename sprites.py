import pygame as pg
from random import randint
vec = pg.math.Vector2


player_img = pg.image.load("kar.PNG")
player_img = pg.transform.scale(player_img, (80,80))

enemy_img = pg.image.load("enemy.PNG")
enemy_img = pg.transform.scale(enemy_img, (70,70))

cake_img = pg.image.load("cake_img.png")
cake_img = pg.transform.scale(cake_img, (50, 50))


player_left_img = pg.transform.flip(player_img, True, False)

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()     #hitbox
        self.pos = vec(250,250)
        self.rect.center = self.pos
        self.speed = 3
        self.life = 100
        self.game = game
        self.image = player_img
        self.image_left = player_left_img
        self.image_right = player_img
  

    def update(self):
        self.rect.center = self.pos # holder rect på player hver frame

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = self.image_right
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = self.image_left
        if keys[pg.K_LSHIFT]:
            self.speed = 5
        else:
            self.speed = 3

        
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()     #hitbox
        self.pos = vec(1700,randint(0,600))
        self.rect.center = self.pos
        self.speed = 3
        self.enemyhealth = 100

        if self.enemyhealth <= 0:
            print("nokka")
            
    

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
        self.pos = vec(1700,randint(0,600))
        self.rect.center = self.pos
        self.speed = 3
        self.enemyhealth = 100

        if self.enemyhealth <= 0:
            print("nokka")

    def update(self):
        self.rect.center = self.pos # holder rect på player hver frame
        self.pos.y += 4

        if self.pos.y < 900:
            self.pos.y = -125
            self.pos.x = randint(100,700)

class Food(pg.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.all_sprites, game.food_group # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = cake_img
        self.rect = self.image.get_rect()
        self.pos = vec(1600, randint(0,800)) # start posisjon
        self.rect.center = self.pos

    def update(self):
        self.rect.center = self.pos
        self.pos.x -= 6

        if self.pos.x < 1:
            self.pos.x = 1900
            self.pos.y = randint(0,800)
    

    #def give_health(self):
        #self.game.hero.max_health += 10
        #self.game.hero.health = self.game.hero.max_health


        
        
        
        



