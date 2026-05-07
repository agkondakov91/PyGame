import pygame

from src.runner.assets import load_animation
import src.runner.constants as const


class Player:
    def __init__(self) -> None:
        self.images = self.load_images()
        self.animation_index = 0.0
        self.image = self.images[int(self.animation_index)]
        self.rect = self.image.get_rect()
        self.start_x = 120
        self.rect.bottomleft = (self.start_x, const.GROUND_Y)
        self.min_player_x = self.start_x - const.PLAYER_MOVE_LIMIT
        self.max_player_x = self.start_x + const.PLAYER_MOVE_LIMIT
        self.is_jumping = False
        self.vertical_speed = 0

    def load_images(self) -> list[pygame.Surface]:
        file_names = [
            f'player_right_{number}.png'
            for number in range(1, const.ANIMATION_FRAMES_COUNT + 1)
        ]
        return load_animation(file_names, const.PLAYER_SCALE)

    def handle_input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= const.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += const.PLAYER_SPEED
        if self.rect.x < self.min_player_x:
            self.rect.x = self.min_player_x
        if self.rect.x > self.max_player_x:
            self.rect.x = self.max_player_x

    def jump(self) -> None:
        if not self.is_jumping:
            self.vertical_speed += const.JUMP_SPEED
            self.is_jumping = True

    def update_gravity(self) -> None:
        self.vertical_speed += const.GRAVITY
        self.rect.y += self.vertical_speed
        if self.rect.bottom >= const.GROUND_Y:
            self.rect.bottom = const.GROUND_Y
            self.vertical_speed = 0
            self.is_jumping = False

    def update_animation(self) -> None:
        self.animation_index += const.ANIMATION_SPEED
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.image = self.images[int(self.animation_index)]

    def update(self) -> None:
        self.handle_input()
        self.update_gravity()
        self.update_animation()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def get_hitbox(self) -> pygame.Rect:
        return self.rect.inflate(*const.PLAYER_HITBOX_INFLATE)

    def reset(self) -> None:
        self.rect.bottomleft = (self.start_x, const.GROUND_Y)
        self.vertical_speed = 0
        self.is_jumping = False
        self.animation_index = 0.0
        self.image = self.images[int(self.animation_index)]