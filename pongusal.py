# Pong personalizado para la Universidad de Salamanca

import turtle

# Configuración de la pantalla
win = turtle.Screen()
win.title("Pong - Universidad de Salamanca")
win.bgcolor("#800000")  # Color burdeos (representativo de la USAL)
win.setup(width=800, height=600)
win.tracer(0)

# Establecer el fondo con el escudo de la USAL
win.bgpic("usal_escudo.gif")  # Asegúrate de que este archivo esté en la misma carpeta

# Registrar imágenes personalizadas para las barras
win.register_shape("escudo_bejar.gif")  # Asegúrate de tener este archivo en la misma carpeta
win.register_shape("escudo_bejar2.gif")  # Segundo escudo para el otro jugador

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("escudo_bejar.gif")  # Usar el escudo como barra
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("escudo_bejar2.gif")  # Usar el escudo como barra
paddle_b.penup()
paddle_b.goto(350, 0)

# Pelota
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("gold")  # Color dorado (representativo de la USAL)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Marcador
score_a = 0
score_b = 0

# Texto del marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))

# Funciones para mover las barras
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)

# Configuración de controles
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Bucle principal del juego
while True:
    win.update()

    # Movimiento de la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Comprobación de bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Jugador A: {score_a}  Jugador B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Jugador A: {score_a}  Jugador B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Colisiones con las barras
    if (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1