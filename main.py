import turtle  ## 100 imported screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Create the Screen
screen = turtle.Screen()  # 100
screen.setup(width=800, height=600) # 100
screen.bgcolor("black")  # 100

screen.title("Jim's Pong Game") # 100
screen.tracer(0) # turns off animation

# Create scoreboard
scoreboard = Scoreboard()

# Create paddle  .... (and move a paddle?)
paddleLeft = Paddle()
paddleLeft.start(-350, 0) # 100

# Create another paddle
paddleRight = Paddle()
paddleRight.start(350, 0) # 100

# draw the net
net = turtle.Turtle()
net.color("white")
net.shape("square")
net.shapesize(30, 0.1)

# Create the ball ...  (and make it move?)
ball = Ball()


game_is_on = True

screen.listen() # 100

screen.onkeypress(paddleLeft.up, "s")  # This will call the up function if the "Left" arrow key is pressed
screen.onkeypress(paddleLeft.down, "x")

screen.onkey(paddleRight.up, "Up")  # This will call the up function if the "Left" arrow key is pressed
screen.onkey(paddleRight.down, "Down")

while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()

    # Detect collision with top or bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddleRight) < 50 and ball.xcor() > 320\
            or ball.distance(paddleLeft) <50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()  # 100



