from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.go_to_start()

    def move_up(self):
        self.forward(5)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
