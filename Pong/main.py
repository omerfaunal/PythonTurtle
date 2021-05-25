"""
    Project name: Pong
    Author: Ömer Ünal
    Date created: 24/05/2021
    Python Version: 3.9
    
"""

from scoreboard import ScoreBoard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

PLAYER_LEFT_NAME = "Player1"
PLAYER_RIGHT_NAME = "Player2"

# You can customize the game settings by changing the values.
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # 800,600 is recommended
RIGHT_PLAYER_UP_KEY = "Up"
RIGHT_PLAYER_DOWN_KEY = "Down"
LEFT_PLAYER_UP_KEY = "w"
LEFT_PLAYER_DOWN_KEY = "s"
GAME_SPEED = 20  # 20 is recommended
RIGHT_PADDLE_SIZE = 5  # 5 is recommended
LEFT_PADDLE_SIZE = 5  # 5 is recommended
RIGHT_PADDLE_SPEED = 20  # 20 is recommended
LEFT_PADDLE_SPEED = 20  # 20 is recommended
SPEED_BOOST = 10  # 10 is recommended
IS_CHEAT_ENABLED_RIGHT = False
IS_CHEAT_ENABLED_LEFT = False

# Do not modify here
SCREEN_WIDTH //= 2
SCREEN_HEIGHT //= 2

# We created our screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)
screen.tracer(0)

# We created our paddles with given features and and we placed it on the right and left sides of the screen.
lPaddle = Paddle((-SCREEN_WIDTH + 50, 0), LEFT_PADDLE_SIZE, LEFT_PADDLE_SPEED)
rPaddle = Paddle((SCREEN_WIDTH - 50, 0), RIGHT_PADDLE_SIZE, RIGHT_PADDLE_SPEED)
# We created our ball object and created customized scoreboard
ball = Ball(GAME_SPEED)
scoreBoard = ScoreBoard(SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_LEFT_NAME, PLAYER_RIGHT_NAME)

screen.listen()
screen.onkeypress(rPaddle.go_up, RIGHT_PLAYER_UP_KEY)
screen.onkeypress(rPaddle.go_down, RIGHT_PLAYER_DOWN_KEY)
screen.onkeypress(lPaddle.go_up, LEFT_PLAYER_UP_KEY)
screen.onkeypress(lPaddle.go_down, LEFT_PLAYER_DOWN_KEY)

gameIsOn = True
while gameIsOn:

    screen.update()
    time.sleep(1 / ball.move_speed_game)
    ball.move()

    # Changes direction if the ball hits the top or bottom edge of the screen
    if ball.ycor() > (SCREEN_HEIGHT - 20) or ball.ycor() < (-SCREEN_HEIGHT + 20):
        ball.bounce_y()

    # If the right player misses the ball
    if ball.xcor() > (SCREEN_WIDTH - 20):
        # If cheat is activated, bounce the ball back
        if IS_CHEAT_ENABLED_RIGHT:
            ball.bounce_x()
        # Reset the ball position to 0,0 and increase the left side's point
        else:
            ball.reset_position()
            scoreBoard.left_scored()

    # If the left player misses the ball
    if ball.xcor() < (-SCREEN_WIDTH + 20):
        # If cheat is activated, bounce the ball back
        if IS_CHEAT_ENABLED_LEFT:
            ball.bounce_x()
        # Reset the ball position to 0,0 and increase the left side's point
        else:
            ball.reset_position()
            scoreBoard.right_scored()

    # If the right player hits the ball, bounce the ball back and increase ball speed for more fun
    if (rPaddle.ycor() - RIGHT_PADDLE_SIZE * 10) <= ball.ycor() <= (
            rPaddle.ycor() + RIGHT_PADDLE_SIZE * 10) and ball.xcor() > (SCREEN_WIDTH - 80):
        ball.bounce_x()
        ball.increase_speed(SPEED_BOOST)

    # If the left player hits the ball, bounce the ball back and increase ball speed for more fun
    if (lPaddle.ycor() - LEFT_PADDLE_SIZE * 10) <= ball.ycor() <= (
            lPaddle.ycor() + LEFT_PADDLE_SIZE * 10) and ball.xcor() < (-SCREEN_WIDTH + 80):
        ball.bounce_x()
        ball.increase_speed(SPEED_BOOST)

screen.exitonclick()
