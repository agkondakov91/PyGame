import random

import pygame

from src.runner.assets import load_image_with_size
from src.runner.constants import (
    COIN_HITBOX_INFLATE,
    COIN_MAX_HEIGHT,
    COIN_MIN_HEIGHT,
    COIN_SIZE,
    COIN_SPEED,
)


class Coin:
    def __init__(self) -> None:
        self.image = load_image_with_size('coin.png', COIN_SIZE)
        self.rect = self.image.get_rect()

    def reset(self, x: int) -> None:
        self.rect.left = x
        self.rect.y = random.randint(COIN_MIN_HEIGHT, COIN_MAX_HEIGHT)

    def update(self, speed_multiplier: float = 1.0) -> None:
        self.rect.x -= int(COIN_SPEED * speed_multiplier)

    def is_outside_screen(self) -> bool:
        return self.rect.right < 0

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def get_hitbox(self) -> pygame.Rect:
        return self.rect.inflate(*COIN_HITBOX_INFLATE)
