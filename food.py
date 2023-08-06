from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # using class inheritance
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.penup()
        self.show_food_at_random()

    def show_food_at_random(self):
        x = random.randint(-360, 360)
        y = random.randint(-260, 260)
        self.goto(x, y)

    # def get_position(self):
    #     return self.food.xcor(), self.food.ycor()
