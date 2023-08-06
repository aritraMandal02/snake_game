from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import update_score, new_high_score, show_final_score
import time

with open('scoreboard.txt', 'r') as f:
    prev_high_score = int(f.read())
    print(prev_high_score)

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor('black')
sc.title('Snake 2D')
sc.tracer(0)


snake = Snake()
food = Food()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

is_on = True
current_score = 0
update_score(current_score)

while is_on:
    sc.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.show_food_at_random()
        snake.grow_snake()
        current_score += 5
        update_score(current_score)
    if abs(snake.head.xcor()) >= 420 or abs(snake.head.ycor()) >= 320:
        is_on = False
    for part in snake.snake[1:-1]:
        if snake.head.distance(part) < 10:
            is_on = False

new_high_score(current_score)
show_final_score(prev_high_score, current_score)
