import pygame as pg
from sprites import *

class Game():
    def __init__(self): #kjører når vi starter spillet
        pg.init()
        self.WHITE = (255,255,255)
        self.CYAN = (0,255,255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.LIGHT_GRAY = (211,211,211)
        self.DARKBLUE = (25, 25, 112)
        self.i = 0
        self.WIDTH = 1600
        self.HEIGTH = 800
        
        self.screen = pg.display.set_mode((1600,800))
        self.bg = pg.image.load("Space Background.png").convert_alpha()
      
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 60)

        self.FPS = 120
        self.clock = pg.time.Clock()

        self.spawn = 0

        self.new()


    def new(self): #ny runde
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.hero = Player()
        self.all_sprites.add(self.hero)

        self.i = 0
        self.enemy = Enemy()
        self.enemy2 = Enemy2()
        self.enemy_group.add(self.enemy, self.enemy2)
        self.tekst = pg.font.SysFont("Comic Sans MS", 30)

        self.run()


    def run(self): #game loop
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
    
            self.screen.blit(self.bg, (self.i,0)) # tegner bakgrunn
            self.screen.blit(self.bg,(self.WIDTH+self.i,0))
            if (self.i <= -self.WIDTH):
                self.screen.blit(self.bg,(self.WIDTH+self.i,0))
                self.i=0
            self.i -= 3
            

            text_hp = self.comic_sans30.render(str(self.hero.life), False, (self.CYAN))
    




            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            hits = pg.sprite.spritecollide(self.hero, self.enemy_group,dokill=False)
            if hits:
                for hit in hits:
                    self.spawn += 1
                hits[0].enemyhealth -= 10
            
            
            if hits:
                self.hero.life -=10
                print (self.hero.life)
                if self.hero.life <= 0:
                    playing = False



            #lag nye fiender
            if len(self.enemy_group) < 8:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemy_group.add(enemy)
            self.screen.blit(text_hp, (10,10))

      
    
            pg.display.update()    


g = Game()