import pygame as pg
from sprites import *

pg.init()

WHITE = (255,255,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_GRAY = (211,211,211)

all_sprites = pg.sprite.Group()

hero = Player()
all_sprites.add(hero)

enemy = Enemy()
all_sprites.add(enemy)


FPS = 120
clock = pg.time.Clock()




screen = pg.display.set_mode((800,800))


playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(CYAN)



    all_sprites.update()

    all_sprites.draw(screen)


    
    pg.display.update()    