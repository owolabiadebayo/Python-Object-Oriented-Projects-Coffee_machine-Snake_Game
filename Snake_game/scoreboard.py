from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"score:{self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.goto(0,270)
        self.high_score = 0
        self.penup()
    def update_scoreboard(self):
        self.write(f"Score: {self.score} high score:{self.high_score}", align="center", font={"Arial", 24, "normal"})
        self.reset()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over: {self.score}", align="center", font={"Arial", 24, "normal"})