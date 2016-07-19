from random import*
'''
size(400,400)
    ellipse(100,20,40,40):
    def setup():
    PImage img;
    img = loadImage("black-ops-3-341.png");
    img.resize(width,height);
    background(img)
def draw():
    x = 0
    y = 3'''
'''c = color(0)
x = 0.0
y = 100.0
speed = 1.0'''

def setup():
  size(200, 200)
  

'''def draw():
    background(255)
    global x
    global y
    ellipse(x,200,40,40)
    x = x + speed
    if (x > width - 40 or x<40):
        x = 0
        x = x + speed'''
c = color(0)
x = 100
y = 10
xdir = True
ydir = True
speed = 6

def draw():
  background(255, 255, 100)
  global x
  global y
  
  global speed
  global xdir
  global ydir

  if x == 180:
      xdir = False
  elif x == 0:
      xdir = True
  if xdir == False:
      x -= 1
  elif xdir == True:
      x += 1
      
  if y == 185:
    ydir = False
  elif y == 0:
      ydir = True

  if ydir == False:
      y-=1
  elif ydir == True:
      y+=1

  if x > mouseX-20 and x < mouseX+20 and y > 175:
    y +=1
    
  fill(randrange(255))
  rect(mouseX, 190, 40, 10)
  ellipse(x,y,30,30)
  stroke(randrange(255))