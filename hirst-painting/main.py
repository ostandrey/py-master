import random
from turtle import Screen
import colorgram
import turtle as t

colors = colorgram.extract('image.jpg', 30)

# def convert_color(colors):
#     color_list = []
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         color_list.append((r, g, b))
#     return color_list
#
# rgb_list = convert_color(colors)
# print(rgb_list)

color_list = [(243, 242, 240), (238, 241, 245), (245, 240, 243), (236, 243, 239), (39, 94, 140), (226, 157, 73), (239, 211,
 97), (153, 25, 59), (183, 42, 75), (217, 131, 155), (146, 96, 50), (32, 52, 78), (118, 170, 200), (153, 157,
30), (233, 89, 56), (36, 150, 65), (109, 202, 169), (204, 67, 108), (139, 210, 229), (17, 59, 125), (91, 33, 25),
              (158, 221, 176), (102, 110, 178), (22, 169, 186), (163, 193, 226), (232, 162, 171), (237, 156, 153),
              (11, 81, 110), (103, 33, 28), (96, 21, 47)]

t.colormode(255)
tur = t.Turtle()
tur.penup()

start_x = -200
start_y = -200
tur.goto(start_x, start_y)

def draw_picture():
    for row in range(10):
        for _ in range(10):
            tur.dot(25, random.choice(color_list))
            tur.forward(40)
        tur.goto(start_x, start_y + (row + 1) * 50)

draw_picture()

screen = Screen()
screen.exitonclick()