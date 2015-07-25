############################################################################################
#Purpose:  This program creates an animation of Miku (a character) dancing in a disco room
#Prerequisites: Arrays and modular indexing
#Programmer: Rena Lu
#Last modified:  April 8, 2014
############################################################################################

#==================== Preparation & Imports ==================#

from random import *
from time import *
from tkinter import*
root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

# Create the ground
groundcolor=["Cyan", "Light Cyan"]
screen.create_oval(0, 500, 800, 900, outline="Cyan", width=40)
screen.create_oval(75, 550, 725, 825, outline="Light Cyan", width= 20)

# Import images of the dancing character
miku1 = PhotoImage(file = "1.gif")
miku2 = PhotoImage(file = "2.gif")
miku3 = PhotoImage(file = "3.gif")
miku4 = PhotoImage(file = "4.gif")
miku5 = PhotoImage(file = "5.gif")
miku6 = PhotoImage(file = "6.gif")
miku7 = PhotoImage(file = "7.gif")

miku = [miku1, miku2, miku3, miku4, miku5, miku6, miku7]

# Import images of the disco ball
ball1 = PhotoImage(file = "ball1.gif")
ball2 = PhotoImage(file = "ball2.gif")
ball3 = PhotoImage(file = "ball3.gif")
ball4 = PhotoImage(file = "ball4.gif")
ball5 = PhotoImage(file = "ball5.gif")
ball6 = PhotoImage(file = "ball6.gif")
ball7 = PhotoImage(file = "ball7.gif")
ball8 = PhotoImage(file = "ball8.gif")
ball9 = PhotoImage(file = "ball9.gif")
ball10 = PhotoImage(file = "ball10.gif")
ball11 = PhotoImage(file = "ball11.gif")
ball12 = PhotoImage(file = "ball12.gif")

ball = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10, ball11, ball12]

# Create Light Spots using arrays
numSpots = 20
spinspeed = 5
spotcolor = ["Red", "Yellow", "LawnGreen", "Cyan","Cyan",  "Magenta"]
spots = []
xspots = []

for x in range (0,9):
    xspots.append(100*x+10)

yspots = [200, 300, 400, 500, 600]
xspotsLR = []
yspotsLR = []
spotsize = []

for s in range (0, numSpots):
    spots.append(0)
    xspotsLR.append(0)
    yspotsLR.append(0)
    spotsize.append(randint(50, 80))

# Create Light Beams using arrays
numBeam = 5
movespeed = 10
beamcolor = ["Red", "Yellow", "LawnGreen", "Cyan", "Magenta"]

beam=[]
beamspeed = 10
xstart=800
ystart=800
xend1=-10
yend1=[]
yend2=[]
beamwidth=40
space=40

for b in range (0, numBeam):
    yend1.append((beamwidth+space)*b)
    beam.append(0)
    yend2.append(0)
    
beam2=[]
xstart2=0
ystart2=800
xend2=810
yend12=[]
yend22=[]

for b in range (0, numBeam):
    yend12.append((beamwidth+space)*b)
    beam2.append(0)
    yend22.append(0)

#Create the crowd
person = PhotoImage(file = "crowd.gif")
crowd = []
ycrowd = []
xcrowd = []
move = []
for i in range (0,30):
    crowd.append(0)
    xcrowd.append(i*40)
    ycrowd.append(800)
    move.append(randint(0, 20))

#================== Create the party! ====================#

for a in range (0, 500):
    
    # Draw the shining ground
    for dance in range (0, len(miku)):
        shine = dance%len(groundcolor)
        screen.create_oval(0, 500, 800, 900, outline=groundcolor[shine], width=40)
        screen.create_oval(75, 550, 725, 825, outline=groundcolor[1-shine], width= 20)

        phase = dance%len(ball)
        discoball = screen.create_image (400, 100, image=ball[phase])

        # Draw the light spots in the background
        for n in range (0, numSpots):
            colorspot = n%len(spotcolor)
            xspotsrepeat = n%len(xspots)
            yspotsrepeat = n%len(yspots)
            if xspots[xspotsrepeat]<800:
                xspots[xspotsrepeat]=xspots[xspotsrepeat]+spinspeed
                xspotsLR[n]=xspots[xspotsrepeat]+spotsize[n]
                yspotsLR[n]=yspots[yspotsrepeat]+spotsize[n]
                spots[n]=screen.create_oval(xspots[xspotsrepeat], yspots[yspotsrepeat], xspotsLR[n], yspotsLR[n], fill=spotcolor[colorspot],outline=spotcolor[colorspot])
            else:
                xspots[xspotsrepeat]=0
                
        # Draw the dancing Miku
        posture = dance%len(miku)
        dancingmiku = screen.create_image (400, 500, image=miku[posture])

        # Draw the light beams shooting from two sides
        for b in range (0, numBeam):
            yend1[b]=yend1[b]+(b+2)*beamspeed
            yend2[b]=yend1[b]+beamwidth
            beam[b]=screen.create_polygon(xstart, ystart, xend1, yend1[b], xend1, yend2[b], fill=beamcolor[b],outline=beamcolor[b])

        for b in range (0, numBeam):
            yend12[b]=yend12[b]+(b+2)*beamspeed
            yend22[b]=yend12[b]+beamwidth
            beam2[b]=screen.create_polygon(xstart2, ystart2, xend2, yend12[b], xend2, yend22[b], fill=beamcolor[b],outline=beamcolor[b])

        #Draw the cheering crowd
        for c in range (0, 30):
            ycrowd[c] = ycrowd[c]-move[c]
            crowd[c]=screen.create_image(xcrowd[c], ycrowd[c], image=person)
            
        screen.update()
        sleep(0.05)

        # Delete the spots, beams and crowd to make them appear moving 
        for n in range (0, numSpots):
            screen.delete(spots[n])
            
        for b in range (0, numBeam):
            screen.delete(beam[b])
            screen.delete(beam2[b])
            if a%10==0:
                if yend1[b] >= 800:
                    yend1[b]=yend1[b]-1600
                if yend12[b] >= 800:
                    yend12[b]=yend12[b]-1600
                    
        for c in range (0, 30):
            screen.delete(crowd[c])
            if ycrowd[c]<=780:
                ycrowd[c]=800

        # Delete Miku and discoball everytime to make them appear moving
        screen.delete(dancingmiku, discoball)
        


