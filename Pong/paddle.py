from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, paddle_size, paddle_speed):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # Create paddle with given size
        self.paddle_speed = paddle_speed
        self.shapesize(stretch_wid=paddle_size, stretch_len=1)
        self.goto(position)

    # Move up units by the given speed value.
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + self.paddle_speed)

    # Move up units by the given speed value.
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - self.paddle_speed)
