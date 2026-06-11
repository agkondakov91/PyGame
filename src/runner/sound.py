import pygame

from src.runner.assets import SOUNDS_DIR


class SoundManager:
    def __init__(self) -> None:
        self.jump_sound = pygame.mixer.Sound(SOUNDS_DIR / "jump.mp3")
        self.coin_sound = pygame.mixer.Sound(SOUNDS_DIR / "coin.mp3")
        self.hit_sound = pygame.mixer.Sound(SOUNDS_DIR / "hit.mp3")

        self.jump_sound.set_volume(0.5)
        self.coin_sound.set_volume(0.5)
        self.hit_sound.set_volume(0.5)

        self.music_path = SOUNDS_DIR / "music.mp3"

    def play_jump(self) -> None:
        self.jump_sound.play()

    def play_coin(self) -> None:
        self.coin_sound.play()

    def play_hit(self) -> None:
        self.hit_sound.play()

    def play_music(self) -> None:
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def stop_music(self) -> None:
        pygame.mixer.music.stop()
