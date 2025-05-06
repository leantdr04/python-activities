import random
from turtle import Turtle, Screen

is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "cyan", "green", "blue", "purple"]
y_positions = [-150, -85, -25, 25, 85, 150]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []

for turtle_num in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_num])
    new_turtle.goto(x=-230, y=y_positions[turtle_num])
    all_turtles.append(new_turtle)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! {winning_color} turtle wins the race.")

            else:
                print(f"You Lose! {winning_color} turtle wins the race.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
