import pygame
from Log import *

from Camera import Camera

class Prazen:
    def __init__(self, screen: pygame.Surface) -> None:
        self.Screen = screen

        self.Camera = Camera(-100, 100, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])

        self.PlayerX = 0
        self.PlayerY = 0

    def OnWindowResize(self, w, h):
        self.Camera.OnWindowResize(w, h)

    def OnUpdate(self, dt) -> None:
        self.Screen.fill("black")
        self.DrawGrid()

        self.Camera.Move(dt)

        playerPos = self.Camera.TranslatePos(self.PlayerX, self.PlayerY)
        pygame.draw.rect(self.Screen, "red", (playerPos.x, playerPos.y, 10, 20))
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