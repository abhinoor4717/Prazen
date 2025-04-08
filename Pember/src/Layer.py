from .Events.Event import Event

class Layer:
    def __init__(self, name):
        self.Name = name
    
    def OnAttach(self):
        pass
    def OnDetach(self):
        pass
    def OnEvent(self, event: Event):
        pass
    def OnUpdate(self, dt: float):
        pass