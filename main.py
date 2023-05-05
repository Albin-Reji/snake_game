from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen=Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake= Snake()
food= Food()
score= Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     collosion with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        score.increase_score()

#     detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()< -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        score.game_over()
        is_game_on= False

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            is_game_on= False
            Scoreboard.game_over()
screen.exitonclick()