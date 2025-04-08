import pygame

class Image:
    def __init__(self, path: str, x, y, w, h) -> None:
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect(topleft=(x,y))
    def Draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)
