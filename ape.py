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

screen = pg.display.set_mode((1600,1200))
bilde = pg.image.load('last ned.png')

playing = True
while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(BLUE)

    fps_counter += 1
    print(fps_counter)

    #move box
    x += directionx
    y += directiony
    

    if x > 1400:
        directionx = -3
    if x < 0:
        directionx = +3
    if y > 1000:
        directiony = -3
    if y < 0:
        directiony = +3

    screen.blit(bilde, (x, y))
    
    pg.display.update()        