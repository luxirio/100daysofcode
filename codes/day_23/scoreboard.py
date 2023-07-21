from tkinter import CURRENT
from turtle import Turtle

FONT = ("Courier", 24, "normal")
CURRENT_LEVEL = 0

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.goto(-280, 250)
        self.level = CURRENT_LEVEL
        self.write(f"LEVEL: {self.level}", font= FONT)
    
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", font= FONT)
    
    def game_over(self):
        self.home()
        self.write("GAME OVER.", font= FONT, align="center")


