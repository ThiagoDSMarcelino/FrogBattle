import math
import pygame
from settings import *

class Character():
    def __init__(self, x: int, y: int) -> None:
        self.rect = pygame.Rect(0, 0 , 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, RED_BLOCK, self.rect)