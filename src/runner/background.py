import pygame

from src.runner.assets import load_background
from src.runner.constants import BACKGROUND_SPEED, WINDOW_WIDTH

class Background:
    def __init__(self):
        self.image = load_background('background.png')
        self.x = 0

    def update(self) -> None:
        self.x -= BACKGROUND_SPEED
        if self.x < -WINDOW_WIDTH:
            self.x = 0

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + WINDOW_WIDTH, 0))