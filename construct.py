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

class Sprite(GameObject):
    """
    Generic Sprite Class
    """
    def __init__(self, NAME="Sprite"):
        super().__init__(NAME)
        self.POSITION = vector2.Vector2(0, 0)
        self.COLOR = colors.RGB(255, 255, 255)
        self.VELOCITY = vector2.Vector2(0, 0)
        self.SPEED = 10
        self.WASD_HOOK = False

    def refresh(self, SCREEN):
        if self.WASD_HOOK:
            KEY_PRESSES = pygame.key.get_pressed()
            if KEY_PRESSES[pygame.K_d] == 1:
                self.POSITION.X += self.SPEED
            if KEY_PRESSES[pygame.K_a] == 1:
                self.POSITION.X -= self.SPEED
            if KEY_PRESSES[pygame.K_w] == 1:
                self.POSITION.Y -= self.SPEED
            if KEY_PRESSES[pygame.K_s] == 1:
                self.POSITION.Y += self.SPEED

        self.POSITION.Y += self.VELOCITY.Y
        self.POSITION.X += self.VELOCITY.X

        pygame.draw.rect(SCREEN, tuple(self.COLOR), pygame.Rect(self.POSITION.X, self.POSITION.Y, self.SCALE.X, self.SCALE.Y))