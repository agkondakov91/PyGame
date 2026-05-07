import pygame

from src.runner.background import Background
from src.runner.constants import FPS, WINDOW_HEIGHT, WINDOW_WIDTH
from src.runner.player import Player


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Player test")

    clock = pygame.time.Clock()

    background = Background()
    player = Player()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                    player.jump()

        background.update()
        player.update()

        background.draw(screen)
        player.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()