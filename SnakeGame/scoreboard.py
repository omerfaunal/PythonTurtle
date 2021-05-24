from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.goto(0, self.screen_height//2 - 30)
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
