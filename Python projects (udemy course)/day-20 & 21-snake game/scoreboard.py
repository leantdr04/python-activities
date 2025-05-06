from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
SCORE_PLACEMENT = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCORE_PLACEMENT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y= 20)
        self.write("GAME OVER..oof", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
