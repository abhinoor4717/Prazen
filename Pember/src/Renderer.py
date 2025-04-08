import pygame

from .Camera import Camera

class Renderer:

    Camera = None
    Screen = None

    @staticmethod
    def Init(screen: pygame.surface.Surface) -> None:
        Renderer.Camera = Camera(0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])
        Renderer.Screen = screen

    @staticmethod
    def DrawRect(rect: pygame.rect.Rect | tuple, color: pygame.color.Color, static=False, width=0):
        if isinstance(rect, tuple):
            rect = pygame.Rect(*rect)
        if not static:
            pos = Renderer.Camera.project((rect.x, rect.y))
            pygame.draw.rect(Renderer.Screen, color, (*pos, rect.width, rect.height), width=width)
            return
        
        pygame.draw.rect(Renderer.Screen, color, rect, width=width)

    @staticmethod
    def DrawText(textSurf, textRect, static=False) -> None:
        draw_pos = (textRect.x, textRect.y) if static else Renderer.Camera.project((textRect.x, textRect.y))
        Renderer.Screen.blit(textSurf, draw_pos)

    @staticmethod
    def DrawImage(surf, rect, static=False) -> None:
        draw_pos = (rect.x, rect.y) if static else Renderer.Camera.project((rect.x, rect.y))
        Renderer.Screen.blit(surf, draw_pos)

    