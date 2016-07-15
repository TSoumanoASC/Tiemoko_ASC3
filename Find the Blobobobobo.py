from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 200 and getGreen(pixel) == 0 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel)== 0 and getGreen(pixel) > 90 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) == 0 and getGreen(pixel) == 0 and getBlue(pixel) > 200):
          
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 180 and getGreen(pixel) > 180 and getBlue(pixel) == 0):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel



# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################
Color = 4
x = 0
pic = takePicture()
#show(pic)
findColorSpot(pic, Color)
x = findColorSpot(pic, Color)
while x < 120 :
    turnBy(45, "deg")
    # not finding the color on the picture you took
    pic = takePicture()
    #show(pic)
    x = findColorSpot(pic, Color)
    print(" x is now: ",x)
    #turnBy(45, "deg")
forward(4, 1)     

nextColor = input("Whats the next color?")
x = 0
## print(newColor)
backward(4, 1)
newColor = 1
pic
findColorSpot(pic, newColor)
x  = findColorSpot(pic, newColor)
while x != 0:
    turnBy(45, "deg")
    pic
    show(pic)
    findColorSpot(pic, newColor)
    x = findColorSpot(pic, newColor)
    print(" x is now set:", x)
turnBy(90, "deg")
forward(4, 1)
#move back to center (maybe)
#findColorSpot(pic, newColor)


#to make the sim run correctly set what color shoudl equal to, and then make the while statement
# not equal to which is != and when you set the color it will give you the x what is should 
#equal to so you just put while x != 3: so you then change it to the said number it gives for
#the color and put x < the number


## After finding the first color we triede to make it ask what color next by inserting
## newColor = input("whats the next color")
## and placing thing back to center and run pic and scan again to move to next color.