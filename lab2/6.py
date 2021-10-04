import turtle as t
n = 10
i = 1
while i <= n:
    t.forward(100)
    t.backward(100)
    t.left(360/n)
    i += 1