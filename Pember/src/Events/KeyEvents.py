from .Event import Event, EventType

class KeyEvent(Event):
    def __init__(self, keycode, scancode, mods):
        super().__init__()

        self.Keycode = keycode
        self.Scancode = scancode
        self.Mods = mods

    def GetName(self):
        return "KeyEvent"
    
class KeyPressEvent(KeyEvent):
    def __init__(self, keycode, scancode, mods, repeatCount):
        super().__init__(keycode, scancode, mods)
        self.Type = EventType.KeyPressed

        self.RepeatCount = repeatCount

    def GetName(self):
        return f'KeyPressedEvent: {self.Keycode} ({self.RepeatCount} repeats)'

class KeyReleaseEvent(KeyEvent):
    def __init__(self, keycode, scancode, mods):
        super().__init__(keycode, scancode, mods)
        self.Type = EventType.KeyReleased

    def GetName(self):
        return f'KeyReleasedEvent: {self.Keycode}'
    

