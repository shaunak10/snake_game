from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#TODO: Create a snake body
#TODO: Move the snake
#TODO: Control the snake
#TODO: Detect collision with food
#TODO: Create a scoreboard
#TODO: Detect collision with wall
#TODO: Detect collision with tail

screen = Screen()
screen.setup(width=600, height=600) # keyword arguments else we can also write (600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # adds a 0.2s delay after each screen moves
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # if head collides with any segment in the tail:
        #trigger game_over

screen.exitonclick()