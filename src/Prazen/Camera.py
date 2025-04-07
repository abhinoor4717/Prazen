import pygame

from util.PositionUtil import Coordinate

class Camera:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 1000

    def OnWindowResize(self, w, h):
        self.width = w
        self.height = h

    def TranslatePos(self, x, y):
        return Coordinate(x - self.x, y + self.y)
    def Move(self, dt):
        keys = pygame.key.get_pressed()

        velocity = self.speed * dt
        if (keys[pygame.K_RIGHT]):
            self.x += velocity
        if (keys[pygame.K_LEFT]):
            self.x -= velocity
        if (keys[pygame.K_UP]):
            self.y += velocity
        if (keys[pygame.K_DOWN]):
            self.y -= velocity