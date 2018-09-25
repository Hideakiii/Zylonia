
## Game settings

WIDTH = 1280
HEIGHT = 720
FPS = 60
GAME_TITLE = "Zylonia"
HS_FILE = "highscore.txt"
SPRITESHEET = "Sprites_v1.png"
SHADOW_MASK = ""
## Flying platforms properties
FLYPLAT_ACC = 0.5
FLYPLAT_GRAV = 0.4
FLYPLAT_MOVE = 20
FLYPLAT_FRICTION = -0.12

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
                    (500 , 600 , 70 , 20)]
                    #(450 , 300 , 350 , 20),
                    #(300 , 400 , 220 , 20)]

## Player Properties
player_acc = 0.5
player_friction = -0.12
gravity = 0.5
JUMP_POWER = 12

## Colors
white = (255,255,255)
black = (0,0,0)
grey = (15,15,15)
dark_blue = (0,0,180)
blue = (0,0,200)
light_blue = (0,0,255)
red = (255,0,0)
light_red = (200,0,0)
green = (0,255,0)

