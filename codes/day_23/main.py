import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Invoking Player:
player = Player()

#Invoking CarManager
car = CarManager()

#Invoking Scoreboard
score = Scoreboard()

#Key Association
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    #Create and move car objects
    car.create()
    car.move_cars()

    #Detect Collisions
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #Detect when player crossed the line:
    if player.ycor() >= 275:
        player.goto(0,-280)
        car.update_speed()
        score.update_score()


screen.exitonclick()