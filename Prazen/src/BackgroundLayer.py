import pygame
import Pember
from Pember import Log

class BackgroundLayer(Pember.Layer):
    def __init__(self):
        super().__init__("Background")

        self.app = self.GetApplication()

        self.Map = Pember.Image("Prazen/src/Resources/Assets/World-prazen.png", 0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])

    def OnAttach(self):
        Log.INFO(F'{self.Name} layer attached!')
    
    def OnEvent(self, event):
        if event.Type == Pember.EventType.WindowResized:
            self.Map.Resize(event.Width, event.Height)

    def OnUpdate(self, dt):
        self.app.Screen.fill("black")

        self.Map.Draw()


    def GetApplication(self):
        from .Prazen import Prazen
        return Prazen.GetInstance()