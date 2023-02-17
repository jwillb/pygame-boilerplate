import pygame
import colors
import vector2
import construct
import time
from vector2 import Vector2

class Window(construct.GameObject):
    def __init__(self, NAME="Template Window", WIDTH=1366, HEIGHT=768, FPS=60):
        super().__init__(NAME)
        self.__FPS = FPS
        self.COLOR = colors.RGB(50, 50, 50)
        self.SCALE = Vector2(WIDTH, HEIGHT)
        self.__FRAME = pygame.time.Clock()
        self.__START = time.time()
        self.__SCREEN = pygame.display.set_mode(tuple(self.SCALE))

        self.__SCREEN.fill(tuple(self.COLOR))
        pygame.display.set_caption(self.NAME)

    def runtime(self, CALLBACK):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            RENDER_ITEMS = CALLBACK(self.SCALE, time.time() - self.__START, self.__FRAME.get_fps())

            self.__SCREEN.fill(tuple(self.COLOR))

            for RENDER_ITEM in RENDER_ITEMS:
                RENDER_ITEM.refresh(self.__SCREEN)

            self.__FRAME.tick(self.__FPS)
            pygame.display.flip()

# test

if __name__ == "__main__":
    MYSQUARE = construct.Sprite()
    MYSQUARE.POSITION = vector2.Vector2(30, 30)
    MYSQUARE.SCALE = vector2.Vector2(100, 100)
    MYSQUARE.VELOCITY = vector2.Vector2(0, 0)
    MYSQUARE.WASD_HOOK = True

    LAST_JUMP = 0

    def game(SCALE, FRAME, FPS):
        global LAST_JUMP

        KEY_PRESSES = pygame.key.get_pressed()
        if KEY_PRESSES[pygame.K_SPACE] == 1 and FRAME - LAST_JUMP > 0.5:
            MYSQUARE.VELOCITY.Y -= 40
            LAST_JUMP = FRAME
        if MYSQUARE.POSITION.Y + MYSQUARE.SCALE.Y >= SCALE.Y and MYSQUARE.VELOCITY.Y >= 0:
            MYSQUARE.VELOCITY.Y = 0
            MYSQUARE.POSITION = Vector2(MYSQUARE.POSITION.X, SCALE.Y - MYSQUARE.SCALE.Y)
        else:
            MYSQUARE.VELOCITY.Y += 3.2

        return (MYSQUARE,)

    Window().runtime(game)