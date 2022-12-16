import pygame
import random
from enum import Enum
class SnakeGame():
    
    def __init__(self):

        self.WIDTH, self.HEIGHT = 900,500
        self.BG_COLOR = (255,255,255)
        self.FPS = 60

        self.DISPLAY = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.draw_window()

    def draw_window(self):
        self.DISPLAY.fill(self.BG_COLOR)
        pygame.draw.rect(self.DISPLAY, (255,0,0), pygame.Rect(self.WIDTH/2 - 30 ,self.HEIGHT/2 - 30, 60,60))
        pygame.display.update()

    def game_loop(self):
        run = True

        clock = pygame.time.Clock()
    
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw_window()
            pygame.display.set_caption(f'Current FPS: {str(clock.get_fps())}')

        pygame.quit()

if __name__ == "__main__":

    pygame.init()

    game = SnakeGame()
    game.game_loop()
     