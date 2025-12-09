from turtle import Turtle
ALIGN  = 'center'
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score}', False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, align=ALIGN, font=FONT)