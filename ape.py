import pygame as pg

pg.init()


WHITE = (255,255,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)


fps_counter = 0

x = 50
y = 50

directionx = 1
directiony = 1

FPS = 120
clock = pg.time.Clock()

screen = pg.display.set_mode((800,600))
bilde = pg.image.load('last ned.png')

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(BLUE)

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= 3
    if keys[pg.K_a]:
        x -= 3
    if keys[pg.K_s]:
        y += 3
    if keys[pg.K_d]:
        x += 3

    fps_counter += 1
    print(fps_counter)

    
    

    if x > 600:
        directionx = -1.5
    if x < 0:
        directionx = +1.5
    if y > 400:
        directiony = -1.5
    if y < 0:
        directiony = +1.5

    screen.blit(bilde, (x, y))
    
    pg.display.update()        