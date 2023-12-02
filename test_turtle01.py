import turtle

# https://docs-python.ru/tutorial/klassy-jazyke-python/sozdanie-sobstvennyh-tipov-dannyh-struktury/

# from turtle import *
tr = turtle.Turtle()
scr = turtle.Screen()

def square(turt, x, y, size, fillcolor):
    # turt.teleport(x, y)
    # turt.goto(x - size/2, y - size/2)
    turt.goto(x, y)

    tr.fillcolor(fillcolor)
    tr.begin_fill()
    turt.pendown()
    for _ in range(4):
        turt.forward(size)
        turt.right(90)
    
    tr.end_fill()
    turt.penup()


def axes(turt, screen):
    turt.home()
    turt.pendown()
    turt.backward(screen.window_width()/2)
    turt.forward(screen.window_width())
    turt.home()
    turt.left(90)
    turt.backward(screen.window_height()/2)
    turt.forward(screen.window_height())
    turt.penup()

def output_row_squares():
    size_square = 30
    for x in range(0, 300, size_square):
        fillcolor = None
    
        if x % (2 * size_square) == 0:
            fillcolor = "black"
        else: 
            fillcolor = "white"
        square(tr, x, 0, 30, fillcolor) 


def row_squares(turt, x0, y0, num_squares):

    for i in range(num_squares):
        x = x0 + i * (size_square + dist_x_square) 
        square(turt, x, y0, size_square, fillcolor)


def matrix_squares(turt, x0, y0, columns, rows):
    for row in range(rows):
        y = y0 + row * (size_square + dist_y_square)
        row_squares(turt, x0, y, columns)


#tr.shape("turtle")
# scr.setup(1440, 1080)
scr.setup(1440, 780, 1, 0)
tr.hideturtle()
tr.speed(0)

axes(tr, scr)

# tr.fillcolor("red")
# tr.fillcolor("black")

# output_row_squares()


num_squares = 15
x = 0
size_square = 5
dist_x_square = 3
dist_y_square = 6
fillcolor = "white"
ROWS = 8
y = 0

matrix_squares(tr, x0 = -100, y0 = -50, columns = 8, rows = 3)
# row_squares(tr, x0 = -100, y0 = -50, num_squares = 8)

turtle.done()
#print(turtle.__dir__())



















