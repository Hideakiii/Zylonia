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
        self.back_display = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        self.front_display = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pygame.display.set_caption(Settings.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()
        self.score = 0

    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir,Settings.SPRITESHEET))
        self.platsheet = Spritesheet(path.join(img_dir,Settings.PLATSHEET))
        self.backsheet = Spritesheet(path.join(img_dir,Settings.BACKSHEET))
        ## shadow effect
        self.fog = pygame.Surface((Settings.WIDTH ,Settings.HEIGHT))
        self.fog.fill(Settings.light_grey)
        self.shadow_mask = pygame.image.load(path.join(img_dir, Settings.SHADOW_MASK)).convert_alpha()
        self.shadow_mask = pygame.transform.scale(self.shadow_mask, Settings.SHADOW_RADIUS)
        self.shadow_rect = self.shadow_mask.get_rect()
        
    def new_game(self):
        ## start a new game
        self.background = Background(game)
        self.BG = pygame.sprite.Group()
        self.BG.add(self.background)
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(100,250, game)    
        self.P_group = pygame.sprite.Group()
        self.P_group.add(self.player) 
        self.all_sprites.add(self.background)    
        for plat in Settings.platform_list:
            p = Platform(*plat ,game)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.all_sprites.add(self.player) 
        self.all_sprites.add(self.background)
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
        if self.player.rect.y >= Settings.HEIGHT:
            #dead()
            pass
        if self.player.vel.y > 0:
            collide = pygame.sprite.spritecollide(self.player ,self.platforms ,False)
            if collide:
                lowest = collide[0]
                for col in collide:
                    if col.rect.bottom > lowest.rect.centery:
                        lowest = col
                if self.player.rect.bottom < lowest.rect.bottom:
                    self.player.rect.bottom = lowest.rect.top + 1
                    self.player.vel.y = 0
                    for plat in self.platforms:
                        self.player.vel.x -= Settings.GESCH / 60 * seconds

        ## löscht/killt Platformen ,die links aus dem Bildschirm hinaus gelangen
        for plat in self.platforms:
            if plat.rect.x <= -plat.rect.right - 100:
                plat.kill()
                self.score += 1
                Settings.GESCH += 1
                print("Score: " ,self.score)

        ## lässt immer 25 Platformen auf dem Bildschirm erscheinen      
        while len(self.platforms) < 25:
            height = random.randrange(450 ,700)
            p = Platform(random.randrange(Settings.WIDTH + 50 ,Settings.WIDTH + 450),height,game)
            self.platforms.add(p)
            self.all_sprites.add(p)

        ## if player reaches the side of the screen 
        if self.player.rect.right >= Settings.WIDTH - 200:
            # Display "E" button
            self.keystate = pygame.key.get_pressed()
            if self.keystate[pygame.K_e]:
                self.player.rect.center = (50,500)
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
        self.fog.fill(Settings.grey)
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
                if event.key == pygame.K_n:
                    self.shadow = not self.shadow

                if event.key == pygame.K_t:         #### Aus/Ein-schaltung der Gravität
                    if Settings.gravity == 0:
                        Settings.gravity = 60
                    else:   
                        Settings.gravity = 0

    def draw(self):
        ## game loop - draw
        self.back_display.fill(Settings.grey)
        self.BG.draw(self.back_display)
        self.all_sprites.draw(self.game_display)
        self.P_group.draw(self.front_display)
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