import pygame

from .Camera import Camera
from Pember import Text
from Pember import Renderer

class Settings:
    Display_Position = True

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        super().__init__()
        self.screen = screen

        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x, y, w, h)

        self.speed = 1000
        self.PlayerPosText = None
        if Settings.Display_Position:
            self.PlayerPosText = Text(f'Player pos: ({self.x}, {self.y})', self.x, self.y - 15, 20)

    def Move(self, dt):
        keys = pygame.key.get_pressed()

        velocity = self.speed * dt
        if not (keys[pygame.K_LSHIFT]):
            if (keys[pygame.K_RIGHT]):
                self.x += velocity
            if (keys[pygame.K_LEFT]):
                self.x -= velocity
            if (keys[pygame.K_UP]):
                self.y -= velocity
            if (keys[pygame.K_DOWN]):
                self.y += velocity
            if (keys[pygame.K_0]):
                self.x = 0
                self.y = 0

    def Draw(self):
        Renderer.DrawRect(pygame.rect.Rect(self.x, self.y, self.width, self.height), "white")
        if self.PlayerPosText:
            self.PlayerPosText.Update(f'Player pos: ({self.x}, {self.y})', self.x, self.y - 15)
    
    def Update(self, dt):
        self.Move(dt)
        self.Draw()