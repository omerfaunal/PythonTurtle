from turtle import Turtle

# You can customize font
FONT = ("Courier", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height, player1, player2):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        # Get the post position and player names.
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player1 = player1
        self.player2 = player2
        # Set scores to 0
        self.lScore, self.rScore = 0, 0
        self.update_score()

    # Updates the score when any party scores
    def update_score(self):
        self.clear()
        # Move slightly to the left of the middle of the screen.
        self.goto(-(FONT[1] * 1 * .5), self.screen_height - (FONT[1] * 2))
        self.write(f"{self.player1} {self.lScore}", align="right", font=FONT)
        # Move slightly to the right of the middle of the screen.
        self.goto((FONT[1] * 1.5), self.screen_height - (FONT[1] * 2))
        self.write(f"{self.player2} {self.rScore}", align="left", font=FONT)
        # Separate two players
        self.goto(0, self.screen_height - (FONT[1] * 2))
        self.write(" |", align="center", font=FONT)

    # Increase left player's score
    def left_scored(self):
        self.lScore += 1
        self.update_score()

    # Increase right player's score
    def right_scored(self):
        self.rScore += 1
        self.update_score()
