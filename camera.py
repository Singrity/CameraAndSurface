import pygame
from settings import Settings


class Camera:

    def __init__(self, screen, gaming_surface):
        self.gaming_surface = gaming_surface
        self.settings = Settings()
        self.rect = pygame.Rect(self.settings.width / 2, self.settings.height / 2, 20, 20)
        self.screen = screen
        self.vector = pygame.Vector2(0, 0)

    def draw(self):
        #pygame.draw.circle(self.screen, (255, 0, 0), self.rect.center, 10)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)

    def update(self):
        if self.vector.x != 0 or self.vector.y != 0:
            self.vector = self.vector.normalize()


