# import turtle
#
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

# import prettytable
from prettytable import PrettyTable
table = PrettyTable()

table.add_column(
    'Pokemon Name', ["Pickachu", "Squirtle", "Charmander"],
)
table.add_column(
    'Type', ["Electric", "Water", "Fire"],
)

table.align = 'l'
print(table)