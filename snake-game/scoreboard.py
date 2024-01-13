from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # Deciding upon the coordinates of where the scoreboard is to be placed
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)
        self.hideturtle()
        # Deciding upon the coordinates of where the scoreboard is to be placed

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)

    def game_over(self):
        FONT = ("Arial", 28, "normal")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNEMENT, font=FONT)