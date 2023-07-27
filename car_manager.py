from turtle import Turtle
from car import Car
import random
# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 0

    def create_car(self):
        if random.randint(1, 6) == 1:
            # new_car = Turtle()
            # new_car.penup()
            # new_car.shape("square")
            # new_car.shapesize(stretch_wid=1, stretch_len=2)
            # new_car.color(random.choice(COLORS))
            # random_y = random.randint(-250, 250)
            # new_car.goto(300, random_y)
            # self.all_cars.append(new_car)
            self.all_cars.append(Car())

    def move_car(self):
        for car in self.all_cars:
            car.move(self.speed)
            # car.backward(self.speed + STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

