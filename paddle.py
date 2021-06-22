from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        # self.left_paddle()
        # self.right_paddle()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    # def right_paddle(self):
    #     self.color("white")
    #     self.penup()
    #     self.shape("square")
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.goto(350, 0)
    #
    # def left_paddle(self):
    #     self.color("white")
    #     self.penup()
    #     self.shape("square")
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.goto(-350, 0)

