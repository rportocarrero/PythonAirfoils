import numpy as np
import matplotlib.pyplot as plt
import math
import random
import struct
import time
import WingArea

s = struct.Struct('ffff')
fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-.2, 2), ylim=(-1, 2))

class Population():
    
    def initPop(self,n):
        for i in range(n):
            span =      random.random()
            rc = random.random()
            tc = random.uniform(0,rc) # tip chord never larger than root chord
            swp = random.uniform(0,math.pi/2) # no forward sweep
                
            chromosome = s.pack(span,rc,tc,swp)
            self.individuals.append(chromosome)
            self.length+=1
            """
            print(chromosome)
            ch = s.unpack(chromosome)
            print(ch)
            """
            
    def __init__(self):
        self.length = 0
        self.individuals = []
        self.index = 0

pop = Population()
pop.initPop(50)

def getvertices(span,rootChord,tipChord,sweepAngle):
    rootLeadingEdge = [1,1]
    rootTrailingEdge = [1,rootChord]
    tipLeadingEdge = [span, (.25*rootChord+math.cos(sweepAngle)-(0.25*tipChord))]
    tipTrailingEdge = [span, tipLeadingEdge[1]+tipChord]
    return [rootLeadingEdge,rootTrailingEdge,tipTrailingEdge,tipLeadingEdge]


def viewIndividual(ch):
    ax.clear()
    [span,rc,tc,swp] = s.unpack(ch)
    wingVertices = getvertices(span,rc,tc,swp)
    wing = plt.Polygon(wingVertices)
    wing.set_facecolor(None)
    body = plt.Polygon([[0,2],[0,-1],[-1,-1],[-1,2]])
    #plt.title(ch.decode(encoding="utf-8"))
    ax.add_patch(wing)
    ax.add_patch(body)
    fig.canvas.draw()
    area = WingArea.wingArea(wingVertices)
    AR = ((2*span)**2)/(2*area)
    print("Area: "+str(2*area)+" b: "+str(2*span)+" AR: "+str(AR))

# Function to be called when mouse is clicked
def on_click(event):
    if pop.index < pop.length:
        viewIndividual(pop.individuals[pop.index])
        pop.index+=1


# Connect the click function to the button press event
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()

    

