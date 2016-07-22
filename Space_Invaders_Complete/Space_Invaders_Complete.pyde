enemies=[["alive","alive","alive","alive","alive","alive"],["alive","alive","alive","alive","alive","alive"]]
bulletexist=False
bulletY = 600
XSpeed = 100
x= 1
y= 50
xdir = 1
# x is position of the enemy
def setup():
    size(700,700)

def draw():
    global k
    global d
    global bulletY , bulletexist
    global x
    global y
    global xdir
    global alive
    background(0,0,100)
    for m in range(len(enemies)):
        for i in range(len(enemies[m])):
            d = dist(XSpeed,bulletY,x+100*i,y+m*100)
            k= dist(XSpeed+90,bulletY,x+100*i,y+m*100)
            
            if enemies[m][i] == "alive":
                rect(x+100*i,y+m*100,50,50)
            if d<=50:
                enemies[m][i] = "dead"
                print("Hit")
                #bulletexist ="False"
            if k <= 50:
                enemies[m][i] = "dead"
                print("Hit")
    x = x + xdir
    if bulletexist==True: 
        fill(255,255,0)
        rect(XSpeed,bulletY,15,15)
        rect(XSpeed+90, bulletY,15,15)
        bulletY -= 30
    if bulletY <= 0 :
        bulletexist=False
        bulletY =600
    if x + 100*i >= 650:
        y += 50
        xdir *= -1
    if x  <= 0:
        y += 50
        xdir *= -1
    if y >= 590:
        x = 700
        y = 700
        textSize(40)
        text("You suck son",width/2,height/2)
        print("You Suck Son")
    
    
    
    fill(255,255,0)
    rect(XSpeed+25,630,50,50)
    rect(XSpeed,650,100,20)
    
    
    
    
    
def keyPressed():
    global bulletexist 
    fill(255,255,0)
    global XSpeed
    if key == "a":
        if XSpeed >=0 :
            XSpeed -= 30
    elif key == "d":
        if XSpeed <= 600:
            XSpeed += 30
    if keyCode == 32:
        bulletexist=True
        print ("hey")
    