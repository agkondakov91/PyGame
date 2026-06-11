import pygame

from src.runner.assets import load_image_with_size
from src.runner.constants import (
    GROUND_Y,
    OBSTACLE_HITBOX_INFLATE,
    OBSTACLE_SIZE,
    OBSTACLE_SPEED,
)


class Obstacle:
    def __init__(self) -> None:
        self.image = load_image_with_size("obstacle.png", OBSTACLE_SIZE)
        self.rect = self.image.get_rect()

    def reset(self, x: int) -> None:
        self.rect.left = x
        self.rect.bottom = GROUND_Y + 10

    def update(self, speed_multiplier: float = 1.0) -> None:
        self.rect.x -= int(OBSTACLE_SPEED * speed_multiplier)

    def is_outside_screen(self) -> bool:
        return self.rect.right < 0

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def get_hitbox(self) -> pygame.Rect:
        return self.rect.inflate(*OBSTACLE_HITBOX_INFLATE)
