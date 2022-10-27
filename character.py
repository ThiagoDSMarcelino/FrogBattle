import math
from turtle import back, update
import pygame
from settings import *

class Character():
    def __init__(self, x: int, y: int, mob_dict: dict, mob_name: str) -> None:
        #CREATE HITBOX
        self.rect = pygame.Rect(0, 0 , 32 * SCALE, 32 * SCALE)
        self.rect.center = (x, y)
        
        self.action = 2 # 0: Back - 1: Front - 2: Idle - 3: Side
        self.frame_index = 0
        self.animation_list = mob_dict[mob_name]
        
        self.name = mob_name
        self.flip = False
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]
        

    def move(self, dx, dy):
        
        
        if dx != 0:
            self.update_action(3)
        elif dy > 0:
            self.update_action(1)
        elif dy < 0:
            self.update_action(0)
        else:
            self.update_action(2)

        if dx < 0:
            self.flip =  True
        if dx > 0:
            self.flip = False

        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    def update(self):        
        animation_cooldown = 70
        self.image = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface: pygame.Surface) -> None:
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, RED_BLOCK, self.rect, 1)