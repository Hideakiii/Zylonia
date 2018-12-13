import Settings
import pygame
import time
import math
import random
vector = pygame.math.Vector2

clock = pygame.time.Clock()
milliseconds = clock.tick(Settings.FPS)  # milliseconds passed since last frame
seconds = milliseconds / 1000.0 # seconds passed since last frame (float)


class Spritesheet:
    # loading spritesheets
    def __init__(self,filename): 
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width // 2, height // 2))
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        pygame.sprite.Sprite.__init__(self)
        self.image = self.game.spritesheet.get_image(614, 1063,120 ,191).convert_alpha()
        self.image.set_colorkey(Settings.black)
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vel = vector(0,0)

    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(9, 10, 89, 177),
                                self.game.spritesheet.get_image(111, 12, 89, 177)]
        for frame in self.standing_frames:
            frame.set_colorkey(Settings.black)
        self.walk_frames_l = [self.game.spritesheet.get_image(9, 10, 89, 177),
                              self.game.spritesheet.get_image(111, 12, 89, 177),
                              self.game.spritesheet.get_image(211, 9, 89, 177),
                              self.game.spritesheet.get_image(316, 11, 89, 177),
                              self.game.spritesheet.get_image(416, 12, 89, 177),
                              self.game.spritesheet.get_image(515, 9, 89, 177)]
        self.walk_frames_r = []
        for frame in self.walk_frames_l:
            frame.set_colorkey(Settings.black)
            self.walk_frames_r.append(pygame.transform.flip(frame, True, False))
        self.jump_frame = self.game.spritesheet.get_image(416, 12, 89, 177)
        self.jump_frame.set_colorkey(Settings.black)        

    def jump(self):
        ## only jump when standing on platform
        self.rect.x += 2
        collide = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if collide:
            self.vel.y = -Settings.JUMP_POWER * seconds

    def update(self):
        self.animate()
        self.acc = vector(0, Settings.gravity * seconds)
        self.keystate = pygame.key.get_pressed()
        if self.keystate[pygame.K_a]:
            self.acc.x += -Settings.player_acc * seconds
        if self.keystate[pygame.K_d]:
            self.acc.x += Settings.player_acc * seconds   ## beschl. x 0 = 0,5

        self.acc.x += self.vel.x * Settings.player_friction * seconds  ## beschl. 0 += gesch. 0 * -0,12
        self.vel += self.acc                    ## gesch. 0 += beschl. 0
        self.rect.move_ip(self.vel)

        if abs(self.vel.x) < 0.2:
            self.vel.x = 0
        if self.rect.x + 50 > Settings.WIDTH:
            self.rect.x = Settings.WIDTH - 50
        if self.rect.x < 50:
            self.rect.x = 50

    def animate(self):
        now = pygame.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # show walk animation
        if self.walking:
            if now - self.last_update > 140:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                left = self.rect.left
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.left = left
        # show idle animation
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                left = self.rect.left
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.left = left
                
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.load_images(game)
        self.image = self.Plat_list[1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_images(self,game):
        self.Plat_list = [self.game.platsheet.get_image(26,39,362,189),
                            self.game.platsheet.get_image(421,45,251,79)]

        for plat in self.Plat_list:
            plat.set_colorkey(Settings.black)

    def Scroll(self):
        self.rect.x -= Settings.GESCH * seconds

    def update(self):
        self.Scroll()


class Background(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.load_images(game)
        self.image = self.Back_list[0]
        ##self.image.transform.scale(image ,(720,1280))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def load_images(self,game):
        self.Back_list = [self.game.backsheet.get_image(0,0,1920,1080).convert_alpha()]
        for back in self.Back_list:
            back.set_colorkey(Settings.black)
            back = pygamec.transform.scale(bak ,(1920,1080))

    def Scroll(self):
        self.rect.x -= Settings.GESCH * seconds

    def update(self):
        self.Scroll()


class Fly_Plat(pygame.sprite.Sprite):
    def __init__(self,x ,y,game):
        self.game = game
        self.load_images(game)
        pygame.sprite.Sprite.__init__(self)
        self.image = self.Flyplat_list[0]
        self.rect = self.image.get_rect()
        self.start_pos = vector(x,y)
        self.pos = vector(x,y)

    def update(self):
        self.pos.y = self.pos.y + math.sin(time.time() * Settings.FLYPLAT_FREQUENZY) * Settings.FLYPLAT_AMPLITUDE
        self.rect.midbottom = self.pos

    def load_images(self,game):
        self.Flyplat_list = [self.game.platsheet.get_image(26,39,362,189),
                            self.game.platsheet.get_image(421,45,251,79)]
        for plat in self.Flyplat_list:
            plat.set_colorkey(Settings.black)
