# Section 1 - Your code
from utils import *
player_name = input("What is your name?")

set_background("nyc")

s1 = create_sprite("cool_dog", -300, 0)
s2 = create_sprite("puppy", 30, 0)

s1.color("white")
s2.color("white")
time.sleep(5)

s1.write("Hey little boy, why are you so tiny??",font = ("Arial", 10, "normal"))
window.update()
time.sleep(4)

s1.clear()
window.update()
time.sleep(1)

s2.write("It's not my fault my mom was 1 foot!!!",font = ("Arial", 10, "normal"))
window.update()
time.sleep(4)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"No its your fault bc your dads 11 feet",font = ("Arial", 10, "normal"))
window.update()
time.sleep(3)

s2.clear()
s2.write("Oops I guess it was my fault!",font = ("Arial", 10, "normal"))
window.update()
time.sleep(2)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()