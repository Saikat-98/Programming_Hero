from turtle import  *

TURTLE_SIZE = 20
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# screen = Screen()

t = Pen()
t.speed(8)
bgcolor('black')

for x in range(60):
    # Half Circle
    t.pencolor(colors[x % 6])
    t.left(50)
    t.forward(98)
    t.circle(40, 180)

    # Other Half Circle
    t.left(260)
    t.circle(40, 180)
    t.forward(98)

    t.left(50)

done()



