from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snaked = Snake()

snaked.create_snake()


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










