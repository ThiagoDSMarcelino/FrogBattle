import os
import pygame
from settings import * 
from character import Character
from weapon import Weapon

def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Frog Battle')

clock = pygame.time.Clock()

moving_up = False
moving_down = False
moving_left = False
moving_right = False

gun_image = pygame.image.load(f"{PATH_WEAPONS}/x90.png")


character_animations = {}
for character in os.listdir(PATH_CHARACTERS):
    animation_list = []
    for type in os.listdir(f"{PATH_CHARACTERS}/{character}"):
        temp_list = []
        for img in os.listdir(f"{PATH_CHARACTERS}/{character}/{type}"):
            img = pygame.image.load(f"{PATH_CHARACTERS}/{character}/{type}/{img}").convert_alpha()
            img = scale_img(img, SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    character_animations[character] = animation_list

player = Character(100, 100, character_animations, "frog_soldier")

gun = Weapon(gun_image)

running = True
while running:
    clock.tick(FPS)

    screen.fill(BG)

    dx = 0
    dy = 0
    if moving_up == True:
        dy = -SPEED
    if moving_down == True:
        dy = SPEED
    if moving_left == True:
        dx = -SPEED
    if moving_right == True:
        dx = SPEED

    player.move(dx, dy)
    player.update()
    player.draw(screen)
    
    gun.update(player)
    gun.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                moving_right = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                moving_down = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                moving_right = False

    pygame.display.update()

pygame.quit()