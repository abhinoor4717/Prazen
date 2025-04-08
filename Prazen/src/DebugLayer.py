import pygame

import Pember

class DebugLayer(Pember.Layer):
    def __init__(self):
        super().__init__("Debug")
        from Prazen.src.Prazen import Prazen
        self.app: Prazen = self.GetApplication()
        
        self.FPS = 0.0
        self.FpsText = Pember.Text(f'FPS: {self.FPS}', 0,0, 20)
        self.counter = 0
    
    def OnUpdate(self, dt):
        # self.app.Screen.fill("black")
        self.FPS = self.app.Clock.get_fps()

        self.FpsText.Update(f'FPS: {int(self.FPS)}', None, None, self.app.Screen)


    def GetApplication(self):
        from .Prazen import Prazen
        return Prazen.GetInstance()