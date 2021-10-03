import turtle as t
def krug (r):
    for i in range (36):
        t.forward(r)
        t.left(10)
        
n = 50
for i in range (n):
        krug (i)
        t.left(180)
        krug (i)
        t.left(180)