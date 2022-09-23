from turtle import Turtle, Screen
from scoreboard import Scoreboard, ScreenDivider
from paddle import Paddle
from ball import Ball
import time

#Defining Screen properties
game_screen = Screen()
game_screen.setup(height= 800, width = 800)
game_screen.bgcolor("black")
game_screen.title("@GHMS Pong's Game")
game_screen.tracer(0)

# Invoking the scoreboard
scoreboard = Scoreboard()

#Invoking the dashed screen divider
screen_divider = ScreenDivider()

#Invoking the paddles
paddle_1 = Paddle((-350,0))
paddle_2 = Paddle((350,0))

#Invoking the ball
game_ball = Ball()

#Controlling the Paddles
game_screen.listen()
game_screen.onkey(paddle_1.go_down, "Down")
game_screen.onkey(paddle_1.go_up, "Up")

game_screen.onkey(paddle_2.go_up, "w")
game_screen.onkey(paddle_2.go_down, "s")


game_is_on = True

initial_ball_speed = 0.004
ball_speed = initial_ball_speed

# Game loop
while game_is_on:
    time.sleep(ball_speed)
    game_screen.update()
    game_ball.move()

    # Bouncing System
    if game_ball.ycor() >= 385 or game_ball.ycor() <= -385:
        game_ball.bounce()
    
    if (game_ball.distance(paddle_2)) <= 45 and game_ball.xcor() > 340:
        game_ball.bounce_paddle()
        ball_speed = ball_speed - ball_speed*0.15
    elif (game_ball.distance(paddle_1)) <= 45 and game_ball.xcor() < -340:
        game_ball.bounce_paddle()
        ball_speed = ball_speed - ball_speed*0.15

    # Scoring system
    if game_ball.xcor() <= -395:
        game_ball.home()
        ball_speed = initial_ball_speed
        scoreboard.score(2)

    elif game_ball.xcor() >= 395:
        game_ball.home()
        ball_speed = initial_ball_speed
        scoreboard.score(1)
    

game_screen.exitonclick()


