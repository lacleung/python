import turtle
import os
import math
import random 

class paddle(turtle.Turtle):

    def __init__(self, width, length, color, posx, posy):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.penup()
        self.goto(posx, posy)

class ball(turtle.Turtle):

    def __init__(self, color, pos, dx, dy):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(pos)
        self.dx = dx
        self.dy = dy

    def collide(self):
        if abs(self.ycor()) > 290:
            self.sety(self.ycor()//abs(self.ycor()) * 290)
            ball.dy *= -1
        if abs(self.xcor()) > 390:
            self.sety(self.xcor()//abs(self.xcor()) * 390)
            ball.dx *= -1

class score(turtle.Turtle):

    def __init__(self, color):
        super().__init__()
        self.speed(0)
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0,260)

    def updateScore(self, score_a, score_b):
        self.clear()
        self.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier New", 24, "bold"))

# Movement functions (no arguments allowed)
def paddle_a_up():
    y = paddle_a.ycor()
    if y > 250:
        pass
    else:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y < -250:
        pass
    else:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y > 250:
        pass
    else:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y < -250:
        pass
    else:
        y -= 20
    paddle_b.sety(y)

# Turtle settings
turtle.colormode(255)

# Window settings
wn = turtle.Screen()
wn.title("Pong!")
wn.bgcolor("#000000")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle settings
paddle_a = paddle(5,1,"#f5b942",-350,0)
paddle_b = paddle(5,1,"#4287f5",350,0)

# Ball settings
ballnum = turtle.textinput("Difficulty Level", "Number of Balls:")
balls = []
for i in range(int(ballnum)):
    balls.append(ball((random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255)),
                       (0, 0),
                       random.randrange(1, 5) * random.randrange(-1, 2, 2),
                       random.randrange(1, 5) * random.randrange(-1, 2, 2)))

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Initialize score
score = score("#FFFFFF")
score_a = 0
score_b = 0

# Main game loop
while True:
    wn.update()
    score.updateScore(score_a, score_b)

    for ball in balls:
        # Move the balls
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Collision checking
        if abs(ball.ycor()) > 290:
            # Set ball pos to avoid out of bounds
            ball.sety(ball.ycor()//abs(ball.ycor()) * 290)
            ball.dy *= -1

        if (340 <= ball.xcor() <= 350) and ((paddle_b.ycor() - 45) < ball.ycor() < (paddle_b.ycor() + 45)):
            ball.setx(340)
            ball.dx *= -1

        if (-350 <= ball.xcor() <= -340) and ((paddle_a.ycor() - 45) < ball.ycor() < (paddle_a.ycor() + 45)): 
            ball.setx(-340)
            ball.dx *= -1

        if abs(ball.xcor()) > 390:
            if ball.xcor() > 0:
                score_a += 1
            else:
                score_b += 1
            
            score.updateScore(score_a, score_b)
            ball.goto(0,0)
            ball.dy = random.randrange(1, 5) * random.randrange(-1, 2, 2)
            ball.dx = random.randrange(1, 5) * ball.dx//abs(ball.dx) * -1