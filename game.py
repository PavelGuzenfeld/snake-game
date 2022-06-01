from snake_io import SnakeIO, Drawable, Writable, Canvas
from snake import Snake
from food import Food
from score_board import ScoreBoard
from time import sleep


class Game:
    def __init__(self):
        screen_width = 600
        screen_height = 600

        snake_size = 2
        snake_start_position = [300, 300]
        snake_segment_dimensions = [25, 25]
        snake_bounds = [screen_width, screen_height]
        snake_graphic = "square"
        snake_color = "white"

        food_graphic = "circle"
        food_color = "blue"
        food_placement_boundary = 10
        food_scale = 0.5

        score_board_start_score = 0
        score_board_message = "Score: "
        score_board_color = "white"
        score_board_color_alignment = "left"
        score_board_color_font = ("Arial", 20, "normal")

        self.canvas = Canvas(a_width=screen_width, a_height=screen_height)

        self.snake = Snake(
            a_size=snake_size,
            a_start_position=snake_start_position,
            a_segment_dimensions=snake_segment_dimensions,
            a_bounds=snake_bounds,
            a_io=SnakeIO(a_segment_graphic=snake_graphic, a_color=snake_color)
        )

        self.food = Food(
            a_width=screen_width,
            a_height=screen_height,
            a_boundary=food_placement_boundary,
            a_io=Drawable(food_graphic, food_color, food_scale)
        )

        self.score_board = ScoreBoard(
            start_score=score_board_start_score,
            a_message=score_board_message,
            a_io=Writable(score_board_color, score_board_color_alignment, score_board_color_font)
        )

        self.game_over_message = Writable(score_board_color, "center", score_board_color_font)
        self.game_over_message.set_position(screen_width / 2, screen_height / 2)

    def run(self):
        self.food.place()
        while True:
            try:
                self.snake.draw()
                is_found = self.snake.is_food_found(self.food.pos_list())
                if is_found:
                    self.snake.grow()
                    self.food.remove()
                    self.food.place()
                    self.score_board.update_score(1)
                    self.score_board.display()

                if self.snake.is_out_of_bounds() or self.snake.is_self_collided():
                    self.game_over_message.write("Game Over!")
                    sleep(2)
                    break

                self.snake.move()
                sleep(0.2)
                self.snake.clear()
            except Exception as error:
                break

# TODO: read the game settings from a settings file
# TODO: refactor exit on exceptions from main loop workaround
# TODO: refactor game over
# TODO: add levels
