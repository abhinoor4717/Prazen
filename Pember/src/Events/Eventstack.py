from .Event import Event

class Eventstack:
    def __init__(self):
        self.Events: list[Event] = []

    def Push(self, event: Event) -> None:
        self.Events.append(event)
    
    def Pop(self, index = -1) -> Event:
        return self.Events.pop(index)
    
    def Remove(self, event: Event) -> None:
        self.Events.remove(event)
    
    def IsEmpty(self) -> bool:
        return len(self.Events) == 0

    def Clear(self):
        self.Events.clear()

    def __iter__(self):
        return iter(self.Events)
    