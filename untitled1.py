# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:37:50 2018

@author: mvrri
"""
from abaqusConstants import *
from odbAccess import *
from textRepr import *
import numpy as np
import csv
odbName='Job-1'
odb=openOdb(odbName+'.odb',readOnly=True)
print(odb.steps)
step=odb.steps['Step-1']
frame=step.frames[-1]
output=frame.fieldOutputs
#Displacement
disp=output['U']
value=disp.values
MyPart=odb.rootAssembly.instances['PART-1-1']
nodeset=MyPart.nodeSets['SET-1']
noderes=np.zeros(shape=[len(nodeset.nodes),4])
for w in range(len(nodeset.nodes)):
    print(nodeset.nodes[w].coordinates)
    print(nodeset.nodes[w].label)
    coord=np.array(nodeset.nodes[w].coordinates,dtype=object)
    label=np.array(nodeset.nodes[w].label,dtype=object)
    noderes[w]=np.append(coord,label)
header1=np.array(['X','Y','Z','Label'],dtype=object)
noderes=np.vstack((header1,noderes))
loadnode=MyPart.nodeSets['LOAD']
MyPartdisp = disp.getSubset(region=MyPart) 
dispValues = MyPartdisp.values 
dispres=np.zeros(shape=[len(dispValues),1])
for k in  range(len(dispValues)):
    print(dispValues[k].magnitude)
    dispres[k]=np.array(dispValues[k].magnitude,dtype=object)
header2=np.array(['Displacement'],dtype=object)
dispres=np.vstack((header2,dispres))
#Stress
stress=output['S']
value=stress.values
Mypartstress=stress.getSubset(region=MyPart)
stressValues= Mypartstress.values
stressres=np.zeros(shape=[len(stressValues),1])
for k in  range(len(stressValues)):
    print(stressValues[k].maxPrincipal)
    stressres[k]=stressValues[k].maxPrincipal
resultf=np.concatenate((noderes,dispres),axis=1)
with open('results1.csv','wb') as csvfile:
    filewriter=csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for i in range(len(noderes)):
        filewriter.writerow(resultf[i])