from random import *
board = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]
#"S" stands for ships
board[int(randrange(4))][int(randrange(4))] = "S"
def setup():
    fill(50,90,90)
    size(500,500)
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100,j*100,100,100)
def draw():
   global yPos
   global xPos
def mousePressed():
    xPos = int(mouseX/100)
    yPos = int(mouseY/100)
    rect(xPos*100,yPos*100,100,100)
    if (board[yPos][xPos] =="S"):
        fill(17,23,122)
        print("Kaboom, Nice Shot")
    else:
        board[yPos][xPos] ="X"
        fill(0,255,0)
        print("Ya Miss Fool, Where ya Shot at")
    
    rect(xPos*100,yPos*100,100,100)
print(board)

    
    
    