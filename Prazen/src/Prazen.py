import pygame

from Pember import Application
from Pember import Renderer

from .Camera import Camera

from .Foreground import Foreground
from .DebugLayer import DebugLayer
from .BackgroundLayer import BackgroundLayer

class Prazen(Application):
    def __init__(self):
        super().__init__()

        self.Layerstack.Push(BackgroundLayer())
        self.Layerstack.Push(Foreground())
        self.Layerstack.Push(DebugLayer())
