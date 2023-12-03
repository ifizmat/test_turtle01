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

@dataclass
class Row_Squares():
    """Data type Row of Squares"""
    x: int = 0
    y: int = 0
    square: Square = field(default = Square)
    amount: int = 0
    interval: int = 0

def draw_row(turt: turtle.Turtle, row: Row_Squares):
    turt.goto(row.x, row.y)
    for col in range(row.amount):
        # square = Square(size = 60, fill_color = "white")
        if col % 2 == 0:
            row.square.fill_color = "black"
        else:
            row.square.fill_color = "white"
        
        row.square.x = row.x + col * (row.interval + row.square.size)
        row.square.y = 0
        draw_square(turt, row.square)

def draw_square(turt: turtle.Turtle, square: Square):
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
    square2 = Square(x = -100, y = -50, size = 8, fill_color = "white")

    scr.setup(1440, 780, 1, 0)
    tr.hideturtle()
    tr.speed(0)

    draw_square(tr, square1)
    draw_square(tr, square2)
    row = Row_Squares(x = -50, y = 0, square = square2, amount = 15, interval = 2)    
    draw_row(tr, row)
    turtle.done()
