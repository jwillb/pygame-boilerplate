import pygame
import vector2
import colors

class GameObject:
    def __init__(self, NAME):
        self.NAME = NAME
        self.COLOR = colors.RGB(255, 255, 255)
        self.SCALE = vector2.Vector2(10, 10)

    def getScreen(self):
        return self.__SCREEN

    def refresh(self):
        self.__SCREEN = pygame.Surface(tuple(self.SCALE), pygame.SRCALPHA, 32)
        self.__SCREEN.fill(tuple(self.COLOR))

class Sprite(GameObject):
    """
    Generic Sprite Class
    """
    def __init__(self, NAME="Sprite"):
        super().__init__(NAME)
        self.POSITION = vector2.Vector2(0, 0)
        self.COLOR = colors.RGB(255, 255, 255)
        self.VELOCITY = vector2.Vector2(0, 0)
        self.refresh()