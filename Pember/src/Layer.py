class Layer:
    def __init__(self, name):
        self.Name = name
    
    def OnAttach(self):
        pass
    def OnDetach(self):
        pass
    def OnUpdate(self, dt: float):
        pass