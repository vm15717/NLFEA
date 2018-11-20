# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def plotting_points():
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
    s.Spot(point=(-15.0, 5.0))


def line():
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
    s.Line(point1=(-15.0, 10.0), point2=(-5.0, 10.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(-5.0, 10.0), point2=(-5.0, 0.0))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.Line(point1=(-5.0, 0.0), point2=(-15.0, 0.0))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(-15.0, 0.0), point2=(-15.0, 10.0))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)


def spline():
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
    s.Spline(points=((-25.0, 15.0), (0.0, 15.0), (0.0, -10.0), (-25.0, -10.0), (
        -25.0, 15.0)))


def CreatingSets():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1149.86, 
        farPlane=1683.25, width=719.739, height=307.666, viewOffsetX=67.4581, 
        viewOffsetY=-20.4838)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
p = mdb.models['Model-1'].parts['Part-1']
n = p.nodes
nodes = n[0:1212] #Selects all the nodes, change to 1 node to force only that node
p.Set(nodes=nodes, name='Set-2')
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)


def ForcingofSets():
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
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-1-1'].sets['Set-2']
    mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf2=1.0, distributionType=UNIFORM, field='', 
    localCsys=None)

def INPEdit():
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
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(26, """
    ** ----------------------------------------------------------------
    * Step, name=exportmatrix
    *matrix generate, mass, stiffness
    *matrix output, mass, stiffness, format=matrix input
    *end step
    **""")
INPEdit()

def ImportingGeom():
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
    step = mdb.openStep(
        'C:/Users/tw15036/OneDrive - University of Bristol/Documents/Year 4/GIP/BeamGeom.stp', 
        scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='BeamGeom', geometryFile=step, 
        combine=False, mergeSolidRegions=True, dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['BeamGeom']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
ImportingGeom()

def Meshing():
p = mdb.models['Model-1'].parts['BeamGeom']
p.seedPart(size=6.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['BeamGeom']
p.generateMesh()
Meshing()



