import pygame


class Text:
    def __init__(self, text: str, x, y, fontSize = 10):
        self.Text = text
        self.font = pygame.font.Font(None, fontSize)
        self.textSurf = self.font.render(self.Text, True, "white")
        self.textRect = self.textSurf.get_rect(topleft=(x,y))

    def SetText(self, text):
        self.Text = text
        self.textSurf = self.font.render(self.Text, True, "white")
    def SetPos(self, x, y):
        self.textRect.x = x
        self.textRect.y = y

    def Draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.textSurf, self.textRect)

    def Update(self, text: str, x: int | None, y: int | None, screen: pygame.surface.Surface):
        self.SetText(text)
        if x is None and y is None:
            pass
        elif x is None:
            self.SetPos(self.textRect.x, y)
        elif y is None:
            self.SetPos(x, self.textRect.y)
        else:
            self.SetPos(x, y)
        self.Draw(screen)