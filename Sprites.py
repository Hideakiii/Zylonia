from Settings import *
import pygame
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45,45))
        self.image.fill(light_red)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,height / 2)
        self.pos = vector(x,y)
        self.vel = vector(0,0)

    def jump(self):
        ## only jump when standing on platform
        self.rect.x += 1
        collide = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if collide:
            self.vel.y = -12


    def update(self):
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

        if self.pos.x + 50 > width:
            self.pos.x = width - 50
        if self.pos.x < 50:
            self.pos.x = 50

        #self.rect.center = (self.pos)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(light_blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
