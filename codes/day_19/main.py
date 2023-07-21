
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen_width = 500
screen.setup(height = 400, width = screen_width)

colors = ["blue", "yellow", "green", "black", "grey", "teal", "red"]
y_positions = [-100, -70, -40, -10, 20, 50, 80]
user_bet = screen.textinput(title = "Make a bet!", prompt= "Which turtle will win the race? Choose a color: ")
all_turtles = []

race_is_on = False

for turtle_index in range(7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    
    new_turtle.setposition(x = -230, y =y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet in colors:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        rand_distance = randint(0,15)
        turtle.forward(rand_distance)
        
        if turtle.pos()[0] >= (screen_width/2 - 35):
            winner_color = (turtle.color()[0])
            print(f"The winner is {winner_color}!")
            race_is_on = False
            
if user_bet == winner_color:
    print("You have chose the right one! Congrats!")
else: 
    print(f"Sorry, you have picked {user_bet}, but it was another call.")
screen.exitonclick()