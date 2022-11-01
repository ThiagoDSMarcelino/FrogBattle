import pygame 
import math
from settings import *
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.dy = -(math.sin(math.radians(self.angle)) * BULLET_SPEED)

        self.damage = 10
    
    def update(self, enemy_list):
        damage = 0
        damage_pos = None

        self.rect.x += self.dx
        self.rect.y += self.dy

        if (
            self.rect.right < 0 or 
            self.rect.bottom < 0 or 
            self.rect.left > SCREEN_SIZE[0] or
            self.rect.top > SCREEN_SIZE[1]            
            ):
            self.kill()

        for enemy in enemy_list:
            if enemy.rect.colliderect(self.rect) and enemy.alive:
                damage = 10 + random.randint(-5, 5)
                damage_pos = enemy.rect
                enemy.health -= damage
                self.kill()
                break
        return damage, damage_pos

    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.centerx - int(self.image.get_width() / 2), self.rect.centery - int(self.image.get_height() / 2)))