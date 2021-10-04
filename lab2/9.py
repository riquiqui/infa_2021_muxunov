import turtle as t
def prv (n):
    t.left(180/n)
    i = 1
    for i in range (n):
        t.forward(50)
        t.left(360/n)
    t.right(180/n)
        
t.left(90)
i = 3
while i <= 12:
    prv (i)
    t.penup()
    t.goto(5*i, 0)
    t.pendown()
    i += 1