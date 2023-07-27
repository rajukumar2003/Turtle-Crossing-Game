import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# import colorgram
#
#
# def get_colors():
#     colors = []
#     color_objects = colorgram.extract(f="colors.png", number_of_colors=8)
#     for color in color_objects:
#         colors.append(tuple(color.rgb))
#     return colors
#
#
# print(get_colors())

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing")
screen.bgcolor("light grey")
screen.colormode(255)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with the car

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            screen.exitonclick()
            game_is_on = False

    # Reached top edge

    if player.ycor() == 280:
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level_up()
