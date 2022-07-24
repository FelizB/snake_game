from turtle import Turtle, Screen
import time
screen = Screen()
move=20


class Snake:
    def __init__(self):
        self.turtles = []
        self.number = 0

    def create_snake(self):
        for _ in range(3):
            self.add_segment(self.number)

    def move_snake(self):
        for items in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[items-1].xcor()
            new_y = self.turtles[items-1].ycor()
            self.turtles[items].goto(new_x, new_y)
        self.turtles[0].forward(move)

    def add_segment(self, position):
        create_turtle = Turtle("square")
        create_turtle.penup()
        create_turtle.color("white")
        create_turtle.goto(self.number, 0)
        self.number -= 20
        self.turtles.append(create_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

