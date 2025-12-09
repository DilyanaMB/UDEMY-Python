from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.goto(0,260)
        self.clear()
        self.score += 1
        self.write(f'score : {self.score}', False, align="center", font=("Arial", 20, "normal"))
