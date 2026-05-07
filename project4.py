from utils import *

# Section 1 - setup
set_background("summer")


# TODO - create at least two variables and set their starting value. ex: cookies = 0
cloud2 = 0
rainbow3 = 0
spritelist = []
# OPTIONAL: use this invisible alien to say a message
m1=create_sprite("cloud2",-200,100)
m2=create_sprite("rainbow3",-20,100)
m1.hideturtle()
# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_cloud2():
    global cloud2
    cloud2 +=1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    s1=create_sprite("cloud2",x,y)
    spritelist.append(s1)
window.onkeypress(get_cloud2, "a")
# when you press the key "a" a cloud 
def get_rainbow3():
    global rainbow3,cloud2
    if cloud2 >=10:
        rainbow3 +=1
        cloud2 -= 10
    
        x = random.randint(-200,300)
        y = random.randint(-200,300)
        create_sprite("rainbow3",x,y)

        for i in range (10):
            s1 = spritelist.pop()
            s1.hideturtle()
window.onkeypress(get_rainbow3,"m")
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    m1.clear()
    m1.write(f"Cloud2: {cloud2}\nrainbow: {rainbow3}",font=("Arial",30,"normal") )

    # TODO - put any automatic actions her

    
    time.sleep(0.01)
    window.update()