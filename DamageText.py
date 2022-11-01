import pygame
from settings import *

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, damage: int, color: str, font) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 30:
            self.kill()
