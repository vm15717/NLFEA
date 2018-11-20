from abaqusConstants import *
from odbAccess import *
from textRepr import *
import numpy as np
import csv
odb=openOdb('C:/temp/Frequency.odb')
print(odb.steps)
step=odb.steps['Frequency']
frame=step.frames[-1]
output=frame.fieldOutputs
#Displacement
disp=output['U']
value=disp.values
MyPart=odb.rootAssembly.instances['BEAM-1']
#nodeset
nodeset=MyPart.nodeSets['SET-1']
noderes=np.zeros(shape=[len(nodeset.nodes),4])
nodeset=MyPart.nodeSets['SET-1']
for w in range(len(nodeset.nodes)):
    coord=np.array(nodeset.nodes[w].coordinates,dtype=object)
    label=np.array(nodeset.nodes[w].label,dtype=object)
    noderes[w]=np.append(coord,label)
header1=np.array(['X','Y','Z','Node number'],dtype=object)
noderes=np.vstack((header1,noderes))
#Displacement
dispframe=np.zeros(shape=[len(step.frames),1],dtype=object)
for i in range(len(step.frames)):
    frame=step.frames[i]
    output=frame.fieldOutputs
    disp=output['U']
    dispres=np.zeros(shape=[len(disp.values),3])
    for j in range(len(disp.values)):
        dispres[j]=np.array(disp.values[j].data,dtype=object)
    dispframe[i]=[dispres];
#freq
print(odb.steps['Frequency'].HistoryRegion)
