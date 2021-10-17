import pygame

class Settings:
    def __init__(self):

        # display resolution
        self.width = 800
        self.height = 600
        self.resolution = self.width, self.height

        self.fps = 60

        # camera settings

        self.camera_speed = 100

        # surface_coordinates

        self.s_x = -100
        self.s_y = -100

