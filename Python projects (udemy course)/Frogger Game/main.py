import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

crossy = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(crossy.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.create_cars()
    cars_manager.move()

    for car in cars_manager.all_cars:
        if crossy.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if crossy.is_finish():
        scoreboard.increase_score()
        crossy.at_start()
        cars_manager.are_speeding()


screen.exitonclick()