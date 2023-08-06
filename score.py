from turtle import Turtle
from turtle import Screen

sc = Screen()

tim = Turtle()


def update_score(score):
    style = ('Arial', 12, 'normal')
    s = f'Current score: {score}'
    tim.clear()
    tim.hideturtle()
    tim.color('white')
    tim.penup()
    tim.goto(-390, 278)
    tim.pendown()
    tim.write(s, font=style)


def new_high_score(current_score):
    with open('scoreboard.txt', 'r') as f:
        high_score = int(f.read())
    if current_score > high_score:
        high_score = current_score
        with open('scoreboard.txt', 'w') as f:
            f.write(str(high_score))
    return high_score


def show_final_score(prev_high_score, current_score):
    toe = Turtle()
    toe.color('white')
    style = ('Arial', 20, 'italic')
    if prev_high_score < current_score:
        toe.write(f'New High Score:\n{new_high_score(current_score)}!!!',
                  font=('Arial', 30, 'italic'), align='center')
    else:
        toe.write(f'Your Score: {current_score}'
                  f'\nHigh Score: {new_high_score(current_score)}',
                  font=style, align='center')

    toe.hideturtle()
    sc.exitonclick()
