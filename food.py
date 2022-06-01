from random import randint


class Food:
    """Snake food placement logic"""

    def __init__(self, a_width, a_height, a_boundary, a_io):
        self.io = a_io
        self.width = a_width
        self.height = a_height
        self.boundary = a_boundary
        self.pos_x = 0
        self.pos_y = 0

    def place(self):
        """places food at random location"""
        self.pos_x = randint(self.boundary, self.width - self.boundary)
        self.pos_y = randint(self.boundary, self.width - self.boundary)
        self.io.draw(self.pos_x, self.pos_y)

    def remove(self):
        """removes all the food"""
        self.io.clear()

    def pos_list(self):
        """returns food location as list"""
        return [self.pos_x, self.pos_y]

# TODO: add capability to have food at multiple locations
