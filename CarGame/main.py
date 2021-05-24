import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SPEED = 10
CAR_SPEED = 5 
CAR_SPEED_INCREASE = 10
COLOR = "orange"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

racer = Player(SCREEN_HEIGHT, PLAYER_SPEED, COLOR)
car_manager = CarManager(SCREEN_WIDTH, SCREEN_HEIGHT, CAR_SPEED, CAR_SPEED_INCREASE)
scoreboard = Scoreboard(SCREEN_WIDTH,SCREEN_HEIGHT)

screen.onkeypress(racer.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car(scoreboard.level)
    car_manager.move_cars()

    if racer.ycor() > (SCREEN_HEIGHT//2 - 20):
        racer.go_back()
        scoreboard.level_up()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(racer) < 30:
            game_is_on = False
            time.sleep(2)
            screen.clear()
            scoreboard.you_are_dead()
    
screen.exitonclick()