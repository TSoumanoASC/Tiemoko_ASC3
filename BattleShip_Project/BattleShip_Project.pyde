from random import *
board = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]
#"S" stands for ships
board[int(randrange(5))][int(randrange(5))] = "S"
def setup():
    fill(50,90,90)
    size(500,500)
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100,j*100,100,100)
def draw():
    if(mouseButton == LEFT):
        xPos = int(mouseX/100)
        yPos = int(mouseY/100)
        board[yPos][xPos] ="X"
        fill(0,255,0)
        rect(xPos*100,yPos*100,100,100)
    
    print(board)