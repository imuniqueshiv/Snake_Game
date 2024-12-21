from turtle import Screen
from snake_game import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create instances of Snake, Food, and Scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# Listen for key presses to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Delay for a short period
    snake.move()     # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 14:
        food.refresh()     # Refresh the food position
        snake.extend()     # Extend the snake's body
        score.increase()   # Increase the score

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()  # Display game over message

    # Detect collision with tail
    for segment in snake.all_snakes[1:]:  # Check each segment except the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()  # Display game over message

# Keep the window open until clicked
screen.exitonclick()
