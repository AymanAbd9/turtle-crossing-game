from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + MOVE_DISTANCE
        self.goto(x, y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        