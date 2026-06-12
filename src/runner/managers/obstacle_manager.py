import pygame

from src.runner.constants import (
    OBSTACLE_SPAWN_MAX_GAP,
    OBSTACLE_SPAWN_MIN_GAP,
)
from src.runner.managers.base_manager import BaseObjectManager
from src.runner.obstacle import Obstacle


class ObstacleManager(BaseObjectManager):
    def __init__(self, count: int) -> None:
        super().__init__(
            count=count,
            min_gap=OBSTACLE_SPAWN_MIN_GAP,
            max_gap=OBSTACLE_SPAWN_MAX_GAP,
        )

    def create_object(self) -> Obstacle:
        return Obstacle()

    def has_collision_with(self, player_hitbox: pygame.Rect) -> bool:
        for obstacle in self.objects:
            if player_hitbox.colliderect(obstacle.get_hitbox()):
                return True

        return False
