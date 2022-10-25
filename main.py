import pygame
from settings import * 
from character import Character

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Frog Battle')

clock = pygame.time.Clock()

moving_up = False
moving_down = False
moving_left = False
moving_right = False

player = Character(100, 100)

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

    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    pygame.display.update()

pygame.quit()