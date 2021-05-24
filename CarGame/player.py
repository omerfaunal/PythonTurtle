from turtle import Turtle

class Player(Turtle):
    def __init__(self, screen_height, player_speed, color):
        super().__init__()
        self.starting_position = (0, -screen_height//2 + 20)
        self.player_speed = player_speed
        self.color(color)
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.turtlesize(1.5,1.5,1.5)
        self.goto(self.starting_position)

    def move(self):
        self.goto(0, self.ycor() + self.player_speed )

    def getYcor(self):
        return self.ycor()

    def go_back(self):
        self.goto(self.starting_position)