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
        
        Game = Prazen(self.Screen)

        while self.Running:
            # Deltatime
            Now = pygame.time.get_ticks()
            Timestep = (Now - self.LastFrameTime) / 1000
            self.LastFrameTime = Now

            Game.SetFps(self.Clock.get_fps())

            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    self.Running = False
                elif Event.type == pygame.VIDEORESIZE:
                    # Update the screen size when the window is resized
                    screen_width, screen_height = Event.size
                    self.Screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.DOUBLEBUF, vsync=1)
                    Game.OnWindowResize(screen_width, screen_height)

            Game.OnUpdate(Timestep)

            pygame.display.flip()

            self.Clock.tick()

        pygame.quit()

    def GetFps(self) -> float:
        return self.Clock.get_fps()

if __name__ == "__main__":
    app = App()
    app.Run()