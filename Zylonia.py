import pygame
import sys
import random
import time
import Settings
from Sprites import *
from os import path

class Game:
    def __init__(self):
        ## initialize game window,etc
        pygame.init()
        pygame.mixer.init()

        self.game_display = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pygame.display.set_caption(Settings.GAME_TITLE)

        self.game_display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir,Settings.SPRITESHEET))
        ## shadow effect
        self.fog = pygame.Surface((Settings.WIDTH ,Settings.HEIGHT))
        self.fog.fill(Settings.light_grey)
        self.shadow_mask = pygame.image.load(path.join(img_dir, Settings.SHADOW_MASK)).convert_alpha()
        self.shadow_mask = pygame.transform.scale(self.shadow_mask, Settings.SHADOW_RADIUS)
        self.shadow_rect = self.shadow_mask.get_rect()
        

            

    def new_game(self):
        ## start a new game
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(100,250, game)            
        self.all_sprites.add(self.player) 
        for plat in Settings.platform_list:
            p = Platform(*plat ,game)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.shadow = True     ### To toggle the shadow_mask on/off
        self.run()

    def run(self):
        ## game loop
        self.playing = True
        while self.playing:
            self.clock.tick(Settings.FPS)
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
        if self.player.rect.right >= Settings.WIDTH - 150:
            # Display "E" button
            self.keystate = pygame.key.get_pressed()
            if self.keystate[pygame.K_e]:
                self.player.pos = (50,500)
                for plat in self.platforms:
                    plat.kill()
                for plat in Settings.platform_list_2:
                    p = Platform(*plat ,game)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                for plat in Settings.Flyplat_list:
                    p = Fly_Plat(*plat ,game)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
       
            #next_scene()


    def render_fog(self):   ### draf the shadowmask onto the player position
        self.fog.fill(Settings.light_grey)
        self.shadow_rect.center = self.player.rect.center
        self.fog.blit(self.shadow_mask ,self.shadow_rect)
        self.game_display.blit(self.fog, (0,0) ,special_flags=pygame.BLEND_MULT)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    self.shadow = not self.shadow

    def draw(self):
        ## game loop - draw
        self.game_display.fill(Settings.grey)
        self.all_sprites.draw(self.game_display)
        if self.shadow:
            self.render_fog()

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
