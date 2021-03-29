import turtle
import random

turtle.shape("turtle")
turtle.speed(0)

for i in range(1000):
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  turtle.color(red, green, blue)

  x = random.randint(-300, 300)
  y = random.randint(-300, 300)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

  # Draw a rectangle
  # length and height to be random, 10 - 100
  length = random.randint(10, 100)
  height = random.randint(10, 100)

  turtle.begin_fill()
  for i in range(1, 3):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
  turtle.end_fill()

  xx = random.randint(-300, 300)
  yy = random.randint(-300, 300)
  turtle.penup()
  turtle.goto(xx,yy)
  turtle.pendown()
  radius = random.randint(10, 50)
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()