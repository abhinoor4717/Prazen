import pygame, enum

from Prazen import Prazen

class Settings:
    class Window:
        WIDTH = 800
        HEIGHT = 600

class App:
    def __init__(self) -> None:

        pygame.init()

        self.Screen = pygame.display.set_mode((Settings.Window.WIDTH, Settings.Window.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Prazen")

        self.Clock = pygame.time.Clock()

        self.Running = True

        self.LastFrameTime = pygame.time.get_ticks()
    def Run(self) -> None:
        
        Game = Prazen()

        while self.Running:
            # Deltatime
            Now = pygame.time.get_ticks()
            Timestep = (Now - self.LastFrameTime) / 1000
            self.LastFrameTime = Now

            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    self.Running = False

            Game.OnUpdate(Timestep)

            pygame.display.flip()

            self.Clock.tick()

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.Run()