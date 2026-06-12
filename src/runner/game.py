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


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("PyGame: Runner")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 56)
        self.small_font = pygame.font.Font(None, 36)

        self.speed_multiplier = 1.0

        self.background = Background()
        self.player = Player()

        self.obstacle_manager = ObstacleManager(count=5)
        self.coin_manager = CoinManager(count=3)

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

    def draw_menu(self) -> None:
        title_text = self.font.render("Runner Game", True, "white")
        title_rect = title_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80),
        )

        start_text = self.small_font.render(
            "Press Enter or Space to start",
            True,
            "white",
        )
        start_rect = start_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
        )

        controls_text = self.small_font.render(
            "Move: A/D or Arrows    Jump: W/Up/Space",
            True,
            "white",
        )
        controls_rect = controls_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50),
        )

        self.screen.blit(title_text, title_rect)
        self.screen.blit(start_text, start_rect)
        self.screen.blit(controls_text, controls_rect)

    def draw_pause(self) -> None:
        pause_text = self.font.render("Pause", True, "white")
        pause_rect = pause_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
        )
        continue_text = self.small_font.render("Press P to continue", True, "white")
        continue_rect = continue_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
        )
        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(continue_text, continue_rect)

    def draw(self) -> None:
        self.background.draw(self.screen)
        if self.state == STATE_MENU:
            self.draw_menu()
            return
        self.coin_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_score()
        if self.state == STATE_PAUSE:
            self.draw_pause()
        if self.state == STATE_GAME_OVER:
            self.draw_game_over()

    def draw_score(self) -> None:
        score_text = self.small_font.render(f"Score: {self.score}", True, "white")
        best_text = self.small_font.render(f"Best: {self.best_score}", True, "white")
        speed_text = self.small_font.render(
            f"Speed: {self.speed_multiplier:.1f}", True, "white"
        )

        self.screen.blit(score_text, (20, 20))
        self.screen.blit(best_text, (20, 50))
        self.screen.blit(speed_text, (20, 80))

    def draw_game_over(self) -> None:
        game_over_text = self.font.render("Game Over", True, "white")
        game_over_rect = game_over_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80),
        )

        score_text = self.small_font.render(f"Final score: {self.score}", True, "white")
        score_rect = score_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20),
        )

        best_text = self.small_font.render(
            f"Best score: {self.best_score}",
            True,
            "white",
        )
        best_rect = best_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
        )

        restart_text = self.small_font.render("Press R to restart", True, "white")
        restart_rect = restart_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70),
        )

        menu_text = self.small_font.render("Press Esc to menu", True, "white")
        menu_rect = menu_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 115),
        )

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(best_text, best_rect)
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(menu_text, menu_rect)

    def reset(self) -> None:
        self.player.reset()
        self.obstacle_manager.reset()
        self.coin_manager.reset()
        self.score = 0
        self.speed_multiplier = 1.0
