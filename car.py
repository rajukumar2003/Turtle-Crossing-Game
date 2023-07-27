from turtle import Turtle
import random

SHAPE = ((-5, 0), (-3, 0), (-3, 5), (3, 5), (3, 0), (5, 0), (5, -4), (3, -4),
         (3, -5), (2, -5), (2, -4), (-2, -4), (-2, -5), (-3, -5), (-3, -4), (-5, -4))


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = [(244, 244, 244), (131, 85, 68), (25, 28, 52), (49, 24, 23), (172, 143, 130),
                       (91, 14, 16), (249, 212, 75), (220, 83, 43)]
        self.penup()
        self.left(90)
        self.set_car_shape()
        self.color("black")
        self.fillcolor(random.choice(self.colors))
        self.goto(x=300, y=random.randint(-220, 220))

    def set_car_shape(self):
        self.getscreen().register_shape(name="car", shape=SHAPE)
        self.shape("car")
        self.shapesize(stretch_wid=4, stretch_len=2)

    def move(self, speed):
        self.setx(self.xcor() - 8-speed)

