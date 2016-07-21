XSpeed= 100
def setup():
    size(700,700)

def draw():
    background(255)
    rect(50,50,50,50)
    rect(150,50,50,50)
    rect(250,50,50,50)
    rect(350,50,50,50)
    rect(450,50,50,50)
    rect(550,50,50,50)
    rect(650,50,50,50) 
    fill(255,255,255)
    if  XSpeed >= 600:
        fill(255,255,255)
        rect(600,650,100,50)
    else:
        rect(XSpeed,650,100,50)
def keyPressed():
    global XSpeed
    if key == "a":
        XSpeed -= 10
    elif key == "d":
        XSpeed += 10
    
    
    
    fill(255)
    rect(XSpeed,650,100,50)
    if  XSpeed >= 600:
        rect(600,650,100,50)
    else:
        rect(XSpeed,650,100,50)
    