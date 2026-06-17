from src.runner.constants import STATE_GAME_OVER, STATE_MENU, STATE_PAUSE, STATE_PLAYING


class GameSession:
    def __init__(self) -> None:
        self.state = STATE_MENU
        self.score = 0
        self.best_score = 0
        self.speed_multiplier = 1.0

    def is_menu(self) -> bool:
        return self.state == STATE_MENU

    def is_playing(self) -> bool:
        return self.state == STATE_PLAYING

    def is_paused(self) -> bool:
        return self.state == STATE_PAUSE

    def is_game_over(self) -> bool:
        return self.state == STATE_GAME_OVER

    def start_game(self) -> None:
        self.score = 0
        self.speed_multiplier = 1.0
        self.state = STATE_PLAYING

    def pause(self) -> None:
        self.state = STATE_PAUSE

    def resume(self) -> None:
        self.state = STATE_PLAYING

    def finish_game(self) -> None:
        self.update_best_score()
        self.state = STATE_GAME_OVER

    def go_to_menu(self) -> None:
        self.state = STATE_MENU

    def add_score(self, point: int) -> None:
        self.score += point

    def increase_speed(self) -> None:
        self.speed_multiplier += 0.0003

    def update_best_score(self) -> None:
        if self.score > self.best_score:
            self.best_score = self.score
