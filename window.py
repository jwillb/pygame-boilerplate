import pygame
import colors
import vector2
import construct
from vector2 import Vector2

class Window(construct.GameObject):
    def __init__(self, NAME="Template Window", WIDTH=1366, HEIGHT=768, FPS=60):
        super().__init__(NAME)
        self.__FPS = FPS
        self.COLOR = colors.RGB(50, 50, 50)
        self.SCALE = Vector2(WIDTH, HEIGHT)
        self.__FRAME = pygame.time.Clock()
        self.__SCREEN = pygame.display.set_mode(tuple(self.SCALE))

        self.__SCREEN.fill(tuple(self.COLOR))
        pygame.display.set_caption(self.NAME)

    def runtime(self, CALLBACK):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            RENDER_ITEMS = CALLBACK()

            self.__SCREEN.fill(tuple(self.COLOR))

            for RENDER_ITEM in RENDER_ITEMS:
                RENDER_ITEM.refresh()
                self.__SCREEN.blit(RENDER_ITEM.getScreen(), tuple(RENDER_ITEM.POSITION))

            self.__FRAME.tick(self.__FPS)
            pygame.display.flip()

def game():
    MYSQUARE = construct.Sprite()
    MYSQUARE.POSITION = vector2.Vector2(30, 30)
    MYSQUARE.SCALE = vector2.Vector2(100, 100)
    return (MYSQUARE,)

if __name__ == "__main__":
    Window().runtime(game)