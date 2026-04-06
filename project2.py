summer_points=0
winter_points=0
spring_points=0
fall_points=0
print("")
print("")
print("Take this short quiz and see if you are a Summer, Winter, Spring, or Fall person!")
print("Have Fun!")
print("")
answer1=input("Do you want A lemonade, B hot chocolate, or C chai?")
if answer1=="A" or answer1=="a":
    summer_points +=1
    spring_points +=1
elif answer1=="B" or answer1=="b":
    winter_points +=1
elif answer1=="C" or answer1=="c":
    fall_points +=1
print("")
answer2=input("What scene most appeals to you?")
answer2=input("A bright blue ocean, B Cozy cabin with snow, C Cherry blossoms, or D Falling orange leaves")
if answer2=="A" or answer2=="a":
    summer_points +=1
elif answer2=="B" or answer2=="b":
    winter_points +=1
elif answer2=="C" or answer2=="c":
    spring_points +=1
elif answer2=="D" or answer2=="d":
    fall_points +=1
print("")
answer3=input("What activity sounds most fun to you?")       
answer3=input("A Swimming, B Skiing, C Picnicking, or D Hiking")
if answer3=="A" or answer3=="a":
    summer_points +=1
elif answer3=="B" or answer3=="b":
    winter_points +=1
elif answer3=="C" or answer3=="c":
    spring_points +=1
    summer_points +=1
elif answer3=="D" or answer3=="d":
    fall_points +=1
    spring_points +=1    
print("")
answer4=input("What is your favorite type of clothing?")  
answer4=input("A shorts/tank tops, B cozy sweaters, or C light jacket")
if answer4=="A" or answer4=="a":
    summer_points +=1
    spring_points +=1
elif answer4=="B" or answer4=="b":
    winter_points +=1
    fall_points +=1
elif answer4=="C" or answer4=="c":
    spring_points +=1   
print("")
answer5=input("What time of day is best? A Midday, B Nighttime, C Sunrise, or D Sunset?")    
if answer5=="A" or answer5=="a":
    summer_points +=1
    spring_points +=1
elif answer5=="B" or answer5=="b":
    winter_points +=1
    summer_points +=1
elif answer5=="C"or answer5=="c":
    spring_points +=1
elif answer5=="D" or answer5=="d":
    fall_points +=1
    summer_points +=1   
print("")
if summer_points > winter_points and summer_points > spring_points and summer_points > fall_points:
    print("You are a summer person! You love warm weather, activities, and being social. You will usually feel more productive when its sunny outside.")
if winter_points > summer_points and winter_points > spring_points and winter_points > fall_points:
    print("You are a winter person! You like the crisp cold air and snow and feeling cozy. Being warm is essential!")   
if spring_points > winter_points and spring_points > summer_points and spring_points > fall_points:
    print("You are a spring person! You like to make new connections with people and have a desire for new beginnings!")     
if fall_points > winter_points and fall_points > spring_points and fall_points > summer_points:
    print("You are a fall person! You appreciate comfort,fall baking, and halloween. You like to layer clothing especially in the cold fall air!")
print("")
print("")
print("I hope you enjoyed this quiz!")   