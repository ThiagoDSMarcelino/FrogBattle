import pygame 
import math

from settings import BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.dy = math.sin(math.radians(self.angle)) * BULLET_SPEED
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.centerx - int(self.image.get_width() / 2), self.rect.centery - int(self.image.get_height() / 2)))