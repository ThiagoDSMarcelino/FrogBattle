from turtle import left
import pygame
from settings import * 
from character import Character

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Frog Battle')

player = Character(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("left")
            if event.key == pygame.K_w:
                print("up")
            if event.key == pygame.K_s:
                print("down")
            if event.key == pygame.K_d:
                print("right")

    player.draw(screen)


    pygame.display.update()

pygame.quit()