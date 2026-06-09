import pygame
import random

from src.runner.assets import load_image_with_size
import src.runner.constants as const


class Coin:
    def __init__(self) -> None:
        self.image = load_image_with_size('coin.png', const.COIN_SIZE)
        self.rect = self.image.get_rect()
        self.reset()


    def reset(self) -> None:
        self.rect.left = const.WINDOW_WIDTH + random.randint(
            const.COIN_MAX_DISTANCE,
            const.COIN_MAX_DISTANCE
        )
        self.rect.y = random.randint(const.COIN_MIN_HEIGHT, const.COIN_MAX_HEIGHT)


    def update(self, speed_multiplier: float = 1.0) -> None:
        self.rect.x -= int(const.COIN_SPEED * speed_multiplier)

        if self.rect.right < 0:
            self.reset()


    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


    def get_hitbox(self) -> pygame.Rect:
        return self.rect.inflate(*const.COIN_HITBOX_INFLATE)