import pygame

from Pember import Layer
from Pember import Log
from Pember import Text
from Pember import Renderer

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

        Renderer.Camera.Move(dt)

        self.Player.Move(dt)
        self.Player.Draw()

    def GetApplication(self):
        from .Prazen import Prazen
        return Prazen.GetInstance()
