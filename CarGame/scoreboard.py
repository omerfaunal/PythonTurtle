from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.level = 1
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-self.screen_width//2 + 40, self.screen_height//2 - 50)
        self.write(f"Level: {self.level}", align="left", font = FONT)

    def get_level(self):
        return self.level

    def you_are_dead(self):
        self.goto(0,0)
        self.write("Great job! Bravo! You killed the Turtle!", align="center", font = ("Courier", 16, "bold"))