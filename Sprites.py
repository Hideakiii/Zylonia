from Settings import *
import pygame
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((45,45))
        #self.image.fill(light_red)
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,height / 2)
        self.pos = vector(x,y)
        self.vel = vector(0,0)
        
    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(x, y,w ,h),
                               self.game.spritesheet.get_image(x ,y, w ,h)]
        for frame in self.standing_frames:
            frame.set.colorkey(black)
        self.walk_frames_r = [self.game.spritesheet.get_image(x ,y, w ,h),
                             self.game.spritesheet.get_image(x ,y, w ,h),
                             self.game.spritesheet.get_image(x ,y, w ,h),
                             self.game.spritesheet.get_image(x ,y, w ,h),
                             self.game.spritesheet.get_image(x ,y, w ,h),
                             self.game.spritesheet.get_image(x ,y, w ,h)]
        for frame in self.standing_frames:
            frame.set.colorkey(black)
        self.walking_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pygame.transform.flip(frame ,True, False))
            frame.set.colorkey(black)
        self.jump_frames = self.game.spritesheet.get_image(x,y,w,h)

    def jump(self):
        ## only jump when standing on platform
        self.rect.x += 1
        collide = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if collide:
            self.vel.y = -12


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
        if abs(self.vel.x) < 0.5:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc   ## pos x,y += gesch. 0 + 0,5 * beschl. 0
        self.rect.midbottom = self.pos

        if self.pos.x + 50 > width:
            self.pos.x = width - 50
        if self.pos.x < 50:
            self.pos.x = 50

    def animate(self):
        now = pygame.time.get_ticks()
        if self.vel.x !=0:
            self.walking = True
        else:
            self.walking = False
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        
        if not self.jumping and not self.walking:
            if now - self.last_update > 300:
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
