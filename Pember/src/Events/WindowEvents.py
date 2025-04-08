from .Event import Event, EventType

class WindowClosedEvent(Event):
    def __init__(self):
        super().__init__()
        self.Type = EventType.WindowClosed

    def GetName(self):
        return "WindowClosedEvent"

class WindowResizedEvent(Event):
    def __init__(self, w, h):
        super().__init__()
        self.Type = EventType.WindowResized

        self.Width = w
        self.Height = h

    def GetName(self):
        return f'WindowResizedEvent: {self.Width}, {self.Height}'

class WindowFocusedEvent(Event):
    def __init__(self):
        super().__init__()
        self.Type = EventType.WindowFocused

    def GetName(self):
        return "WindowFocusedEvent"

class WindowLostFocusEvent(Event):
    def __init__(self):
        super().__init__()
        self.Type = EventType.WindowLostFocus

    def GetName(self):
        return "WindowLostFocusEvent"