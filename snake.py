from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_part = Turtle()
            new_part.speed(0)
            if position == (0, 0):
                new_part.shape('triangle')  # size is by default 20*20 pixels
            else:
                new_part.shape('square')
            new_part.color('white')
            new_part.penup()
            new_part.goto(position)
            self.snake.append(new_part)

    def move(self):  # refer image for better understanding of this algorithm
        for i in range(len(self.snake) - 1, 0, -1):
            pos_x = self.snake[i - 1].xcor()
            pos_y = self.snake[i - 1].ycor()
            self.snake[i].goto(pos_x, pos_y)
        self.snake[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)

    def grow_snake(self):
        new_part = Turtle()
        new_part.shape('square')
        new_part.color('white')
        new_part.penup()
        new_part.goto(self.snake[len(self.snake)-1].xcor(),
                      self.snake[len(self.snake)-1].ycor())
        self.snake.append(new_part)
    # def get_position(self):
    #     return self.head.xcor(), self.head.ycor()
