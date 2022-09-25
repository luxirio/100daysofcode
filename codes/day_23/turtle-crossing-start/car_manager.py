from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1,8)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len= 2, stretch_wid= 1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(250,random.randint(-250,250))
            self.all_cars.append(new_car)


    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.move_speed)
    
    def update_speed(self):
        self.move_speed += MOVE_INCREMENT
        