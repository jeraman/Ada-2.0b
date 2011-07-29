

##########################################################
##########################################################
# description: example that works with connection/disconnections of boxes
#
# autor: jeraman
# date: 26/04/2010
##########################################################
##########################################################

#imports Pyata library
from pyata.pd import *
import math


    

#planet class for rotate boxes
class Clock():
    def __init__(self, radius, center, processes, lifetime, inlet=0):
        self.radius = radius
        self.center = center
        self.inlet = inlet
        self.list = []
        self.pointer = 0
        self.processes = processes
        self.draw()
        self.lifetime = lifetime
        
    def increment(self):   
        self.lifetime=self.lifetime-1
        disconnect(self.list[self.pointer][0], 0, self.center[0], self.inlet)
        self.pointer = (self.pointer+1)%len(self.processes)
        
        i = self.pointer
        exp = (float(self.processes[i][1])*100/pow(2,float(self.processes[i][1])/10))+110
        
        connect(self.list[self.pointer][0], 0, self.center[0], self.inlet)
        self.list[self.pointer][0].set(exp)
        
        
    def destroy(self):
        self.list.reverse()
        for b in self.list:
            b[0].delete()
            b[1].delete()
            sleep(0.1)
        for c in self.center:
            c.delete()
            sleep(0.1)
    
    def draw(self):
        q_boxes = len(self.processes)
        total = 360
        slice_angle = total/q_boxes
        angle = -90 - slice_angle
        
        for i in range(0,q_boxes):
            angle += slice_angle
            rad_angle = math.radians(angle)
            x = self.radius * math.cos(rad_angle)
            y = self.radius * math.sin(rad_angle)
            x+=self.center[0].x
            y+=self.center[0].y
            x = int(x)
            y = int(y)
            #print self.processes[i]
            n = Number(x, y)
            c = Comment(x, y-20, self.processes[i][0])
            #exp = (float(self.processes[i][1])*100/pow(2,float(self.processes[i][1])/10))+110
            #n.set(exp)
            self.list.append([n,c])
   