import turtle as t

def draw (number, n):
    list_of_coords = [
    (0, 0, 50, 0, 50, 100, 0, 100, 0, 0),
    (0, 50, 50, 100, 50, 0),
    (0, 100, 50, 100, 50, 50, 0, 0, 50, 0),
    (0, 100, 50, 100, 0, 50, 50, 50, 0, 0),
    (0, 100, 0, 50, 50, 50, 50, 0, 50, 100),
    (50, 100, 0, 100, 0, 50, 50, 50, 50, 0, 0, 0),
    (50, 100, 0, 50, 0, 0, 50, 0, 50, 50, 0, 50),
    (0, 100, 50, 100, 0, 50, 0, 0),
    (0, 100, 50, 100, 50, 0, 0, 0, 0, 100, 0, 50, 50, 50),
    (0, 0, 50, 50, 50, 100, 0, 100, 0, 50, 50, 50,)
    ]
    
    t.penup()
    t.goto(list_of_coords[number][0] + 100*n - 300, list_of_coords[number][1])
    t.pendown()
    for i in range (len(list_of_coords[number])//2):
        t.goto(list_of_coords[number][i*2] + n*100 - 300, list_of_coords[number][i*2 + 1])

n = 0
draw_list = [1, 4, 8, 8]
for i in range (len(draw_list)):
    draw(draw_list[i], n)
    n += 1
