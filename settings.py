import pygame

FPS = 60
SCREEN_SIZE = (1280, 720)

SPEED = 5
BULLET_SPEED = 10

CHARACTER_SCALE = 3
WEAPON_SCALE = 2
ITEM_SCALE = 2


WEAPON_OFFSET = 16

PATH_IMAGES = "assets/images"
PATH_CHARACTERS = f"{PATH_IMAGES}/characters"
PATH_WEAPONS = f"{PATH_IMAGES}/weapons"
PATH_ITEMS = f"{PATH_IMAGES}/items"

RED = (255, 0, 0)
BG = (40, 25, 25)

pygame.init()
FONT = pygame.font.Font("assets/fonts/AtariClassic.ttf", 20)