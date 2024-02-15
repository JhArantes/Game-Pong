
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer()

# Placar Jogo
pontos_a = 0
pontos_b = 0


# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = -4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0 Player B: 0",  font=("Courier", 24, "normal"),align="center")



# Function
def raquete_a_up():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)

def raquete_a_down():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)

def raquete_b_up():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)

def raquete_b_down():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)


# Teclado Bind
wn.listen()
wn.onkeypress(raquete_a_up, "w")
wn.onkeypress(raquete_a_down, "s")
wn.onkeypress(raquete_b_up, "Up")
wn.onkeypress(raquete_b_down, "Down")



# Loop principal
while True:
    wn.update()

    # Move a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checa a borda
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pontos_a += 1
        pen.clear()
        pen.write(f"Player A: {pontos_a} Player B: {pontos_b}",  font=("Courier", 24, "normal"),align="center")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pontos_b += 1
        pen.clear()
        pen.write(f"Player A: {pontos_a} Player B: {pontos_b}",  font=("Courier", 24, "normal"),align="center")

    # Colisão entre raquete e bola
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < raquete_b.ycor() + 40 and ball.ycor() > raquete_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < raquete_a.ycor() + 40 and ball.ycor() > raquete_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1