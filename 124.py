import turtle as trtl
import random as rnd
import math

mazeDrawer = trtl.Turtle()
mazeDrawer.penup()
mazeDrawer.goto(150, 150)
mazeDrawer.pensize(2)
mazeDrawer.pendown()
mazeDrawer.setheading(270)
mazeDrawer.speed(0)
headingSet = 270
distance = 300
pathWidth = 16
doorDist = 0
wallDist = 0
distGo = 0
distTraveled = 0
distToGo = 300
lastChoice = " "
randomChoice = " "
obstacleChoices = ["wall", "door", " "]
keysPress = ["w", "a", "s", "d"]

def DrawDoor(distanceForDoor):
    global mazeDrawer
    mazeDrawer.penup()
    mazeDrawer.forward(distanceForDoor)
    mazeDrawer.pendown()

def DrawWall(distanceForWall):
    global mazeDrawer
    global pathWidth
    global headingSet
    mazeDrawer.setheading(headingSet - 90)
    mazeDrawer.forward(distanceForWall)
    mazeDrawer.back(distanceForWall)
    mazeDrawer.setheading(headingSet)

for i in range (30):
    distToGo = distance
    distTraveled = 0
    while (distTraveled < distance):
        distGo = rnd.randint(int(8 - 8 *(distTraveled/distance)), math.pow(distToGo, 2))
        distGo = int(math.sqrt(distGo))
        distTraveled += distGo
        distToGo -= distGo
        mazeDrawer.forward(distGo)
        if (distToGo >= pathWidth * 2 and distTraveled >= pathWidth * 2):
            while (randomChoice == " "):
                randomChoice = rnd.choice(obstacleChoices)
                if (randomChoice == "wall"):
                    if (i < 26):
                        DrawWall(pathWidth)
                else:
                    if (distToGo >= pathWidth * 2 + 20 and i > 2):
                        doorDist = rnd.randint(10, int((distToGo - pathWidth * 2)/2))
                        DrawDoor(doorDist)
                        distToGo -= doorDist
                        distTraveled += doorDist
    distance -= pathWidth / 2
    headingSet -= 90
    mazeDrawer.setheading(headingSet)
    randomChoice = " "
mazeDrawer.hideturtle()

mazeRunner = trtl.Turtle()
mazeRunner.speed(0)
mazeRunner.penup()

def moveRunner(event):
    global mazeRunner
    if (event == "w"):
        mazeRunner.setheading(90)
    elif (event == "a"):
        mazeRunner.setheading(180)
    elif (event == "s"):
        mazeRunner.setheading(270)
    elif (event == "d"):
        mazeRunner.setheading(0)
    mazeRunner.forward(4)



wn = trtl.Screen()
for n in keysPress:
  wn.onkeypress(lambda n=n: moveRunner(n), str(n))
wn.listen()
wn.mainloop()