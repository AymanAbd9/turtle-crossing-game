from tkinter import CENTER
from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

        
    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align=CENTER, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=CENTER, font=FONT)
