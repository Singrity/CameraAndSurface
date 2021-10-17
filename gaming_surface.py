import pygame
from settings import Settings
from camera import Camera
from player import Player


class Surface:

    def __init__(self, screen, color, x, y, width, height):

        self.color = color
        self.screen = screen
        self.settings = Settings()
        self.surface = pygame.Surface((width, height))
        self.camera = Camera(screen, self.surface)
        self.rect = pygame.Rect(x, y, width, height)

        self.player = Player(self.surface, (255, 0, 0), self.camera.rect.x, self.camera.rect.y, 70, 50)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)

    def draw_objects(self):
        self.surface.fill(self.color)
        self.camera.draw()
        #for player in self.players:
            #player.draw()


    def update_objects(self):
        self.camera.update()
        #self.players.update()

    def move_camera_right(self, delta_time):
        self.camera.vector.x = -1

        if self.rect.right != self.camera.rect.right:
            self.rect.x += self.camera.vector.x * self.settings.camera_speed * delta_time
            print(self.camera.vector.x * delta_time)

    def move_camera_left(self, delta_time):
        self.camera.vector.x = 1
        # print(self.rect.x)
        if self.rect.left != self.camera.rect.left:
            self.rect.x += self.camera.vector.x * self.settings.camera_speed * delta_time

    def move_camera_up(self, delta_time):
        self.camera.vector.y = 1
        # print(self.rect.x)
        if self.rect.top != self.camera.rect.top:
            self.rect.y += self.camera.vector.y * self.settings.camera_speed * delta_time

    def move_camera_down(self, delta_time):
        self.camera.vector.y = -1
        # print(self.rect.x)
        if self.rect.bottom != self.camera.rect.bottom:
            self.rect.y += self.camera.vector.y * self.settings.camera_speed * delta_time




