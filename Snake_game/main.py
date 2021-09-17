from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


"""Screen setup"""
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Stephen Snake Game")
screen.tracer(0)

# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)

# starting_positions = [(0,0), (-20,0), (-40,0) ]

# segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
"""Snake Movement"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:       
    screen.update()
    time.sleep(0.1)

    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1]. xcor()
    #     new_y = segments[seg_num - 1].ycor()
    snake.move()
    #detect collision
    if snake.head.distance(food) < 15:
        print("num num num")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        """Detect collision with wall"""
        if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
            scoreboard.reset()
            """Detect collision with tail"""
            for segment in snake.segments[1:]:
                if snake.head.distance(segment)<10:
                    scoreboard.reset()
                    screen.exitonclick()
            # scoreboard.game_over()
            # game_is_on = False 
        # scoreboard.game_over()
        # game_is_on = False  