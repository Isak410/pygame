import pygame as pg

pg.init()

WHITE = (255,255,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_GRAY = (211,211,211)

player_img = pg.image.load("kar.PNG")
player_img = pg.transform.scale(player_img, (250,250))

x = 50
y = 50

directionx = 1
directiony = 1

FPS = 120
clock = pg.time.Clock()

speed = 5

screen = pg.display.set_mode((800,800))


playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(WHITE)

#move keys
    keys = pg.key.get_pressed()
    

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_a]:
        x -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_d]:
        x += speed



    
    
    if x > 650:
        x = 650
    if x < -80:
        x = -80
    if y > 593:
        y = 593
    if y < -75:
        y = -75

    screen.blit(player_img, (x, y))
    
    pg.display.update()    