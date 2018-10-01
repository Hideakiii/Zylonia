
## Game settings

WIDTH = 1280
HEIGHT = 720
FPS = 60
GAME_TITLE = "Zylonia"

SPRITESHEET = "Sprites_v1.png"
PLATSHEET = "Flyplatforms_v2.png"

SHADOW_MASK = "Shadow_mask.png"
SHADOW_RADIUS = (700 ,700)

## Platforms
platform_list = [(WIDTH / 5 - 50 , HEIGHT * 3 / 4, 100, 20),
                 (0 ,HEIGHT - 50 , WIDTH ,50),
                 (150 , HEIGHT - 300 , 100, 20),
                 (400 , 350 , 150, 20),
                 (600 , 300 , 100, 20)]
platform_list_2 = [(0 ,HEIGHT - 50 , WIDTH ,50),
                    (20 , 510 , 250 , 20),
                    (470 , 320 , 370 , 20),
                    (290 , 390 , 210 , 20)]
Flyplat_list = [
                    (500 , 600)]

## Player Properties
player_acc = 0.5
player_friction = -0.12
gravity = 0.5
JUMP_POWER = 12
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