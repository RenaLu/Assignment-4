##############################################################################
#Purpose:  This program creates beautiful string-art patterns inside a circle
#Prerequisites: Arrays, modular indexing, and Grade 11 trigonometry
#Programmer:  J. Schattman & Rena Lu
#Last modified:  April 8, 2014
##############################################################################

#IMPORTS
from tkinter import *
from math import *
from time import *


#SET UP THE DRAWING CANVAS
screenHeight = 700
screenWidth = 700
root = Tk()
screen = Canvas( root, width=screenWidth, height=screenHeight, background = "black" )
screen.pack()


#SET PARAMETERS
xCenter = screenWidth / 2
yCenter = screenHeight / 2
radius = 0.4 * screenWidth
nailRadius = 3
numNails = 100
skip = 30 #must be less than numNails
colors1 = [ "SpringGreen", "MediumSeaGreen", "SeaGreen", "ForestGreen","DarkGreen", "YellowGreen","OliveDrab" ] #ADD MORE COLORS TO THE LIST FOR DIFFERENT EFFECTS
numColors1 = len( colors1 )
colors2 = [ "Pink" ]
numColors2 = len( colors2 )
colors3 = [ "Gold", "Yellow", "LightYellow", "LemonChiffon" ]
numColors3 = len( colors3 )

#DRAW THE OUTER CIRCLE
screen.create_oval( xCenter-radius, yCenter-radius, xCenter+radius, yCenter+radius, outline = "yellow", width=4 )
screen.create_rectangle(0,0,700,700,fill="black")

skips = []

for i in range(1, int(numNails/2+1)):
    skips.append(i)


#CREATE AN ARRAY OF EVENLY SPACED nails ALONG THE OUTER CIRCLE
#THESE nails WILL BE THE NAILS BETWEEN WHICH THE "STRINGS" ARE STRUNG
deltaTheta = 360.0 / numNails
nails = []

for pointCounter in range( 0, numNails ):
    
    thetaDegrees = pointCounter * deltaTheta
    theta = radians( thetaDegrees )

    #The (x,y) coordinates of the current nail.
    x1 = xCenter + radius * cos( theta )
    y1 = yCenter - radius * sin( theta )
    
    newPoint = [ x1, y1 ]
    nails.append( newPoint )
    
    #OPTIONALLY DRAW THE nails
    screen.create_oval( x1-nailRadius, y1-nailRadius, x1+nailRadius, y1+nailRadius, fill="white" )



#DRAW THE STRINGS   
for startIndex in range(0, numNails):
    thetaDegrees = startIndex * deltaTheta
    theta = radians( thetaDegrees )
    thetaDegreesEnd = (startIndex+skip) * deltaTheta
    thetaEnd = radians( thetaDegreesEnd )

    #The (x,y) coordinates of the current nail.
    xStart = xCenter + radius * cos( theta )
    yStart = yCenter - radius * sin( theta )
    xEnd = xCenter + radius * cos( thetaEnd )
    yEnd = yCenter - radius * sin( thetaEnd )
    
    screen.create_line( xStart, yStart, xEnd, yEnd, fill = colors1[ startIndex % numColors1 ], width=2)
    sleep(0.01)
    screen.update()
       
for startIndex in range (0, numNails):
    thetaDegrees = startIndex * deltaTheta
    theta = radians( thetaDegrees )
    thetaDegreesEnd = (startIndex+skip+1) * deltaTheta
    thetaEnd = radians( thetaDegreesEnd )

    xStart = xCenter - radius * cos( theta )/1.65
    yStart = yCenter - radius * sin( theta)/1.65
    xEnd = xCenter - radius * cos( thetaEnd )/1.65
    yEnd = yCenter - radius * sin( thetaEnd )/1.65
    
    screen.create_line( xStart, yStart, xEnd, yEnd, fill = colors3[ startIndex % numColors3 ], width=2)
    sleep(0.01)
    screen.update()


for startIndex in range (0, numNails):
    thetaDegrees = startIndex * deltaTheta
    theta = radians( thetaDegrees )
    thetaDegreesEnd = (startIndex+skip) * deltaTheta
    thetaEnd = radians( thetaDegreesEnd )

    xStart = xCenter - radius * cos( theta * 2 )/2.9 
    yStart = yCenter - radius * sin( theta * 2)/2.9
    xEnd = xCenter - radius * cos( thetaEnd/2 )/2.9 
    yEnd = yCenter - radius * sin( thetaEnd/2 )/2.9

    screen.create_line( xStart, yStart, xEnd, yEnd, fill = colors2[ startIndex % numColors2 ], width=1)
    sleep(0.01)
    screen.update()       



