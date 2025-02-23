from turtle import Turtle, Screen
import random

is_race_on = False
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
start_x = -350
start_y = [-70, -40, -10, 20, 50, 80]

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")

user_bet = screen.textinput(title="Your bet", prompt="Which turtle will win? Enter a color: ")

turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=start_x, y=start_y[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win!{winning_color} is the winner!")
            else:
                print(f"You`ve lose( {winning_color} wins!")
        turtle.forward(random.randint(1, 10))

screen.exitonclick()
