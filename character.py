import pygame
from settings import *

class Character():
    def __init__(self, X: int, Y: int) -> None:
        self.rect = pygame.Rect(0, 0 , 40, 40)
        self.rect.center = (X, Y)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, RED_BLOCK, self.rect)