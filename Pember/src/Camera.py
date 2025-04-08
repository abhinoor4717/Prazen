import pygame
import numpy as np
from dataclasses import dataclass

@dataclass
class Coordinate:
    x: float
    y: float

class Settings:
    Debug = True

class Camera:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y], dtype=float)
        self.width = width
        self.height = height
        self.speed = 1000

        if Settings.Debug:
            from .Text import Text
            self.Text = Text(f'Camera | Pos: ({self.position[0]}, {self.position[1]}) | Size: ({self.width},  {self.height})', 0,30, 20)

        self.UpdateMatrix()

    def UpdateMatrix(self):
        # Translate the world by negative camera position
        tx = -self.position[0]
        ty = -self.position[1]

        self.matrix = np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ])

    def OnWindowResize(self, w, h):
        self.width = w
        self.height = h
        self.UpdateMatrix()

    def project(self, world_pos):
        """ Convert a 2D world position (tuple or array) to screen space """
        pos = np.array([world_pos[0], world_pos[1], 1])
        result = self.matrix @ pos
        return result[:2]  # Return x, y screen position
    def Move(self, dt):
        if Settings.Debug:
            self.Text.Update(f'Camera | Pos: ({self.position[0]}, {self.position[1]}) | Size: ({self.width},  {self.height})', None, None, static=True)
        keys = pygame.key.get_pressed()
        velocity = self.speed * dt

        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_RIGHT]:
                self.position[0] += velocity
            if keys[pygame.K_LEFT]:
                self.position[0] -= velocity
            if keys[pygame.K_UP]:
                self.position[1] -= velocity
            if keys[pygame.K_DOWN]:
                self.position[1] += velocity
            if keys[pygame.K_0]:
                self.position[0] = 0
                self.position[1] = 0

            self.UpdateMatrix()
