'''
    File name: main.py
    Author: Ömer Ünal
    Date created: 24/05/2021
    Python Version: 3.9
    
'''

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# You can customize game by changing these values

STARTING_SPEED = 5  # 5 is recommended
SPEED_BOOST = 1.3  # 1.3 is recommended
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600  # 600,600 is recommended

# Create a screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create objects
snake = Snake()
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
score = ScoreBoard(SCREEN_HEIGHT)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
gameIsOn = True

sleepTime = 1/STARTING_SPEED
while gameIsOn:

    screen.update()
    time.sleep(sleepTime)
    snake.move()

    # If snake eats food
    if snake.head.distance(food) < 15:
        # Change the food position
        food.refresh()
        # Make snake bigger
        snake.grow()
        score.increase_score()
        # After the snake eats three foods, increase the speed.
        if score.score != 0 and score.score % 3 == 0:
            sleepTime /= SPEED_BOOST
    
    # If snake hits the walls
    if snake.head.xcor() > (SCREEN_WIDTH//2 - 20) or snake.head.xcor() < -(SCREEN_WIDTH//2 - 20) or snake.head.ycor() > (SCREEN_HEIGHT//2 - 20) or snake.head.ycor() < -(SCREEN_HEIGHT//2 - 20):
        score.game_over()
        time.sleep(2)
        score.reset()
        snake.reset()

    # If snake hits the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            time.sleep(2)
            score.reset()
            snake.reset()


screen.exitonclick()
