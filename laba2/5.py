import turtle as t
a = 1
while a <=1000:
  turtle.forward (1*a)
  turtle.left(90)
  turtle.forward (1*a)
  turtle.left(90)
  turtle.forward (1*a)
  turtle.left(90)
  turtle.forward (1*a)
  turtle.left(90)
  turtle.penup()
  turtle.goto(-0.5*a, -0.5*a)
  turtle.pendown()
  a += 1