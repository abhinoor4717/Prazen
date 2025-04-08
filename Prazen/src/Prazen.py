import pygame

from Pember import Application

# from .Log import *
from .Camera import Camera
# from .Player import Player
# from .Text import Text
# from .Image import Image

from .Foreground import Foreground
from .DebugLayer import DebugLayer

# class Prazen:
#     def __init__(self, screen: pygame.Surface) -> None:
#         self.Screen = screen

#         self.Camera = Camera(0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])

#         self.Player = Player(0,10,10,20, self.Screen)
#         self.FPS = 0
#         self.DisplayFps = self.FPS

#         # self.PlayerPosText = Text(f'Player pos: ({self.Player.x}, {self.Player.y})', self.Player.x-30,self.Player.y-30, 50)
#         self.FpsText = Text(f'FPS: {int(self.DisplayFps)}', 30, 10, 20)
#         self.counter = 0.0

#         self.Val = Image("src/Resources/Assets/valorant.jpg", 100, 100, 300, 600)

#     def OnWindowResize(self, w, h):
#         self.Camera.OnWindowResize(w, h)
#         self.Val.rect.x = int(w/2)
#         self.Val.rect.y = int(h/2)
        
#     def SetFps(self, fps):
#         self.FPS = fps

#     def OnUpdate(self, dt) -> None:

#         if self.counter >= 0.5:
#             self.DisplayFps = self.FPS
#             self.counter = 0
#         self.counter += dt

#         self.Screen.fill("black")

#         # self.PlayerPosText.Update(f'Player pos: ({self.Player.x}, {self.Player.y})', self.Player.x, self.Player.y - 30, self.Screen)
#         self.FpsText.Update(f'FPS: {int(self.DisplayFps)}', None, None, self.Screen)
        
#         self.Val.Draw(self.Screen)

#         self.Player.Move(dt)
#         self.Player.Draw(self.Camera)

#         self.Camera.Move(dt)

class Prazen(Application):
    def __init__(self):
        super().__init__()
        self.Camera = Camera(0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])
        # self.Screen.fill("black")
        self.Layerstack.Push(Foreground())
        self.Layerstack.Push(DebugLayer())
