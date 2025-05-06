from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
tim.shape("turtle")

tim.fd(100)
tim.setheading(90)
tim.fd(100)
tim.setheading(180)
tim.fd(100)
tim.setheading(270)
tim.fd(100)

screen.exitonclick()