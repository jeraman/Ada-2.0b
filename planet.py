
##########################################################
##########################################################
# description: example that moves objects and set values fro numbers dynamically
#
# autor: jeraman
# date: 26/04/2010
##########################################################
##########################################################



#imports Pyata library
from pyata.pd import *
import math


#planet class for rotate boxes
class Planet():
    def __init__(self, radius, c_x, c_y, box):
        self.radius = radius
        self.c_x = c_x
        self.c_y = c_y
        self.box = box
        self.speed = 1
        self.angle = 0
    
    def set_speed(self, speed):
        self.speed = speed
    
    def move(self):
        self.angle = (self.angle+self.speed)%361
        angle =  math.radians(self.angle)
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        x+=self.c_x
        y+=self.c_y
        x = int(x)
        y = int(y)
        self.box.move(x, y)




#mains method
if __name__ == '__main__':
    
    #creates an instance of Pd
    pd = Pd()
    
    #initializes Pyata
    pd.init()
    
    #creates an object dac~ in 10, 10 on the patch
    dac = Object(10, 10, "dac~")
    #creates a planet to rotate boxes
    p1 = Planet(100, 300, 300, dac)
    
    #creates an oscillator
    osc = Object(dac.x+50, dac.y, "osc~")
    #creates another planet for the osc
    p2 = Planet(50,dac.x, dac.y, osc)
    p2.set_speed(5)
    
    #conencts osc to dac
    connect(osc, 0, dac, 0)
    
    #creates a number t control the synth
    centro=Number(300, 300)
    centro.set(440)
    
    #connects all numbers to osc
    connect(centro, 0, osc, 0)

    #init numbers used during the rotation
    i = 0
    j = 0
    
    #the main loop to rotate
    for time in range(600):
        #i = (i+1)%361
        p1.move()
        p2.c_x = dac.x
        p2.c_y = dac.y
        #j = (j+5)%361
        p2.move()
        centro.set(440+j)
        sleep(0.05)
        
        
    #finishes Pyata
    pd.quit()
    
   