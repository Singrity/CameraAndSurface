import pygame, time
from settings import Settings
from gaming_surface import Surface


class Game:

    def __init__(self):
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.gaming_surface = Surface(self.screen, (255, 23, 255), self.settings.s_x, self.settings.s_y, 1000, 1000)

        pygame.display.set_caption("MEGA")

        self.clock = pygame.time.Clock()
        self.is_running = False

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.prev_time = time.time()

    def run(self):

        self.is_running = True

        while self.is_running:
            time = self.clock.tick(self.settings.fps)
            time_s = time / 1000.

            self.handle_events()
            self.draw()
            self.update(time_s)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                self.handle_key_down_events(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up_events(event)

    def handle_key_down_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self.stop()
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        if event.key == pygame.K_LEFT:
            self.moving_left = True
        if event.key == pygame.K_UP:
            self.moving_up = True
        if event.key == pygame.K_DOWN:
            self.moving_down = True

    def handle_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        if event.key == pygame.K_LEFT:
            self.moving_left = False
        if event.key == pygame.K_UP:
            self.moving_up = False
        if event.key == pygame.K_DOWN:
            self.moving_down = False

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.gaming_surface.surface, (self.gaming_surface.rect.x, self.gaming_surface.rect.y))
        self.gaming_surface.draw_objects()

    def update(self, dt):
        self.make_camera_move(dt)
        self.gaming_surface.update_objects()
        pygame.display.update()

    def make_camera_move(self, dt):
        if self.moving_right:
            self.gaming_surface.move_camera_right(dt)
        if self.moving_left:
            self.gaming_surface.move_camera_left(dt)
        if self.moving_up:
            self.gaming_surface.move_camera_up(dt)
        if self.moving_down:
            self.gaming_surface.move_camera_down(dt)


    def stop(self):
        self.is_running = False
        exit()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
