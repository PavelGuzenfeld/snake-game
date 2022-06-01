from turtle import Screen
from turtle import Turtle


class Writable:
    """Writes stuff on canvas"""
    def __init__(self, a_color, a_align, a_font):
        self.align = a_align
        self.font = a_font
        self.graphic = Turtle()
        self.graphic.color(a_color)
        self.graphic.penup()
        self.graphic.hideturtle()
        self.graphic.speed("fastest")

    def set_position(self, a_x, a_y):
        self.graphic.goto(a_x, a_y)

    def write(self, a_text):
        self.graphic.write(arg=a_text, align=self.align, font=self.font)

    def clear(self):
        self.graphic.clear()


class Drawable:
    """Drawing and clearing graphic"""
    def __init__(self, a_graphic, a_color, a_scale):
        self.graphic = Turtle(a_graphic)
        self.graphic.color(a_color)
        self.graphic.penup()
        self.graphic.hideturtle()
        self.graphic.shapesize(a_scale, a_scale)
        self.graphic.speed("fastest")

    def draw(self, a_x, a_y):
        """draws graphic"""
        self.graphic.goto(a_x, a_y)
        self.graphic.stamp()
        Screen().update()

    def clear(self):
        """clears graphic"""
        self.graphic.clear()


class Controls:
    """listens to arrow key stroke events"""
    @staticmethod
    def listen(a_up, a_down, a_left, a_right):
        Screen().listen()
        Screen().onkey(a_up, "Up")
        Screen().onkey(a_down, "Down")
        Screen().onkey(a_left, "Left")
        Screen().onkey(a_right, "Right")


class Canvas:
    """opens a canvas to draw game graphics"""
    def __init__(self, a_width, a_height):
        Screen().bgcolor("black")
        Screen().setup(width=a_width, height=a_height)
        Screen().title("Snake")
        Screen().setworldcoordinates(llx=0, lly=0, urx=a_width, ury=a_height)
        Screen().tracer(0)

    @staticmethod
    def close():
        Screen().exitonclick()


class SnakeIO(Drawable, Controls):
    """Aggregates game IO"""
    def __init__(self, a_segment_graphic, a_color, a_scale=1):
        Drawable.__init__(self, a_segment_graphic, a_color, a_scale)
