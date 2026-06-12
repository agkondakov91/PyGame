from typing import Protocol

import pygame

from src.runner.spawn import SpawnManager


class ManagedObject(Protocol):
    rect: pygame.Rect

    def reset(self, x: int) -> None:
        pass

    def update(self, speed_multiplier: float = 1.0) -> None:
        pass

    def is_outside_screen(self) -> bool:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def get_hitbox(self) -> pygame.Rect:
        pass


class BaseObjectManager:
    def __init__(self, count: int, min_gap: int, max_gap: int) -> None:
        self.spawn_manager = SpawnManager(min_gap, max_gap)

        self.objects = [self.create_object() for _ in range(count)]

        self.reset()

    def create_object(self) -> ManagedObject:
        raise NotImplementedError("Subclasses must implement create_object()")

    def reset(self) -> None:
        self.spawn_manager.reset()

        for game_object in self.objects:
            game_object.reset(self.spawn_manager.get_next_x())

    def update(self, speed_multiplier: float) -> None:
        for game_object in self.objects:
            game_object.update(speed_multiplier)

            if game_object.is_outside_screen():
                game_object.reset(self.spawn_manager.get_next_x())

    def draw(self, screen: pygame.Surface) -> None:
        for game_object in self.objects:
            game_object.draw(screen)
