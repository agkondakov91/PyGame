import pygame

from pathlib import Path
from src.runner.constants import WINDOW_WIDTH, WINDOW_HEIGHT

BASE_DIR = Path(__file__).resolve().parents[2]
IMAGES_DIR = BASE_DIR / 'assets' / 'images'

def load_image(file_name: str, scale: int = 1) -> pygame.Surface:
    image = pygame.image.load(IMAGES_DIR / file_name).convert_alpha()
    if scale == 1:
        return image
    new_size = (
        image.get_width() * scale,
        image.get_height() * scale
    )
    return pygame.transform.scale(image, new_size)


def load_image_with_size(file_name: str, size: tuple[int, int]) -> pygame.Surface:
    image = pygame.image.load(IMAGES_DIR / file_name).convert_alpha()
    return pygame.transform.scale(image, size)


def load_background(file_name: str) -> pygame.Surface:
    image = pygame.image.load(IMAGES_DIR / file_name).convert()
    return pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))


def load_animation(file_names: list[str], scale: int = 1) -> list[pygame.Surface]:
    return [
        load_image(filename, scale)
        for filename in file_names
    ]