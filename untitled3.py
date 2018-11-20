# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:06:33 2018

@author: mvrri
"""

# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    global task
    exec(open('symvar.py').read())
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
    
############Geometry
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(0.3, 0.2))
    s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(0.414811789989471, 
        0.107560992240906), value=0.2)
    s.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(0.160332977771759, 
        -0.0643089115619659), value=0.3)
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=Depth)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    ########Material Properties
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((210000.0, 0.3), 
        ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
        region=region, localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Part-1']
    n = p.nodes
    nodes = n.getSequenceFromMask(mask=('[#0 #400 ]', ), )
    p.Set(nodes=nodes, name='load')
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
        bcs=ON, predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-1-1'].sets['load']
    mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
        region=region, cf2=-1.0, distributionType=UNIFORM, field='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, optimizationTasks=ON, 
        geometricRestrictions=ON, stopConditions=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    mdb.Job(name='Job-2', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)
    mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
    task=0
    try:
      mdb.jobs['Job-2'].waitForCompletion(1000)
      print('Job Done')
      task=1
    except AbaqusException, message:
        print("Job Timed Out",message)
    session.mdbData.summary()
    o3 = session.openOdb(name='C:/temp/Job-2.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
Macro1()
#import time
#time.sleep(10)
 ####ODB extractions    
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
nodeset=MyPart.nodeSets['SET-1']
noderes=np.zeros(shape=[len(nodeset.nodes),4])
for w in range(len(nodeset.nodes)):
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
    stressres[k]=stressValues[k].maxPrincipal
resultf=np.concatenate((noderes,dispres),axis=1)
#Frequency
print(odb.steps['Frequency'].historyRegions['Assembly ASSEMBLY'].historyOutputs['EIGFREQ'])
with open('results2.csv','wb') as csvfile:
    filewriter=csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for i in range(len(noderes)):
        filewriter.writerow(resultf[i])
