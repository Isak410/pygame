import pygame as pg
from sprites import *

pg.mixer.init()
pg.mixer.music.load('sangmain.mp3') 

pg.mixer.music.play(-1) 

dead_screen = pg.image.load("dead_screen.jpg")
dead_screen = pg.transform.scale(dead_screen, (500,500))

            
    

class Game():
    def __init__(self): #kjører når vi starter spillet
        pg.init()
        
        self.WHITE = (255,255,255)
        self.CYAN = (0,255,255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.LIGHT_GRAY = (200,196,196)
        self.DARKBLUE = (25, 25, 112)
        self.BLUE = (0, 0, 255)
        self.i = 0
        self.WIDTH = 1600
        self.HEIGTH = 800

        pg.display.set_caption('ok')

        

        foodY = 5
        
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
        self.enemy_group2 = pg.sprite.Group()
        self.food_group = pg.sprite.Group()

        self.hero = Player(self)
        self.all_sprites.add(self.hero)

        self.food = Food(self)
        
        self.enspawn = 1
        self.tospawn = 1
        self.trespawn = 1
        
        self.i = 0
        self.enemy = Enemy()
        self.enemy2 = Enemy2()
        self.enemy_group.add(self.enemy)
        self.tekst = pg.font.SysFont("Comic Sans MS", 30)

        self.stop = False

        self.startscreen()

    def new1(self): #ny runde
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.enemy_group2 = pg.sprite.Group()
        self.food_group = pg.sprite.Group()

        self.hero = Player(self)
        self.all_sprites.add(self.hero)

        self.food = Food(self)
        
        self.i = 0
        self.enemy = Enemy()
        self.enemy2 = Enemy2()
        self.enemy_group.add(self.enemy)
        self.tekst = pg.font.SysFont("Comic Sans MS", 30)

        self.stop = False

        self.run()



    def startscreen(self):
        self.startsc = True
        while self.startsc:
            self.clock.tick(self.FPS)        
            self.startsc_text = self.comic_sans30.render("Easy = U, Normal = I, Hard = P", False, (self.DARKBLUE))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.startsc = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_u:
                        self.enspawn = 4
                        self.tospawn = 3
                        self.trespawn = 3
                        self.startsc = False
                        self.run()
                    if event.key == pg.K_i:
                        self.enspawn = 6
                        self.tospawn = 5
                        self.trespawn = 2
                        self.startsc = False
                        self.run()
                    if event.key == pg.K_p:
                        self.enspawn = 7
                        self.tospawn = 7
                        self.trespawn = 1
                        self.startsc = False
                        self.run()
            
            
            
            self.screen.fill(self.WHITE)
            self.screen.blit(self.startsc_text,(380,600)) 
            
            pg.display.update()

    


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

            self.hits = pg.sprite.spritecollide(self.hero, self.enemy_group,dokill=True)
            if self.hits:
                for hit in self.hits:
                    self.spawn += 1
                self.hits[0].enemyhealth -= 10

            self.hits1 = pg.sprite.spritecollide(self.hero, self.enemy_group2,dokill=True)
            if self.hits1:
                for hit in self.hits1:
                    self.spawn += 1
                self.hits1[0].enemyhealth -= 10

            food_hit = pg.sprite.spritecollide(self.hero, self.food_group, True)
            if food_hit:
                self.hero.life += 10
                self.text_hp = self.comic_sans30.render("HP: " + str(self.hero.life), False, self.LIGHT_GRAY)

            self.food_group 
            
            
            if self.hits:
                self.hero.life -=10
                print (self.hero.life)
                if self.hero.life <= 0:
                    self.stop = True
                    playing = False

            if self.hits1:
                self.hero.life -=10
                print (self.hero.life)
                if self.hero.life <= 0:
                    self.stop = True
                    playing = False
            
            



            #lag nye fiender
            if len(self.enemy_group) < self.enspawn:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemy_group.add(enemy)

            if len(self.enemy_group2) < self.tospawn:
                enemy2 = Enemy2()
                self.all_sprites.add(enemy2)
                self.enemy_group2.add(enemy2)
            

            if len(self.food_group) < self.trespawn:
                food = Food(self)
                self.all_sprites.add(food)
                self.food_group.add(food)

            
            if self.food.pos.x < 1:
                self.food.pos.x == 1800
            
            
            
            self.screen.blit(text_hp, (10,10))               

            

            pg.display.update()    
            
        if self.stop:
            pg.mixer.music.stop()
            self.game_stop()

      
    

    def game_stop(self):
        pg.mixer.music.load('endmusic.mp3') 
        pg.mixer.music.play(0)
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.comic_sans30.render("Easy = U, Normal = I, Hard = P", False, (self.DARKBLUE))
            self.game_over_text1 = self.comic_sans30.render("GAME OVER", False, (self.DARKBLUE))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_u:
                        self.enspawn = 4
                        self.tospawn = 3
                        self.trespawn = 3
                        self.game_over = False
                        self.startover = True
                        
                    if event.key == pg.K_i:
                        self.enspawn = 6
                        self.tospawn = 5
                        self.trespawn = 2
                        self.game_over = False
                        self.startover = True
                        
                    if event.key == pg.K_p:
                        self.enspawn = 7
                        self.tospawn = 7
                        self.trespawn = 1
                        self.game_over = False
                        self.startover = True
                        

            
        
            self.screen.fill(self.LIGHT_GRAY)
            self.screen.blit(self.game_over_text,(380,600))  
            self.screen.blit(self.game_over_text1,(645,12))
            self.screen.blit(dead_screen, (580,100))

            pg.display.update()
            
        if self.startover == True:
            pg.mixer.music.stop()
            pg.mixer.music.load('sangmain.mp3') 
            pg.mixer.music.play(-1)

            self.new1()


g = Game()