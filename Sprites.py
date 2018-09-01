from Settings import *
import pygame
vector = pygame.math.Vector2

class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):  
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width // 2, height // 2))
        return image

    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(614, 1063, 120, 191),
                                self.game.spritesheet.get_image(690, 406, 120, 201)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [self.game.spritesheet.get_image(678, 860, 120, 201),
                              self.game.spritesheet.get_image(692, 1458, 120, 207)]
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))
        self.jump_frame = self.game.spritesheet.get_image(382, 763, 150, 181)
        self.jump_frame.set_colorkey(BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
    #    self.load_images()
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((45,45))
        #self.image.fill(light_red)
        self.image = self.game.spritesheet.get_image(50, 200,60 ,200)
        self.image.set.colorkey(black)
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HEIGHT / 2)
        self.pos = vector(x,y)
        self.vel = vector(0,0)
        

    def jump(self):
        ## only jump when standing on platform
        self.rect.x += 1
        collide = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if collide:
            self.vel.y = -JUMP_POWER


    def update(self):
        self.animate()
        self.acc = vector(0, gravity)
        self.keystate = pygame.key.get_pressed()
        if self.keystate[pygame.K_a]:
            self.acc.x = -player_acc
        if self.keystate[pygame.K_d]:
            self.acc.x = player_acc             ## beschl. x 0 = 0,5

        self.acc.x += self.vel.x * player_friction  ## beschl. 0 += gesch. 0 * -0,12
        self.vel += self.acc                    ## gesch. 0 += beschl. 0
        self.pos += self.vel + 0.5 * self.acc   ## pos x,y += gesch. 0 + 0,5 * beschl. 0
        self.rect.midbottom = self.pos

        if self.pos.x + 50 > WIDTH:
            self.pos.x = WIDTH - 50
        if self.pos.x < 50:
            self.pos.x = 50

        #self.rect.center = (self.pos)
    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # show walk animation
        if self.walking:
            if now - self.last_update > 180:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        # show idle animation
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(light_blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
