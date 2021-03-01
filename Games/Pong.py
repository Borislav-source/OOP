import turtle

# Todo Create a screen
wn = turtle.Screen()
wn.title("Pong by Bogdan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Todo Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390, 0)

# Todo Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(380, 0)

# Todo Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1


# Todo Functions for movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y + 20 <= 260:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y - 20 > -260:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y + 20 <= 260:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y - 20 > -260:
        y -= 20
    paddle_b.sety(y)


# Todo Connect Keyboard
wn.listen()
wn.onkey(paddle_a_up, 'w')
wn.onkey(paddle_a_down, 's')
wn.onkey(paddle_b_up, 'Up')
wn.onkey(paddle_b_down, 'Down')

# Todo Scoring
player_a = 0
player_b = 0

# Todo Main game loop
while True:
    wn.update()

    # Todo Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Todo Borders Validations
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        print('Player A is the WINNER!\n'
              'Points:\n'
              f'Player A: {player_a}\n'
              f'Player B: {player_b}')
        break

    if ball.xcor() < -390:
        print('Player B is the WINNER!\n'
              'Points:\n'
              f'Player A: {player_a}\n'
              f'Player B: {player_b}')
        break

    # Todo Collisions with paddles
    if ball.xcor() > 370 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        player_b += 1
    if ball.xcor() < -370 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        player_a += 1
