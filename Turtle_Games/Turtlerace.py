from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtle=[]

for turtleindex in range(0,6):
    new_turtle =Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtleindex])
    new_turtle.goto(x=-290, y= y_positions[turtleindex])
    all_turtle.append(new_turtle)


is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
          if turtle.xcor()>290:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
                random_distance = random.randint(0,10)
                turtle.forward(random_distance)

screen.exitonclick()