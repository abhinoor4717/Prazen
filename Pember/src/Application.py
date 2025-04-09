import pygame
from .Layerstack import Layerstack

from .Renderer import Renderer

from .Events.Event import Event
from .Events.WindowEvents import *
from .Events.MouseEvents import *
from .Events.KeyEvents import *
from .Events.Eventstack import Eventstack
from .Log  import *

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

            Renderer.Init(self.Screen)

            self.Eventstack = Eventstack()
            self.Layerstack = Layerstack()

            self.initialized = True  # Flag to mark initialization as complete

    def Run(self) -> None:
        
        while self.Running:
            # Deltatime
            Now = pygame.time.get_ticks()
            Timestep = (Now - self.LastFrameTime) / 1000
            self.LastFrameTime = Now

            self.Eventstack.Clear()

            for Event in pygame.event.get():
                # Window Events
                if Event.type == pygame.QUIT:
                    self.Eventstack.Push(WindowClosedEvent())
                    self.Running = False
                elif Event.type == pygame.VIDEORESIZE:
                    # Update the screen size when the window is resized
                    w, h = Event.size
                    event = WindowResizedEvent(w, h)
                    # TRACE(event)
                    self.Eventstack.Push(event)
                    self.Screen = pygame.display.set_mode((w, h), pygame.RESIZABLE | pygame.DOUBLEBUF, vsync=1)
                    Renderer.Camera.OnWindowResize(w, h)
                elif Event.type == pygame.WINDOWFOCUSGAINED:
                    self.Eventstack.Push(WindowFocusedEvent())
                elif Event.type == pygame.WINDOWFOCUSLOST:
                    self.Eventstack.Push(WindowLostFocusEvent())
                elif Event.type == pygame.WINDOWMOVED:
                    self.Eventstack.Push(WindowMovedEvent(Event.x, Event.y))
                
                elif Event.type == pygame.MOUSEBUTTONDOWN:
                    if Event.button not in (4, 5):
                        self.Eventstack.Push(MouseButtonPressedEvent(*Event.pos, Event.button))
                elif Event.type == pygame.MOUSEBUTTONUP:
                    if Event.button not in (4, 5):
                        self.Eventstack.Push(MouseButtonReleasedEvent(*Event.pos, Event.button))
                elif Event.type == pygame.MOUSEMOTION:
                    self.Eventstack.Push(MouseMovedEvent(*Event.pos))
                elif Event.type == pygame.MOUSEWHEEL:
                    self.Eventstack.Push(MouseScrolledEvent(Event.x, Event.y))
                
                elif Event.type == pygame.KEYDOWN:
                    self.Eventstack.Push(KeyPressEvent(Event.key, Event.scancode, Event.mod, 1))
                elif Event.type == pygame.KEYUP:
                    self.Eventstack.Push(KeyReleaseEvent(Event.key, Event.scancode, Event.mod))
                    
                    

            for layer in self.Layerstack:
                if not self.Eventstack.IsEmpty():
                    for event in self.Eventstack:
                        if not event.Handled:
                            layer.OnEvent(event)
                layer.OnUpdate(Timestep)

            pygame.display.flip()
            self.Clock.tick()

        pygame.quit()

    @classmethod
    def GetInstance(cls):
        # Return the instance of the class (the singleton instance)
        return cls._instances.get(cls)
