#moving cube by Jura Perić
#version 1.1

#modules
from random import*

#variables
xSpawnC=randint(1,5)
ySpawnC=randint(1,5)
xPSpawnC=0
controller=""
border="▓"
ground="░"
character="■"

#screen
L1=[border,border,border,border,border,border,border]
L2=[ground,ground,ground,ground,ground,ground,ground] #1st line
L3=[ground,ground,ground,ground,ground,ground,ground] #2nd line
L4=[ground,ground,ground,ground,ground,ground,ground] #3rd line
L5=[ground,ground,ground,ground,ground,ground,ground] #4th line
L6=[ground,ground,ground,ground,ground,ground,ground] #5th line
L7=[border,border,border,border,border,border,border]

#defined commands
def spawnCube():
    if ySpawnC==1:
        L2[xSpawnC]=character
    elif ySpawnC==2:
        L3[xSpawnC]=character
    elif ySpawnC==3:
        L4[xSpawnC]=character
    elif ySpawnC==4:
        L5[xSpawnC]=character
    elif ySpawnC==5:
        L6[xSpawnC]=character

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
        L6[xSpawnC]=character
        L2[xSpawnC]=ground
        ySpawnC=5
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==2:
        L2[xSpawnC]=character
        L3[xSpawnC]=ground
        ySpawnC=1
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==3: 
        L3[xSpawnC]=character
        L4[xSpawnC]=ground
        ySpawnC=2
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==4:
        L4[xSpawnC]=character
        L5[xSpawnC]=ground
        ySpawnC=3
        displayScreen()
    elif controller=="up" or controller=="w" and ySpawnC==5:
        L5[xSpawnC]=character
        L6[xSpawnC]=ground
        ySpawnC=4
        displayScreen()
        
    #down
    if controller=="down" or controller=="s" and ySpawnC==1: 
        L3[xSpawnC]=character
        L2[xSpawnC]=ground
        ySpawnC=2
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==2:
        L4[xSpawnC]=character
        L3[xSpawnC]=ground
        ySpawnC=3
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==3: 
        L5[xSpawnC]=character
        L4[xSpawnC]=ground
        ySpawnC=4
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==4:
        L6[xSpawnC]=character
        L5[xSpawnC]=ground
        ySpawnC=5
        displayScreen()
    elif controller=="down" or controller=="s" and ySpawnC==5:
        L2[xSpawnC]=character
        L6[xSpawnC]=ground
        ySpawnC=1
        displayScreen()
        
    #left
    if controller=="left" or controller=="a" and ySpawnC==1:
        xPSpawnC=xSpawnC
        L2[xSpawnC-1]=character
        L2[xPSpawnC]=ground
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==2:
        xPSpawnC=xSpawnC
        L3[xSpawnC-1]=character
        L3[xPSpawnC]=ground
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==3:
        xPSpawnC=xSpawnC
        L4[xSpawnC-1]=character
        L4[xPSpawnC]=ground
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==4:
        xPSpawnC=xSpawnC
        L5[xSpawnC-1]=character
        L5[xPSpawnC]=ground
        xSpawnC=xSpawnC-1
        displayScreen()
    if controller=="left" or controller=="a" and ySpawnC==5:
        xPSpawnC=xSpawnC
        L6[xSpawnC-1]=character
        L6[xPSpawnC]=ground
        xSpawnC=xSpawnC-1
        displayScreen()

    #right
    if controller=="right" or controller=="d" and ySpawnC==1:
        xPSpawnC=xSpawnC
        L2[xSpawnC+1]=character
        L2[xPSpawnC]=ground
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==2:
        xPSpawnC=xSpawnC
        L3[xSpawnC+1]=character
        L3[xPSpawnC]=ground
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==3:
        xPSpawnC=xSpawnC
        L4[xSpawnC+1]=character
        L4[xPSpawnC]=ground
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==4:
        xPSpawnC=xSpawnC
        L5[xSpawnC+1]=character
        L5[xPSpawnC]=ground
        xSpawnC=xSpawnC+1
        displayScreen()
    if controller=="right" or controller=="d" and ySpawnC==5:
        xPSpawnC=xSpawnC
        L6[xSpawnC+1]=character
        L6[xPSpawnC]=ground
        xSpawnC=xSpawnC+1
        displayScreen()
