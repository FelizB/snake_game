
from turtle import Screen
from snake import Snake
from score_board import ScoreBoard
import time
from food import Food
screen = Screen()
screen.bgcolor("black")

screen.title("My snake Game")
screen.tracer(0)

snaked = Snake()
food = Food()
snaked.create_snake()
score = ScoreBoard()

game_on = True

screen.listen()
screen.onkey(snaked.up, "Up")
screen.onkey(snaked.down, "Down")
screen.onkey(snaked.left, "Left")
screen.onkey(snaked.right, "Right")
while game_on:
    screen.update()
    time.sleep(0.1)
    snaked.move_snake()

    #     colliding
    if snaked.turtles[0].distance(food) < 20:
        food.refresh()
        snaked.extend()
        score.increase_score()

    if snaked.turtles[0].xcor() > 300 or snaked.turtles[0].xcor() < -300 or snaked.turtles[0].ycor() > 300 or snaked.turtles[0].ycor() < -300:
        game_on = False
        score.game_over()

    for segments in snaked.turtles[2:]:
        if snaked.turtles[1].distance(segments) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()









