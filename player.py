import pygame
from settings import Settings
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, surface, color, x, y, width, height):
        super().__init__()
        self.surface = surface
        self.color = color
        self.settings = Settings
        self.rect = pygame.Rect(x, y, width, height)
        self.vector = pygame.Vector2(0, 0)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update(self):
        if self.vector.x != 0 or self.vector.y != 0:
            self.vector = self.vector.normalize()