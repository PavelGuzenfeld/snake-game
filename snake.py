import numpy as np
from scipy.spatial import distance

DIRECTIONS = {
    "UP": np.array([0, 1]),
    "DOWN": np.array([0, -1]),
    "LEFT": np.array([-1, 0]),
    "RIGHT": np.array([1, 0])
}


class Snake:

    def __init__(self, a_size, a_start_position, a_segment_dimensions, a_bounds, a_io):
        self.segment_dimensions = np.array(a_segment_dimensions)
        self.io = a_io
        self.direction = DIRECTIONS["RIGHT"]
        self.bounds = a_bounds
        head = np.array(a_start_position)
        self.snake_segments = [head]
        for _ in range(a_size):
            next_segment = self.snake_segments[-1] + self.segment_dimensions * self.direction
            self.snake_segments.append(next_segment)
        self.io.listen(a_up=self.up, a_down=self.down, a_left=self.left, a_right=self.right)

    def grow(self):
        next_segment = self.snake_segments[-1] + self.segment_dimensions * self.direction
        self.snake_segments.append(next_segment)

    def move(self):
        head = self.snake_segments[-1] + self.segment_dimensions * self.direction
        one_before_head = 1
        iterations = len(self.snake_segments) - one_before_head
        for itr in range(iterations):
            self.snake_segments[itr] = self.snake_segments[itr + 1]
        self.snake_segments[-1] = head

    def draw(self):
        for segment in self.snake_segments:
            x = segment[0]
            y = segment[1]
            self.io.draw(x, y)

    def clear(self):
        self.io.clear()

    def up(self):
        if not np.array_equal(self.direction, DIRECTIONS["DOWN"]):
            self.direction = DIRECTIONS["UP"]

    def down(self):
        if not np.array_equal(self.direction, DIRECTIONS["UP"]):
            self.direction = DIRECTIONS["DOWN"]

    def left(self):
        if not np.array_equal(self.direction, DIRECTIONS["RIGHT"]):
            self.direction = DIRECTIONS["LEFT"]

    def right(self):
        if not np.array_equal(self.direction, DIRECTIONS["LEFT"]):
            self.direction = DIRECTIONS["RIGHT"]

    def is_food_found(self, a_food):
        head = self.snake_segments[-1]
        d = distance.euclidean(head, a_food)
        print(d)
        if d < 20:
            return True
        else:
            return False

    def is_out_of_bounds(self):
        head = self.snake_segments[-1]
        print(head)
        print(self.bounds)
        x_condition = abs(head[0] - self.bounds[0]) < 5 or head[0] < 0
        y_condition = abs(head[1] - self.bounds[1]) < 5 or head[1] < 0
        return x_condition or y_condition

    def is_self_collided(self):
        head = self.snake_segments[-1]
        for segment in self.snake_segments[:-1]:
            equal = np.all(np.equal(head, segment))
            if equal:
                return True
            else:
                return False
