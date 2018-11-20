
from abaqus import *
from abaqusConstants import *
import __main__

def TextOutput():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    from abaqusConstants import *
    from odbAccess import *
    from textRepr import *
    import numpy as np
    import csv
    import os, sys
    ## Load ODB file
    odb=openOdb('C:/temp/Frequency.odb')
    frame=odb.steps['Frequency'].frames
    for i in range(len(frame)):
        Filename='Mode' +str(i)+ '.txt'
        f=open(Filename,'wt')
        f.write('[U1, U2, U3] \n')
        for j in range(len(frame[i].fieldOutputs['U'].values)):
            nodemag=frame[i].fieldOutputs['U'].values[j].data
            f.write(str(nodemag) + '\n')
        f.close        
    f=open('EIGFREQ.txt', 'wt')
    f.write('(Mode, Freq.)\n')
    for i in range(len(frame)-1):
        f.write(str(odb.steps['Frequency'].historyRegions['Assembly ASSEMBLY'].historyOutputs['EIGFREQ'].data[i]) + '\n')
    f.close
    os.rename('Frequency.inp','Frequency.txt')
    
TextOutput()


    


        


