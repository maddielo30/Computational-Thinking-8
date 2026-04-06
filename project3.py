import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-200
y1 = 200
x2 = -200
y2 = 100
x3 = -200
y3 = 0
x4 = -300
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("summer")
t1 = create_sprite("corgi",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("turtle2",x3,y3)
t4 = create_sprite("stitch",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - x4 is the fastest because it has a bigger range and increases less. And x2 is the slowest because it has the smallest range.
for i in range(30):
    x1 += 12
    x2 += 10
    x3 += 15
    x4 += 20

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
        s5.write("Player 1 wins! Great job")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
        s5.write("Player 2 wins! Great job")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
        s5.write("Player 3 wins! Great job")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
        s5.write("Player 4 wins! Great job")


turtle.exitonclick()