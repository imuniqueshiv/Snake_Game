from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape of the food to a circle
        self.color("red")  # Set the color of the food to red
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Scale down the size of the food
        self.penup()  # Lift the pen to avoid drawing lines when moving the food
        self.speed("fastest")  # Set the speed of the food to the fastest for quick repositioning
        self.refresh()  # Call the refresh method to place the food at a random position

    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen bounds
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen bounds
        self.goto(random_x, random_y)  # Move the food to the new random position
