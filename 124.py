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
        distGo = rnd.randint(0, math.pow(distToGo, 2))
        distGo = int(math.sqrt(distGo))
        distTraveled += distGo
        distToGo -= distGo
        mazeDrawer.forward(distGo)
        if (distToGo >= pathWidth * 2 and distTraveled >= pathWidth * 2):
            while (randomChoice == " "):
                randomChoice = rnd.choice(obstacleChoices)
                if (randomChoice == "wall"):
                    if (i < 26 and (lastChoice == " " or lastChoice == "door")):
                        DrawWall(pathWidth)
                    lastChoice = "wall"
                    obstacleChoices.pop()
                    obstacleChoices.append("door")
                else:
                    if (distToGo >= pathWidth * 2 + 20 and (lastChoice == " " or lastChoice == "wall") and i > 2):
                        doorDist = rnd.randint(10, int((distToGo - pathWidth * 2)/2))
                        DrawDoor(doorDist)
                        distToGo -= doorDist
                        distTraveled += doorDist
                    lastChoice = "door"
                    obstacleChoices.pop()
                    obstacleChoices.append("wall")
    distance -= pathWidth / 2
    headingSet -= 90
    mazeDrawer.setheading(headingSet)
    randomChoice = " "



wn = trtl.Screen()

wn.mainloop()