import pygame

WIDTH, HEIGHT = 900,500
BG_COLOR = (255,255,255)
FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test Game")

def draw_window():
    WINDOW.fill(BG_COLOR)
    pygame.display.update()

def main():
    run = True

    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()