import pygame

from .Renderer import Renderer

class Image:
    def __init__(self, path: str, x, y, w, h) -> None:
        self.originalImage = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.originalImage, (w, h))
        self.rect = self.image.get_rect(topleft=(x,y))
    def Resize(self, w, h):
        self.image = pygame.transform.scale(self.originalImage, (w, h))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        
    def Draw(self):
        Renderer.DrawImage(self.image, self.rect)
