import pygame

from .Renderer import Renderer

_FONT_CACHE = {}

def get_font(size):
    if size not in _FONT_CACHE:
        _FONT_CACHE[size] = pygame.font.Font(None, size)
    return _FONT_CACHE[size]

class Text:
    def __init__(self, text: str, x: int, y: int, fontSize: int = 10):
        self.Text = text
        self.font = get_font(fontSize)
        self.textSurf = self.font.render(self.Text, True, "white")
        self.textRect = self.textSurf.get_rect(topleft=(x, y))

    def SetText(self, text: str):
        if self.Text != text:
            self.Text = text
            self.textSurf = self.font.render(self.Text, True, "white")
            self.textRect = self.textSurf.get_rect(topleft=(self.textRect.x, self.textRect.y))

    def SetPos(self, x: int, y: int):
        self.textRect.x = x
        self.textRect.y = y

    def Draw(self, static: bool = False) -> None:
        Renderer.DrawText(self.textSurf, self.textRect, static)

    def Update(self, text: str, x: int | None = None, y: int | None = None, static: bool = False):
        self.SetText(text)
        if x is not None or y is not None:
            self.SetPos(
                x if x is not None else self.textRect.x,
                y if y is not None else self.textRect.y
            )
        self.Draw(static)