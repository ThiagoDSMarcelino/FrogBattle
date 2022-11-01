import os
import pygame

from settings import * 
from weapon import Weapon
from character import Character
from DamageText import DamageText

# Change the iamge size
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

# Draw info of player
def draw_info():
    heart_full = scale_img(pygame.image.load(f"{PATH_ITEMS}/heart_full.png"), ITEM_SCALE)
    heart_falf = scale_img(pygame.image.load(f"{PATH_ITEMS}/heart_half.png"), ITEM_SCALE)
    heart_empty = scale_img(pygame.image.load(f"{PATH_ITEMS}/heart_empty.png"), ITEM_SCALE)
    for i in range(5):
        if player.health >= ((i+1) * 20):
            screen.blit(heart_full, (10 + i * 50, 0))

# Start basic functions
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Frog Battle')
screen = pygame.display.set_mode(SCREEN_SIZE)

# Possible moves
moving_up = False
moving_down = False
moving_left = False
moving_right = False

# Get all the necessary images for the characters
character_animations = {}
for character in os.listdir(PATH_CHARACTERS):
    animation_list = []
    for type in os.listdir(f"{PATH_CHARACTERS}/{character}"):
        temp_list = []
        for img in os.listdir(f"{PATH_CHARACTERS}/{character}/{type}"):
            img = pygame.image.load(f"{PATH_CHARACTERS}/{character}/{type}/{img}").convert_alpha()
            img = scale_img(img, CHARACTER_SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    character_animations[character] = animation_list

gun_image = scale_img(pygame.image.load(f"{PATH_WEAPONS}/gun.png"), WEAPON_SCALE)
bullet_image = scale_img(pygame.image.load(f"{PATH_WEAPONS}/gun_bullet.png"), WEAPON_SCALE)

player = Character(100, 100, 100, character_animations, "frog_soldier")
enemy = Character(200, 300, 100, character_animations, "skull")
gun = Weapon(gun_image, bullet_image)

enemy_list = []
enemy_list.append(enemy)

damage_text_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

running = True
while running:
    # FPS
    clock.tick(FPS)

    # Background color
    screen.fill(BG)

    # Set where are you going
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
    
    # Update all elements
    player.update()
    damage_text_group.update()
    for enemy in enemy_list:
        enemy.update()
    bullet = gun.update(player)
    if bullet:
        bullet_group.add(bullet)
    for bullet in bullet_group:
        damage, damage_pos = bullet.update(enemy_list)
        if damage:
            damage_text = DamageText(damage_pos.centerx, damage_pos.y, damage, RED)
            damage_text_group.add(damage_text)

    # Draw all elements
    player.draw(screen)
    gun.draw(screen)
    bullet_group.draw(screen)
    damage_text_group.draw(screen)
    for enemy in enemy_list:
        enemy.draw(screen)
    for bullet in bullet_group:
        bullet.draw(screen)
    draw_info()

    # Check events
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