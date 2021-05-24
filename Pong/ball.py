from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, move_speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        nums = [-10, 10]
        self.move_speed = move_speed
        self.move_speed_game = move_speed
        # Choose random dx and dy values and and initially move the ball to a completely random spot
        self.dx = random.choice(nums)
        self.dy = random.choice(nums)

    # Move the ball dx and dy pixels
    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    # Change the Y direction of ball
    def bounce_y(self):
        self.dy *= -1

    # Change the X direction of ball
    def bounce_x(self):
        self.dx *= -1

    # Take the ball to the starting position
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed_game = self.move_speed

    # Increase ball speed
    def increase_speed(self, speed_boost):
        self.move_speed_game += speed_boost
