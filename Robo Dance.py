from Myro import *
init ("COM*")
i = 0
while i < 6:
beep(.1233333, 900)
i = i + 1
for seconds in timer(2): motors(0,1) 
bacstop()
t = 0
while t > 2:
    backward(10, 1.99)
    turnRight(.1, .3)
    turnLeft(.1, .3)
    t = t + 1
    
    
    
    
    
from Myro import *
#for sliding
for seconds in timer(2):
    motors(0,1)
    stop()
for seconds in timer(2):
    motors(0,-1)
    stop()
for seconds in timer(2):
    motors(1,0)
    stop()
for seconds in timer(2):
    motors(-1,0)
    stop()
## ##for wiggle
## for seconds in timer(2):
##     motors(0,1)
##     stop()
## for seconds in timer(2):
##     motors(0,-1)
##     stop()
## for seconds in timer(2):
##     motors(1,0)
##     stop()
## for seconds in timer(2):
##     motors(-1,0)
##     stop()