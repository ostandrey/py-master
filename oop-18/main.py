from turtle import Turtle, Screen
import turtle as t
import random

turt = Turtle()

# def draw_square():
#     for _ in range(4):
#         turt.forward(100)
#         turt.right(90)
#
# draw_square()

# def draw_dash():
#     for _ in range(10):
#         turt.pendown()
#         turt.forward(10)
#         turt.penup()
#         turt.forward(10)
#
# draw_dash()

"""Draw shapes by sides"""
# colors = ["#c1f091", "#651927", "#f6e5a9", "#fc0fb7", "#4fb1c3", "#7205ea"]
"""Variant 1"""
# def draw_shapes(shapes = 7):
#     angle = 3
#
#     for _ in range(shapes):
#         for _ in range(angle):
#             turt.right(360/angle)
#             turt.forward(50)
#         angle += 1
#
# draw_shapes()

# """Variant 2"""
# def draw_shapes(shape_sides):
#     angle = 360 / shape_sides
#     for _ in range(shape_sides):
#         turt.forward(50)
#         turt.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     turt.color(random.choice(colors))
#     draw_shapes(shape_side_n)

"""Random walk"""
"""Variant 1"""
# ways = ["forward", "left", "right", "backward"]
#
# def random_walk():
#     turt.pensize(10)
#     turt.speed(100)
#     turt.color(colors[random.randint(0, len(colors) - 1)])
#
#     step = 20
#     way = random.choice(ways)
#
#     if way == "forward":
#         turt.forward(step)
#     elif way == "left":
#         turt.left(90)
#         turt.forward(step)
#     elif way == "right":
#         turt.right(90)
#         turt.forward(step)
#     elif way == "backward":
#         turt.back(step)
#
# for _ in range(50):
#     random_walk()


""" Variant 2"""
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

# ways = [0, 90, 180, 270]
# def random_walk():
#     turt.pensize(10)
#     turt.speed(100)
#     turt.color(random_color())
#
#
#     turt.forward(20)
#     turt.setheading(random.choice(ways))
#
# for _ in range(50):
#     random_walk()


"""Spirograph"""
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turt.speed(100)
        turt.color(random_color())
        turt.circle(80)
        turt.setheading(turt.heading() + size_of_gap)



draw_spirograph(5)

screen = Screen()
screen.exitonclick()