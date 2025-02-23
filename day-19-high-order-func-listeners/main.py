from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()

def move_forward():
    tur.forward(10)

def move_backward():
    tur.backward(10)

def rotate_counterclockwise():
    tur.right(5)

def rotate_clockwise():
    tur.left(5)

def clear_drawing():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

def exit_drawing():
    screen.bye()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="q", fun=exit_drawing)
screen.exitonclick()