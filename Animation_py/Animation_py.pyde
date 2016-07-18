from random import *
def setup():
    size(400, 400)
def draw():
    strokeWeight(10)
    stroke(randrange(255),randrange(255) ,randrange(255))
    line(mouseX, mouseY, 10, 10)
    
def mousePressed(): 
    randshape = randint(0,3)
    if randshape == 0:
        ellipse (mouseX,mouseY,30, 46)
    elif randshape == 1:
        rect(mouseX,mouseY,30,46)
    elif randshape ==2:
        quad(mouseX,mouseY, 20, 34, 200, 69,54,50)
    elif randshape ==3:
        triangle(mouseX, mouseY, 158, 20, 100, 75)
    
    
    strokeWeight(2)