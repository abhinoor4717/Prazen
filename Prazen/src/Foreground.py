import pygame

from Pember import Layer
from Pember import Log
from Pember import Text

from .Player import Player

class Foreground(Layer):
    def __init__(self):
        super().__init__("Foreground")

        self.app = self.GetApplication()

        self.Player = Player(0,0,10,20, self.app.Screen)

    def OnAttach(self):
        Log.INFO(f'{self.Name} layer attached')
    def OnDetach(self):
        Log.INFO(f'{self.Name} layer detached')
    def OnUpdate(self, dt):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_LSHIFT]:
            if keys[pygame.K_0]:
                self.Player.x = 0
                self.Player.y = 0
        else:
            if keys[pygame.K_0]:
                self.app.Camera.x = 0
                self.app.Camera.y = 0
        self.app.Screen.fill("black")
        self.app.Camera.Move(dt)
        self.Player.Move(dt)
        self.Player.Draw(self.app.Camera)
    def GetApplication(self):
        from .Prazen import Prazen
        return Prazen.GetInstance()
