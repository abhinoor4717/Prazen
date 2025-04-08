from enum import Enum, auto
from abc import ABC, abstractmethod

class EventType(Enum):
    Null = auto()
    WindowClosed = auto()
    WindowResized = auto()
    WindowFocused = auto()
    WindowLostFocus = auto()
    WindowMoved = auto()
    
    KeyPressed = auto()
    KeyReleased = auto()

    MouseButtonPressed = auto()
    MouseButtonReleased = auto()
    MouseMoved = auto()
    MouseScrolled = auto()

class Event(ABC):
    def __init__(self):
        self.Name: str
        self.Type: EventType = EventType.Null
        self.Handled = False
    
    @abstractmethod
    def GetName(self) -> str:
        pass

    def __str__(self):
        return self.GetName()