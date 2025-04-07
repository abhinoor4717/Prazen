import pygame
from Log import *

from Camera import Camera
from Player import Player
from Text import Text

class Prazen:
    def __init__(self, screen: pygame.Surface) -> None:
        self.Screen = screen

        self.Camera = Camera(0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])

        self.Player = Player(0,10,10,20, self.Screen)
        self.FPS = 0

        self.PlayerPosText = Text(f'Player pos: ({self.Player.x}, {self.Player.y})', self.Player.x-30,self.Player.y-30, 50)
        self.FpsText = Text(f'FPS: {int(self.FPS)}', 30, 10, 20)

    def OnWindowResize(self, w, h):
        self.Camera.OnWindowResize(w, h)
    def SetFps(self, fps):
        self.FPS = fps

    def OnUpdate(self, dt) -> None:
        self.Screen.fill("black")

        self.PlayerPosText.Update(f'Player pos: ({self.Player.x}, {self.Player.y})', self.Player.x, self.Player.y - 30, self.Screen)
        self.FpsText.Update(f'FPS: {int(self.FPS)}', None, None, self.Screen)

        self.Player.Move(dt)
        self.Player.Draw(self.Camera)

        self.Camera.Move(dt)

    def DrawGrid(self):
        cellSize = 100

        # Get camera position and screen size
        startX = int(self.Camera.x / cellSize) * cellSize - cellSize  # Adjust the starting point
        startY = int(self.Camera.y / cellSize) * cellSize - cellSize  # Adjust the starting point

        # Calculate screen width and height based on the camera's current view
        screenWidth = self.Camera.width
        screenHeight = self.Camera.height

        # Determine the grid bounds (with some extra space)
        endX = startX + screenWidth + cellSize * 2
        endY = startY + screenHeight + cellSize * 2

        # Loop through the grid and draw cells
        for x in range(startX, endX, cellSize):
            for y in range(startY, endY, cellSize):
                pygame.draw.rect(self.Screen, (128, 128, 128), (x, y, cellSize, cellSize), 1)  # Draw grid cell outline