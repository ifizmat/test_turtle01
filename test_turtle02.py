from dataclasses import dataclass, field
import turtle

# https://docs-python.ru/tutorial/klassy-jazyke-python/sozdanie-sobstvennyh-tipov-dannyh-struktury/

tr = turtle.Turtle()
scr = turtle.Screen()

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


square1 = Square(0, 0, 20)
square2 = Square(x = -100, y = -50, size = 60, fill_color = "black")

def draw_square(turt, square: Square):
    turt.goto(square.x, square.y)

    tr.fillcolor(square.fill_color)
    tr.begin_fill()
    turt.pendown()
    for _ in range(4):
        turt.forward(square.size)
        turt.right(90)
    
    tr.end_fill()
    turt.penup()

draw_square(tr, square1)
draw_square(tr, square2)

turtle.done()
