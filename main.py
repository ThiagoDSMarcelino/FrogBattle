import os
import pygame

from settings import * 
from weapon import Weapon
from character import Character
from Text import Text
from item import Item

# Change the iamge size
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

# Draw info of player
def draw_info():
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_SIZE[0], 50))
    pygame.draw.line(screen, WHITE, (0, 50), (SCREEN_SIZE[0], 50))

    heart_full = scale_img(pygame.image.load(f"{PATH_ITEMS}/heart_full.png"), HEART_SCALE)
    heart_half = scale_img(pygame.image.load(f"{PATH_ITEMS}/heart_half.png"), HEART_SCALE)
    heart_empty = scale_img(pygame.image.load(f"{PATH_ITEMS}/heart_empty.png"), HEART_SCALE)

    heart_half_drawn = False
    for i in range(5):
        if player.health >= ((i+1) * 20):
            screen.blit(heart_full, (10 + i * 50, -10))
        elif player.health % 20 > 0 and not heart_half_drawn:
            screen.blit(heart_half, (10 + i * 50, -10))
            heart_half_drawn = True
        else:
            screen.blit(heart_empty, (10 + i * 50, -10))
    
    draw_text(f"X: {player.score}", font, WHITE, (SCREEN_SIZE[0] - (160 + 15 * (int(player.score / 10) + 1)), 15))

# Get all the necessary images for the characters
def get_character_images():
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
    return character_animations

# Get all coin images to animate the coin
def get_coin_images():
    coin_images = []
    for i in range(5):
        coin_images.append(scale_img(pygame.image.load(f"{PATH_ITEMS}/coin{i}.png"), ITEM_SCALE))
    return coin_images

# Draw text
def draw_text(text, font, text_col, xy):
    img = font.render(text, True, text_col)
    screen.blit(img, xy)

# Start basic functions
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Frog Battle')
screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.Font("assets/fonts/AtariClassic.ttf", 20)

# Possible moves
moving_up = False
moving_down = False
moving_left = False
moving_right = False

# Loading images
character_animation = get_character_images()
coin_animation = get_coin_images()
gun_image = scale_img(pygame.image.load(f"{PATH_WEAPONS}/gun.png"), WEAPON_SCALE)
bullet_image = scale_img(pygame.image.load(f"{PATH_WEAPONS}/gun_bullet.png"), WEAPON_SCALE)
red_potion = scale_img(pygame.image.load(f"{PATH_ITEMS}/red_potion.png"), ITEM_SCALE)

# Create objects
player = Character(100, 100, 90, character_animation, "frog_soldier")
enemy = Character(200, 300, 100, character_animation, "skull")
gun = Weapon(gun_image, bullet_image)

# Enemies
enemy_list = []
enemy_list.append(enemy)

# Sprites groups
damage_text_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
item_group = pygame.sprite.Group()

score_coin = Item(SCREEN_SIZE[0] - 200, 25, 0, coin_animation)
item_group.add(score_coin)

item_group.add(Item(200, 200, 1, [red_potion]))
item_group.add(Item(400, 400, 0, coin_animation))

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
    for enemy in enemy_list:
        enemy.update()
    bullet = gun.update(player)
    if bullet:
        bullet_group.add(bullet)
    for bullet in bullet_group:
        damage, damage_pos = bullet.update(enemy_list)
        if damage:
            damage_text = Text(damage_pos.centerx, damage_pos.y, damage, RED, font)
            damage_text_group.add(damage_text)
    damage_text_group.update()
    item_group.update(player)

    # Draw all elements
    player.draw(screen)
    gun.draw(screen)
    bullet_group.draw(screen)
    damage_text_group.draw(screen)
    for enemy in enemy_list:
        enemy.draw(screen)
    for bullet in bullet_group:
        bullet.draw(screen)
    item_group.draw(screen)
    draw_info()
    score_coin.draw(screen)

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