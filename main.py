import pygame as pg
from sprites import *

pg.init()

WHITE = (255,255,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_GRAY = (211,211,211)
DARKBLUE = (25, 25, 112)

spawn = 0

all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()

hero = Player()
all_sprites.add(hero)

enemy = Enemy()
enemy2 = Enemy2()
enemy_group.add(enemy, enemy2)


FPS = 120
clock = pg.time.Clock()




screen = pg.display.set_mode((800,800))


playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(DARKBLUE)



    all_sprites.update()
    all_sprites.draw(screen)

    hits = pg.sprite.spritecollide(hero, enemy_group,dokill=True)
    if hits:
        for hit in hits:
            spawn += 1
            print (spawn)


    #lag nye fiender
    if len(enemy_group) < 50009:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_group.add(enemy)

 



  


    
    pg.display.update()    