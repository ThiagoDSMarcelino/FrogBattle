import pygame
import math
from settings import WEAPON_OFFSET, WEAPON_SCALE
from bullet import Bullet

class Weapon():
    def __init__(self, image, bullet_image) -> None:
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.bullet_image = bullet_image
        self.rect = self.image.get_rect()
        self.fired = False
        self.last_shot = pygame.time.get_ticks()


    def update(self, player):
        shot_cooldown = 300

        bullet = None

        self.rect.center = player.rect.center

        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.centerx
        y_dist = -(pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))


        if pygame.mouse.get_pressed()[0] and not self.fired and (pygame.time.get_ticks() - self.last_shot) >= shot_cooldown:
            bullet = Bullet(self.bullet_image, self.rect.centerx, self.rect.centery, self.angle)
            self.last_shot = pygame.time.get_ticks()
            self.fired = True
        
        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

        return bullet


    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, (self.rect.centerx - int(self.image.get_width() / 2), self.rect.centery - int(self.image.get_height() / 2)))