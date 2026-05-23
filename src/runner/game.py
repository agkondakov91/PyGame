import pygame

from src.runner.background import Background
from src.runner.coin import Coin
from src.runner.constants import FPS, WINDOW_WIDTH, WINDOW_HEIGHT
from src.runner.obstacle import Obstacle
from src.runner.player import Player


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pygame: Runner')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 56)
        self.small_font = pygame.font.Font(None, 36)
        self.background = Background()
        self.player = Player()
        self.obstacle = Obstacle()
        self.coin = Coin()
        self.score = 0
        self.state = 'playing'
        self.running = True


    def run(self) -> None:
        while self.running:
            self.handle_events()
            if self.state == "playing":
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
        if self.state == "playing":
            if key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                self.player.jump()
        if self.state == "game_over":
            if key == pygame.K_r:
                self.reset()


    def update(self) -> None:
        self.background.update()
        self.player.update()
        self.obstacle.update()
        self.coin.update()
        self.check_collisions()


    def check_collisions(self) -> None:
        player_hitbox = self.player.get_hitbox()
        obstacle_hitbox = self.obstacle.get_hitbox()
        coin_hitbox = self.coin.get_hitbox()
        if player_hitbox.colliderect(obstacle_hitbox):
            self.state = "game_over"
        if player_hitbox.colliderect(coin_hitbox):
            self.score += 1
            self.coin.reset()


    def draw(self) -> None:
        self.background.draw(self.screen)
        self.coin.draw(self.screen)
        self.obstacle.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_score()
        if self.state == "game_over":
            self.draw_game_over()


    def draw_score(self) -> None:
        score_text = self.small_font.render(f"Score: {self.score}", True, "white")
        self.screen.blit(score_text, (20, 20))


    def draw_game_over(self) -> None:
        game_over_text = self.font.render("Game Over", True, "white")
        game_over_rect = game_over_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
        )
        restart_text = self.small_font.render("Press R to restart", True, "white")
        restart_rect = restart_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60),
        )
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(restart_text, restart_rect)


    def reset(self) -> None:
        self.player.reset()
        self.obstacle.reset()
        self.coin.reset()
        self.score = 0
        self.state = "playing"