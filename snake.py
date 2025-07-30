from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # add new segment to the turtle
    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append("new segments")

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for new_seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[new_seg].xcor()
            new_y = self.segments[new_seg].ycor()
            self.segments[new_seg].goto(new_x, new_y)
        self.head.setheading(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





