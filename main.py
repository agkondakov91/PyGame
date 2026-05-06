import pygame

from src.runner.background import Background
from src.runner.constants import FPS, WINDOW_HEIGHT, WINDOW_WIDTH


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Background test")

    clock = pygame.time.Clock()
    background = Background()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background.update()
        background.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()