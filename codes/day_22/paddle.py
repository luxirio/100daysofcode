from turtle import Turtle

class Paddle(Turtle):

    #Creating a segment of paddles
    def __init__(self, position):
        super().__init__()
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))
 