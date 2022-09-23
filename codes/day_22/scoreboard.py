from turtle import Turtle, Screen, speed
import time

FONT_FAMILY = ("Arial", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0 
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.goto(0,360)
        self.write(f"Score: {self.score_1} x {self.score_2}", align= "center", font= FONT_FAMILY)

    def score(self, paddle_number):
        if paddle_number == 1:
            self.score_1 += 1
            self.clear()
            self.write(f"Score: {self.score_1} x {self.score_2}", align= "center", font= FONT_FAMILY)
            time.sleep(.5)

        else:
            self.score_2 += 1
            self.clear()
            self.write(f"Score: {self.score_1} x {self.score_2}", align= "center", font= FONT_FAMILY)
            time.sleep(.5)

class ScreenDivider(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 360)
        self.pendown()
        self.setheading(270)

        for steps in range(330, -410, -30):
            self.color("white")
            self.forward(15)
            self.color("black")
            self.forward(15)
        
        

