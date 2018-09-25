import pygame
import sys
import random
import time
from Settings import *
from Sprites import *
from os import path

class Game:
    def __init__(self):
        ## initialize game window,etc
        pygame.init()
        pygame.mixer.init()

        self.game_display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
    

    def new_game(self):
        ## start a new game
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(100,250, game)            
        self.all_sprites.add(self.player) 
        for plat in platform_list:
            p = Platform(*plat ,game)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        ## game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        ## game loop - update
        self.all_sprites.update()
        
        if self.player.vel.y > 0:
            collide = pygame.sprite.spritecollide(self.player ,self.platforms ,False)
            if collide:
                lowest = collide[0]
                for col in collide:
                    if col.rect.bottom > lowest.rect.centery:
                        lowest = col
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y = lowest.rect.top + 1
                    self.player.vel.y = 0

        ## if player reaches the side of the screen 
        if self.player.rect.right >= WIDTH - 150:
            # Display "E" button
            self.keystate = pygame.key.get_pressed()
            if self.keystate[pygame.K_e]:
                self.player.pos = (50,500)
                for plat in self.platforms:
                    plat.kill()
                for plat in platform_list_2:
                    p = Platform(*plat ,game)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                for plat in Flyplat_list:
                    p = Fly_Plat(*plat ,game)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
       
            #next_scene()

    def events(self):
        ## game loop - events
        ## event check 
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        ## game loop - draw
        self.game_display.fill(grey)
        self.all_sprites.draw(self.game_display)

        pygame.display.flip()

    def Start_Screen(self):
        ## show game start screen
        pass

    def Gameover_Screen(self):
        ## shoe game over screen
        pass

game = Game()
player = Player(100,250,game)
game.Start_Screen()
while game.running :
    game.new_game()
    game.Gameover_Screen()

    pygame.quit()
    quit()
