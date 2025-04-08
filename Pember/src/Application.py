import pygame
from .Layerstack import Layerstack

class Settings:
    class Window:
        WIDTH = 800
        HEIGHT = 600
    
class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Create a new instance if it doesn't already exist
            cls._instances[cls] = super(SingletonBase, cls).__new__(cls)
        return cls._instances[cls]


class Application(SingletonBase):
    def __init__(self) -> None:
        # Prevent __init__ from running more than once
        if not hasattr(self, 'initialized'):
            pygame.init()

            self.Screen = pygame.display.set_mode((Settings.Window.WIDTH, Settings.Window.HEIGHT), pygame.RESIZABLE)
            pygame.display.set_caption("Prazen")
            self.Clock = pygame.time.Clock()

            self.Running = True
            self.LastFrameTime = pygame.time.get_ticks()

            self.Layerstack = Layerstack()

            self.initialized = True  # Flag to mark initialization as complete

    def Run(self) -> None:
        while self.Running:
            # Deltatime
            Now = pygame.time.get_ticks()
            Timestep = (Now - self.LastFrameTime) / 1000
            self.LastFrameTime = Now

            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    self.Running = False
                elif Event.type == pygame.VIDEORESIZE:
                    # Update the screen size when the window is resized
                    screen_width, screen_height = Event.size
                    self.Screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.DOUBLEBUF, vsync=1)

            for layer in self.Layerstack.Layers:
                layer.OnUpdate(Timestep)

            pygame.display.flip()
            self.Clock.tick()

        pygame.quit()

    @classmethod
    def GetInstance(cls):
        # Return the instance of the class (the singleton instance)
        return cls._instances.get(cls)
