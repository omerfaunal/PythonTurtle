from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width, self.screen_height = screen_width, screen_height
        self.shape("circle")
        self.penup()
        self.color("cyan")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
        
    def refresh(self):
        num_x = random.randint(-self.screen_width//2 + 50, self.screen_width//2 - 50)
        num_y = random.randint(-self.screen_height//2 + 50, self.screen_height//2 - 50)
        self.goto(num_x, num_y)
