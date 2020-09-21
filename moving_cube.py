#moving cube by Jura Perić
#version 1.0.1

#modules
from random import*

#variables
xSpawnC=randint(1,5)
ySpawnC=randint(1,5)
xPSpawnC=0
controller=""

#screen
L1=["▓","▓","▓","▓","▓","▓","▓"]
L2=["░","░","░","░","░","░","░"] #1st line
L3=["░","░","░","░","░","░","░"] #2nd line
L4=["░","░","░","░","░","░","░"] #3rd line
L5=["░","░","░","░","░","░","░"] #4th line
L6=["░","░","░","░","░","░","░"] #5th line
L7=["▓","▓","▓","▓","▓","▓","▓"]

#defined commands
def spawnCube():
    if ySpawnC==1:
        L2[xSpawnC]="■"
    elif ySpawnC==2:
        L3[xSpawnC]="■"
    elif ySpawnC==3:
        L4[xSpawnC]="■"
    elif ySpawnC==4:
        L5[xSpawnC]="■"
    elif ySpawnC==5:
        L6[xSpawnC]="■"

def displayScreen():
    print("".join(L1))
    print("".join(L2))
    print("".join(L3))
    print("".join(L4))
    print("".join(L5))
    print("".join(L6))
    print("".join(L7))
    print("")
    #print(xSpawnC)
    #print(ySpawnC)


#main execution
spawnCube()
displayScreen()
while True:

    #input controls
    controller=input("Enter valid controls (up, down, left, right, wasd): ")

    if xSpawnC == -1:
        xSpawnC = 6
    if xSpawnC == 6 and controller == "d":
        xSpawnC = -1

    #up
    if controller=="up" or controller=="w" and ySpawnC==1: 
        L6[xSpawnC]="■"
        L2[xSpawnC]="░"
        ySpawnC=5
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==2:
        L2[xSpawnC]="■"
        L3[xSpawnC]="░"
        ySpawnC=1
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==3: 
        L3[xSpawnC]="■"
        L4[xSpawnC]="░"
        ySpawnC=2
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==4:
        L4[xSpawnC]="■"
        L5[xSpawnC]="░"
        ySpawnC=3
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==5:
        L5[xSpawnC]="■"
        L6[xSpawnC]="░"
        ySpawnC=4
        displayScreen()
        
    #down
    if controller=="down" or controller=="s" and ySpawnC==1: 
        L3[xSpawnC]="■"
        L2[xSpawnC]="░"
        ySpawnC=2
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==2:
        L4[xSpawnC]="■"
        L3[xSpawnC]="░"
        ySpawnC=3
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==3: 
        L5[xSpawnC]="■"
        L4[xSpawnC]="░"
        ySpawnC=4
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==4:
        L6[xSpawnC]="■"
        L5[xSpawnC]="░"
        ySpawnC=5
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==5:
        L2[xSpawnC]="■"
        L6[xSpawnC]="░"
        ySpawnC=1
        displayScreen()
        
    #left
    if controller=="left" or controller=="a" and ySpawnC==1:
        xPSpawnC=xSpawnC
        L2[xSpawnC-1]="■"
        L2[xPSpawnC]="░"
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==2:
        xPSpawnC=xSpawnC
        L3[xSpawnC-1]="■"
        L3[xPSpawnC]="░"
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==3:
        xPSpawnC=xSpawnC
        L4[xSpawnC-1]="■"
        L4[xPSpawnC]="░"
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==4:
        xPSpawnC=xSpawnC
        L5[xSpawnC-1]="■"
        L5[xPSpawnC]="░"
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==5:
        xPSpawnC=xSpawnC
        L6[xSpawnC-1]="■"
        L6[xPSpawnC]="░"
        xSpawnC=xSpawnC-1
        displayScreen()

    #right
    if controller=="right" or controller=="d" and ySpawnC==1:
        xPSpawnC=xSpawnC
        L2[xSpawnC+1]="■"
        L2[xPSpawnC]="░"
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==2:
        xPSpawnC=xSpawnC
        L3[xSpawnC+1]="■"
        L3[xPSpawnC]="░"
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==3:
        xPSpawnC=xSpawnC
        L4[xSpawnC+1]="■"
        L4[xPSpawnC]="░"
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==4:
        xPSpawnC=xSpawnC
        L5[xSpawnC+1]="■"
        L5[xPSpawnC]="░"
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==5:
        xPSpawnC=xSpawnC
        L6[xSpawnC+1]="■"
        L6[xPSpawnC]="░"
        xSpawnC=xSpawnC+1
        displayScreen()
