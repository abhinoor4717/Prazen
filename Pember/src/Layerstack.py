from .Layer import Layer

class Layerstack:
    def __init__(self) -> None:
        self.Layers: list[Layer] = []

    def Push(self, layer: Layer) -> None:
        self.Layers.append(layer)
        layer.OnAttach()
    def Pop(self, index = -1) -> Layer:
        l = self.Layers.pop(index)
        l.OnDetach()
        return l
    def PopLayer(self, layer: Layer) -> None:
        self.Layers.remove(layer)
        layer.OnDetach()