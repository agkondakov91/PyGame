import random

from src.runner.constants import SPAWN_START_X


class SpawnManager:
    def __init__(self, min_gap: int, max_gap: int) -> None:
        self.min_gap = min_gap
        self.max_gap = max_gap
        self.next_x = SPAWN_START_X

    def get_next_x(self) -> int:
        gap = random.randint(self.min_gap, self.max_gap)
        self.next_x += gap
        return self.next_x

    def reset(self) -> None:
        self.next_x = SPAWN_START_X
