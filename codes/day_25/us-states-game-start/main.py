import turtle
import pandas as pd

screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

game_is_on = True

#Loading the data
states_data = pd.read_csv("50_states.csv")

#Gathering the states
list_of_states = list(states_data.state)

#Transforming the states into a list
list_of_states = [state.lower() for state in list_of_states]


def write_state(x,y, state_name):
    writer = turtle.Turtle()
    writer.color("black")
    writer.penup()
    writer.ht()
    writer.goto(x,y)
    writer.write(f"{state_name}")
states_game = []
while len(states_game) < 50:

    answer_state = screen.textinput(title = f"Guess the US States {len(states_game)}/{50}", prompt="What's the name of the next U.S. State?: ").lower()
    
    if answer_state.lower() in list_of_states:
        states_game.append(answer_state.lower())
        print("You've got one!")
        x_state_coord = int(states_data[states_data["state"] == answer_state.title()].x)
        y_state_coord = int(states_data[states_data["state"] == answer_state.title()].y)
        write_state(x = x_state_coord, y = y_state_coord, state_name = answer_state.title())

    elif answer_state.lower() == "exit":
        break




turtle.mainloop()