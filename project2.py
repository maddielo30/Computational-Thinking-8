summer_points=0
winter_points=0
spring_points=0
fall_points=0
print("Take this short quiz and see if you are a Summer, Winter, Spring, or Fall person!")
print("Have Fun!")
input("")
answer1=input("Do you want A lemonade, B hot chocolate, or C chai?")
if answer1=="A":
    summer_points +=1
    spring_points +=1
elif answer1=="B":
    winter_points +=1
elif answer1=="C":
    fall_points +=1
input("")
answer2=input("What scene most appeals to you?")
answer2=input("A bright blue ocean, B Cozy cabin with snow, C Cherry blossoms, or D Falling orange leaves")
if answer2=="A":
    summer_points +=1
elif answer2=="B":
    winter_points +=1
elif answer2=="C":
    spring_points +=1
elif answer2=="D":
    fall_points +=1
input("")
answer3=input("What activity sounds most fun to you?")       
answer3=input("A Swimming, B Skiing, C Picnicking, or D Hiking")
if answer3=="A":
    summer_points +=1
elif answer3=="B":
    winter_points +=1
elif answer3=="C":
    spring_points +=1
    summer_points +=1
elif answer3=="D":
    fall_points +=1
    spring_points +=1    
input("")
answer4=input("What is your favorite type of clothing?")  
answer4=input("A shorts/tank tops, B cozy sweaters, or C light jacket")
if answer4=="A":
    summer_points +=1
    spring_points +=1
elif answer4=="B":
    winter_points +=1
    fall_points +=1
elif answer4=="C":
    spring_points +=1   
input("")
answer5=input("What time of day is best? A Midday, B Nighttime, C Sunrise, or D Sunset?")    
if answer5=="A":
    summer_points +=1
    spring_points ==1
elif answer5=="B":
    winter_points +=1
    summer_points +=1
elif answer5=="C":
    spring_points +=1
elif answer5=="D":
    fall_points +=1
    summer_points +=1   
input("")
if summer_points > winter_points and summer_points > spring_points and summer_points > fall_points:
    print("You are a summer person! You love warm weather and fun summer activities")
if winter_points > summer_points and winter_points > spring_points and winter_points > fall_points:
    print("You are a winter person! You like the snow, feeling cozy, and like warm drinks!")   
if spring_points > winter_points and spring_points > summer_points and spring_points > fall_points:
    print("You are a spring person! You are a lively person, who likes getting fresh starts!")     
if fall_points > winter_points and fall_points > spring_points and fall_points > summer_points:
    print("You are a fall person! You appreciate comfort and fall baking")

print("I hope you enjoyed this quiz!")   