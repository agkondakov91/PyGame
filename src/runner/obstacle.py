import pygame
import random

from src.runner.assets import load_image_with_size
import src.runner.constants as const


class Obstacle:
    def __init__(self) -> None:
        self.image = load_image_with_size('obstacle.png', const.OBSTACLE_SIZE)
        self.rect = self.image.get_rect()
        self.reset()


    def reset(self) -> None:
        self.rect.left = const.WINDOW_WIDTH + random.randint(
            const.OBSTACLE_MIN_DISTANCE,
            const.OBSTACLE_MAX_DISTANCE
        )
        self.rect.bottom = const.GROUND_Y + 10


    def update(self) -> None:
        self.rect.x -= const.OBSTACLE_SPEED

        if self.rect.right < 0:
            self.reset()


    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


    def get_hitbox(self) -> pygame.Rect:
        return self.rect.inflate(*const.OBSTACLE_HITBOX_INFLATE)