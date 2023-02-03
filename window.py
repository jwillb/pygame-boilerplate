import pygame
import colors
from vector2 import Vector2

class Window:
    def __init__(self, TITLE="Template Window", WIDTH=1366, HEIGHT=768, FPS=60):
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__COLOR = colors.RGB(50, 50, 50)
        self.__DIMENSIONS = Vector2(WIDTH, HEIGHT)
        self.__FRAME = pygame.time.Clock()
        self.__SCREEN = pygame.display.set_mode(tuple(self.__DIMENSIONS))

        self.__SCREEN.fill(tuple(self.__COLOR))
        pygame.display.set_caption(self.__TITLE)

    def runtime(self, CALLBACK):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            RENDER_ITEMS = CALLBACK()

            for RENDER_ITEM in RENDER_ITEMS:
                self.__SCREEN.blit(RENDER_ITEM.getScreen(), RENDER_ITEM.getPOS())