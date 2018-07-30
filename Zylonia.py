import pygame
import sys
import random
import time
from Settings import *
from Sprites import *

class Game:
    def __init__(self):
        ## initialize game window,etc
        pygame.init()
        pygame.mixer.init()

        self.game_display = pygame.display.set_mode((width, height))
        pygame.display.set_caption(game_title)
        self.clock = pygame.time.Clock()
        self.running = True

    def new_game(self):
        ## start a new game
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(100,250, game)            
        self.p1 = Platform(0 ,height - 50 , width ,50)
        self.p2 = Platform(width / 5 - 50 , height * 3 / 4, 100, 20)
        self.all_sprites.add(self.player) 
        for plat in platform_list:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        ## game loop
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
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
                    if col.rect.bottom > lowest.rect.bottom:
                        lowest = col
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y = lowest.rect.top + 1
                    self.player.vel.y = 0


        ## if player reaches the side of the screen 
        if self.player.rect.right >= width - 100:
            self.player.pos.x = 50
            #for plat in self.platforms:
                #if plat.rect.right >= width:
                    #plat.kill()
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
game.Start_Screen()
while game.running :
    game.new_game()
    game.Gameover_Screen()

    pygame.quit
