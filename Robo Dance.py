init("sim")
    
for seconds in timer(2):
    turnBy(270, "deg")
    turnBy(90, "deg")
    
    
   ## i =0

## while i < 2:      # Robot "Clapping"
##     beep(.1233333, 900)
##     wait(0.7)
##     beep(.1233333, 900)
##     wait(0.3)
##     beep(.1233333, 900)
##     wait(0.4)
##     beep(.5, 900)
##     wait(1.6)
##     i = i + 1
for seconds in timer(1):   #To the left
    rotate(10)
    stop()
wait(1)
backward(3,.3)
wait(1)
forward(5,.3)           #one hop this time
wait(1)
motors(0,1)
wait(1)
motors (1,0)
wait(1)
                     #cha chat real smooth
t = 0
while t < 2:
    backward(10, 1.99)
    turnRight(.1, .3)
    turnLeft(.1, .3)
    t = t + 1






from Myro import *
init ("sim")
x = 0
for x in range(0, 4):
    beep(.233333,900)






i = 0
while i < 6:
    beep(.233333, 900)
    i = i + 1
for seconds in timer(2): motors(0,1) 
stop()
t = 0
while t > 2:
    backward(10, 1.99)
    turnRight(.1, .3)
    turnLeft(.1, .3)
    t = t + 1
    
    
    
    
    
