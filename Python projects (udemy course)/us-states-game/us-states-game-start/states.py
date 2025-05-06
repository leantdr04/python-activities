from turtle import Turtle


class TitleState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def create_title(self, name, x_coor, y_coor):
        self.goto(x=x_coor, y=y_coor)
        self.write(name, align="center")
