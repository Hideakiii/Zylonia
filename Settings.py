
## Game settings

WIDTH = 1280
HEIGHT = 720
FPS = 60
GAME_TITLE = "Zylonia"
GESCH = 100
## images
SPRITESHEET = "Sprites_v1.png"
PLATSHEET = "Flyplatforms_v2.png"
BACKSHEET = "martin-vallin-bakgrund-lvl5a.jpg"  ###  All background images are from: https://www.artstation.com/artwork/Lb8xK

SHADOW_MASK = "Shadow_mask.png"
SHADOW_RADIUS = (800 ,700)

        
platform_list = [(WIDTH / 5 - 50 , HEIGHT * 3 / 4),
                 (0 ,HEIGHT - 50),
                 (100 ,HEIGHT - 50),
                 (200 ,HEIGHT - 50),
                 (150 , HEIGHT - 300),
                 (400 , 350),
                 (900 , 500),
                 (1000 , 600),
                 (900 , 550),
                 (800 , 450),
                 (1100 , 700),
                 (550 , 600),
                 (900 , 500),
                 (1500 , 600),
                 (1300 , 550),
                 (1050 , 450),
                 (1250 , 700),
                 (550 , 600),
                 (600 , 300)]
platform_list_2 = [(0 ,HEIGHT - 50),
                    (100 ,HEIGHT - 50),
                    (200 ,HEIGHT - 50),
                    (300 ,HEIGHT - 50),
                    (20 , 510 ),
                    (470 , 320 ),
                    (1100 , 700),
                    (1000 , 650),
                    (290 , 390)]
Flyplat_list = [
                    (500 , 600)]

## Player Properties
player_acc = 70 #0.4
player_friction = -12 #-0.12
gravity = 60 #0.6
JUMP_POWER = 1100 #8
## Flying platforms properties

FLYPLAT_FREQUENZY = 1
FLYPLAT_AMPLITUDE = 1

## Colors
white = (255,255,255)
black = (0,0,0)
grey = (15,15,15)
light_grey = (35,35,35)
dark_blue = (0,0,180)
blue = (0,0,200)
light_blue = (0,0,255)
red = (200,0,0)
light_red = (255,0,0)
green = (0,200,0)
light_green = (0,255,0)