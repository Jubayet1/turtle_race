from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Color You Want")

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(220, 190)
tim.setheading(270)
tim.pendown()
tim.forward(370)

is_race_on = False

coordinate = [(-200, 160), (-200, 100), (-200, 40), (-200, -20), (-200, -80), (-200, -140)]
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

for num in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color[num])
    turtle.goto(coordinate[num])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        tile = randint(0, 10)
        turtle.forward(tile)
        if turtle.xcor() > 220:
            is_race_on = False
            if turtle.color() == user_bet:
                print(f'You Won')
            else:
                print(f'You choose {user_bet} and the winner is {turtle.color()}')

screen.exitonclick()
