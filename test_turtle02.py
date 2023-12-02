from dataclasses import dataclass, field
import turtle

# https://docs-python.ru/tutorial/klassy-jazyke-python/sozdanie-sobstvennyh-tipov-dannyh-struktury/

@dataclass
class Square():
    """Data type Square"""
    x: int = 0
    y: int = 0
    size: int = 0
    color: str = "black"
    fill_color: str = "white"

    def __post_init__(self):
        # initialization attribute "area"
        self.area = self.size ** 2

class Row_Squares():
    """Data type Row of Squares"""
    x: int = 0
    y: int = 0
    square: Square = field(default = Square)
    num_squares: int = 0
    dist_squares: int = 0

def draw_square(turt, square: Square):
    turt.goto(square.x, square.y)

    turt.fillcolor(square.fill_color)
    turt.begin_fill()
    turt.pendown()
    for _ in range(4):
        turt.forward(square.size)
        turt.right(90)
    
    turt.end_fill()
    turt.penup()


if __name__ == "__main__":
    tr = turtle.Turtle()
    scr = turtle.Screen()

    square1 = Square(0, 0, 20)
    square2 = Square(x = -100, y = -50, size = 60, fill_color = "black")

    scr.setup(1440, 780, 1, 0)
    tr.hideturtle()
    tr.speed(0)

    draw_square(tr, square1)
    draw_square(tr, square2)

turtle.done()
