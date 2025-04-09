from .Event import Event, EventType

class MouseButtonEvent(Event):
    def __init__(self, button):
        super().__init__()

        self.Button = button
    
    def GetName(self):
        return f'MouseButtonEvent: {self.Button}'
    
class MouseButtonPressedEvent(MouseButtonEvent):
    def __init__(self, x, y, button):
        super().__init__(button)
        self.Type = EventType.MouseButtonPressed
        
        self.x = x
        self.y = y

    def GetName(self):
        return f'MouseButtonPressedEvent: {self.Button} ({self.x}, {self.y})'
    
class MouseButtonReleasedEvent(MouseButtonEvent):
    def __init__(self, x, y, button):
        super().__init__(button)
        self.Type = EventType.MouseButtonReleased

        self.x = x
        self.y = y

    def GetName(self):
        return f'MouseButtonReleasedEvent: {self.Button} ({self.x}, {self.y})'
    
class MouseMovedEvent(Event):
    def __init__(self, x, y):
        super().__init__()
        self.Type = EventType.MouseMoved

        self.x = x
        self.y = y

    def GetName(self):
        return f'MouseMoveEvent: {self.x}, {self.y}'
    
class MouseScrolledEvent(Event):
    def __init__(self, xOffset, yOffset):
        super().__init__()
        self.Type = EventType.MouseScrolled

        self.xOffset = xOffset
        self.yOffset = yOffset

    def GetName(self):
        return f'MouseScrolledEvent: {self.xOffset}, {self.yOffset}'