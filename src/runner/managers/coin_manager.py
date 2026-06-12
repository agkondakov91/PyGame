import pygame

from src.runner.coin import Coin
from src.runner.constants import (
    COIN_SPAWN_MAX_GAP,
    COIN_SPAWN_MIN_GAP,
)
from src.runner.managers.base_manager import BaseObjectManager


class CoinManager(BaseObjectManager):
    def __init__(self, count: int) -> None:
        super().__init__(
            count=count,
            min_gap=COIN_SPAWN_MIN_GAP,
            max_gap=COIN_SPAWN_MAX_GAP,
        )

    def create_object(self) -> Coin:
        return Coin()

    def collect_collided(self, player_hitbox: pygame.Rect) -> int:
        collected_count = 0

        for coin in self.objects:
            if player_hitbox.colliderect(coin.get_hitbox()):
                collected_count += 1
                coin.reset(self.spawn_manager.get_next_x())

        return collected_count
