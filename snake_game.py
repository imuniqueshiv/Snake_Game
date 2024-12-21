from turtle import Turtle, Screen

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
FORWARD = 20  # Distance the snake moves forward
UP = 90       # Angle for moving up
DOWN = 270    # Angle for moving down
LEFT = 180    # Angle for moving left
RIGHT = 0     # Angle for moving right

# Screen setup
screen = Screen()

class Snake:

    def __init__(self):
        self.all_snakes = []  # List to hold all snake segments
        self.create_snake()   # Create the initial snake
        self.head = self.all_snakes[0]  # The head of the snake is the first segment

    def create_snake(self):
        # Create the initial snake segments
        for position in STARTING_POSITIONS:
            self.add_segments(position)  # Add each segment to the snake

    def add_segments(self, position):
        # Create a new turtle segment and add it to the snake
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)  # Set the position of the new segment
        self.all_snakes.append(new_turtle)  # Append the new segment to the list

    def extend(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segments(self.all_snakes[-1].position())

    def move(self):
        # Move each segment to the position of the segment in front of it
        for turtles_ in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[turtles_ - 1].xcor()
            new_y = self.all_snakes[turtles_ - 1].ycor()
            self.all_snakes[turtles_].goto(new_x, new_y)
        self.head.forward(FORWARD)  # Move the head forward

    def right(self):
        # Turn the snake to the right, unless it is currently moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        # Turn the snake up, unless it is currently moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        # Turn the snake to the left, unless it is currently moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        # Turn the snake down, unless it is currently moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
