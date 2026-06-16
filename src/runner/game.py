import pygame

from src.runner.background import Background
from src.runner.constants import (
    FPS,
    STATE_GAME_OVER,
    STATE_MENU,
    STATE_PAUSE,
    STATE_PLAYING,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from src.runner.managers.coin_manager import CoinManager
from src.runner.managers.obstacle_manager import ObstacleManager
from src.runner.player import Player
from src.runner.sound import SoundManager
from src.runner.ui import UIManager


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('PyGame: Runner')

        self.clock = pygame.time.Clock()

        self.speed_multiplier = 1.0

        self.background = Background()
        self.player = Player()
        self.obstacle_manager = ObstacleManager(count=5)
        self.coin_manager = CoinManager(count=4)

        self.ui = UIManager()

        self.sounds = SoundManager()
        self.sounds.play_music()

        self.score = 0
        self.best_score = 0
        self.state = STATE_MENU
        self.running = True

    def run(self) -> None:
        while self.running:
            self.handle_events()

            if self.state == STATE_PLAYING:
                self.update()

            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        if self.state == STATE_MENU:
            if key in (pygame.K_RETURN, pygame.K_SPACE):
                self.reset()
                self.state = STATE_PLAYING

        elif self.state == STATE_PLAYING:
            if key == pygame.K_p:
                self.state = STATE_PAUSE
            if key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                if self.player.jump():
                    self.sounds.play_jump()

        elif self.state == STATE_PAUSE:
            if key == pygame.K_p:
                self.state = STATE_PLAYING

        elif self.state == STATE_GAME_OVER:
            if key == pygame.K_r:
                self.reset()
                self.state = STATE_PLAYING

            if key == pygame.K_ESCAPE:
                self.state = STATE_MENU

    def update(self) -> None:
        self.speed_multiplier += 0.0003
        self.background.update(self.speed_multiplier)
        self.player.update()
        self.obstacle_manager.update(self.speed_multiplier)
        self.coin_manager.update(self.speed_multiplier)
        self.check_collisions()

    def update_best_score(self) -> None:
        if self.score > self.best_score:
            self.best_score = self.score

    def check_collisions(self) -> None:
        player_hitbox = self.player.get_hitbox()
        if self.obstacle_manager.has_collision_with(player_hitbox):
            self.sounds.play_hit()
            self.update_best_score()
            self.state = STATE_GAME_OVER
            return
        collected_coins = self.coin_manager.collect_collided(player_hitbox)
        if collected_coins > 0:
            self.score += collected_coins
            self.sounds.play_coin()

    def draw(self) -> None:
        self.background.draw(self.screen)

        if self.state == STATE_MENU:
            self.ui.draw_menu(self.screen)
            return

        self.coin_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        self.player.draw(self.screen)

        self.ui.draw_score(
            screen=self.screen,
            score=self.score,
            best_score=self.best_score,
            speed_multiplier=self.speed_multiplier,
        )

        if self.state == STATE_PAUSE:
            self.ui.draw_pause(self.screen)

        if self.state == STATE_GAME_OVER:
            self.ui.draw_game_over(
                screen=self.screen,
                score=self.score,
                best_score=self.best_score,
                best_speed=f'{self.speed_multiplier:.1f}',
            )

    def reset(self) -> None:
        self.player.reset()
        self.obstacle_manager.reset()
        self.coin_manager.reset()
        self.score = 0
        self.speed_multiplier = 1.0
