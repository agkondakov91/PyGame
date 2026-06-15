import pygame

from src.runner.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class UIManager:
    def __init__(self) -> None:
        self.font = pygame.font.Font(None, 56)
        self.small_font = pygame.font.Font(None, 36)

    def draw_menu(self, screen: pygame.Surface) -> None:
        title_text = self.font.render('Runner Game', True, 'white')
        title_rect = title_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80),
        )

        start_text = self.small_font.render(
            'Press Enter or Space to start',
            True,
            'white',
        )
        start_rect = start_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
        )

        controls_text = self.small_font.render(
            'Move: A/D or Arrows    Jump: W/Up/Space',
            True,
            'white',
        )
        controls_rect = controls_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50),
        )

        pause_text = self.small_font.render(
            'Pause: P',
            True,
            'white',
        )
        pause_rect = pause_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90),
        )

        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(controls_text, controls_rect)
        screen.blit(pause_text, pause_rect)

    def draw_score(
        self, screen: pygame.Surface, score: int, best_score: int, speed_multiplier
    ) -> None:
        score_text = self.small_font.render(f'Score: {score}', True, 'white')
        best_text = self.small_font.render(f'Best: {best_score}', True, 'white')
        speed_text = self.small_font.render(
            f'Speed: {speed_multiplier:.1f}', True, 'white'
        )

        screen.blit(score_text, (20, 20))
        screen.blit(best_text, (20, 50))
        screen.blit(speed_text, (20, 80))

    def draw_pause(self, screen: pygame.Surface) -> None:
        pause_text = self.font.render('Pause', True, 'white')
        pause_rect = pause_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
        )
        continue_text = self.small_font.render('Press P to continue', True, 'white')
        continue_rect = continue_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
        )
        screen.blit(pause_text, pause_rect)
        screen.blit(continue_text, continue_rect)

    def draw_game_over(
        self, screen: pygame.Surface, score: int, best_score: int
    ) -> None:
        game_over_text = self.font.render('Game Over', True, 'white')
        game_over_rect = game_over_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80),
        )

        score_text = self.small_font.render(f'Final score: {score}', True, 'white')
        score_rect = score_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20),
        )

        best_text = self.small_font.render(
            f'Best score: {best_score}',
            True,
            'white',
        )
        best_rect = best_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20),
        )

        restart_text = self.small_font.render('Press R to restart', True, 'white')
        restart_rect = restart_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70),
        )

        menu_text = self.small_font.render('Press Esc to menu', True, 'white')
        menu_rect = menu_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 115),
        )

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(best_text, best_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(menu_text, menu_rect)
