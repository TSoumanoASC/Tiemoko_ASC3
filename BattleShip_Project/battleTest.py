


from random import *
def setup():
    size(500,500)

x = 0
y = 0
def draw():
    fill(randrange(255))
    global x
    global y
    for b in range(5):
        x=0
        for i in range(5):
            rect(x,y,100,100)
            x += 100
        y += 100 
        
def mousePressed():
    if mousePressed == True:
        ellipse(mouseX,mouseY,79,80)
        fill(255,0,0)
        
        print("KaBoom!!!!!!!!!")