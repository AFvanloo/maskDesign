import gdsCAD as cad
import numpy as np
import defaultParms as dpars
import maskDesign as md
import sys
from matplotlib import pyplot as plt


print 'loading PCBClass'
#Units are nm, so to use um, multiply by 1000
um = 1e3
mm = 1e6

#default border and launcher configuration options:
borderTagList, offCenters = dpars.dLists()

#Default component design values
defaults = dpars.dPars()

class PCB:

    def __init__(self, PCBSize=30*mm, shape=2, mmpxLocs=[4,0,0,0],chipSize = (10*mm,5*mm), chipLocation=(0,0), chipConfig='D', chipRot=90):
        '''
        constructor of the PCB class

        PCBsize is the PCB diameter in mm

        Use the layers as follows:
            layer 0 is for lithography
            layer 1 is for drilling

        PCBOffcenter is about where to space the milling holes
        '''
        #properties
        self.fileName = 'testPCB.gds'
        self.size = PCBSize
        self.shape = shape

        #CPW properties
        self.a1 = .2*mm
        self.abr = 3
        self.rbend = defaults['PCBrbend']

        #chip properties
        self.chipSize = chipSize
        self.chipConfig = chipConfig
        self.offCenters = offCenters
        self.chipRot = 90

        #mmpx positions: a list for shape 2 or a number for shape 1
        self.mmpxLocs = mmpxLocs
        self.mmpxLoc = []

        self.viaPositions = []
        self.screwPositions = []
        self.PCBOffCenter = PCBOffCenter
        
        #components
        self.CPWs = 0
        self.MMPXs = 0
        self.vias = 0
        self.chips = 0
        self.arcs = 0
        self.screwHoles = 0
        
        #Initialize
        self.initPCB()
        self.addChip(chipLocation)


    def initPCB(self):
        '''
        construct a PCB
        '''
        #make the cell
        self.topCell = cad.core.Cell('TOP')
        self.layout = cad.core.Layout('SAMPLE')
        self.layout.unit = 1e-9

        #determine shape
        if self.shape == 1:
            print 'shape 1'
            self.Shape1()
        if self.shape == 2:
            print 'shape 2'
            self.Shape2()


    def Shape1(self):
        shapeCell = md.PCBShape1(self.size)
        self.topCell.add(shapeCell)


    def Shape2(self):
        '''
        mmpx = number of mmpx connectors for each side (clockwise from 12)
        '''
        shapeCell = md.PCBShape2(self.size)
        self.topCell.add(shapeCell)
        self.addEdgeMMPXs()


    def addChip(self, placeInfo = (0,0), vias=True):
        '''
        adds a chip at placeInfo
        according to properties already set in the PCB class
        '''

        print 'adding a chip to the PCB'

        self.chips += 1
        setattr(self, 'Chip'+str(self.chips), Chip(self, placeInfo, vias=vias))


    def addScrewHole(self, coords):
        '''
        Adds a screw hole
        '''

        print 'adding a screw hole'

        self.screwHoles += 1
        self.screwPositions.append(coords)
        setattr(self, 'Screw'+str(self.screwHoles), ScrewHole(self, coords))


    def addEdgeMMPXs(self):
        '''
        adds EdgeMMPX connector thingies as defined when calling the PCB class
        will cause problems when using the top/bottom AND sides
        '''

        print 'adding MMPX connectors'

        mx, my = defaults['MMPXEdge']
        px, py = self.size

        #top, bottom
        for i in [0,2]:
            num = self.mmpxLocs[i]
            if num == 0:
                continue
            dis = (px)/(num)
            xs = np.arange(-(num-1)*dis/2, dis/2 + (num-1)*dis/2, dis)
            y = (py-my)/2*(1-i) 
            crot = 90*(-i)
            for x in xs:
                self.mmpxLoc.append([x,y])
                self.addEdgeMMPX([x,y], rot=crot)

        #sides
        for i in [1,3]:
            num = self.mmpxLocs[i]
            if num == 0:
                continue
            dis = (py-my)/(num-1)
            x = (px-my)/2*(2-i)
            ys = np.arange(-num/2*dis + dis/2, dis/2 + num/2*dis, dis)
            crot = 90*(-i)
            for y in ys:
                self.mmpxLoc.append((x,y))
                self.addEdgeMMPX((x,y), rot=crot)

 
    def addEdgeMMPX(self, placeInfo, rot=0):
        '''
        Add a single MMPX edge connector
        '''

        self.MMPXs += 1
        setattr(self, 'mmpxEdge'+str(self.MMPXs), EdgeMMPX(self, placeInfo, rot=rot))




    def addCPW(self, leng, placeInfo, flip=False, vias=True, rot=0):
        '''
        add a CPW line

        Input the length in nm

        PlaceInfo can be either a location or the connector of an object.
        Examples:
            (x, y)
            'launcher1.connect'

        Flip is used when connecting to a component situated to the right of the
        CPW. By default flip is off, meaning a CPW is added to a component on
        its left
        '''

        #Keep track of the number of lines
        self.CPWs +=1
        setattr(self, 'CPW'+str(self.CPWs), CPW(self,leng, placeInfo, flip, vias, rot))


    def addLine(self, placeInfo1, placeInfo2):
        pass

   
    def addArc(self, initAngle, degrees, placeInfo, flip=False, rbend=None, name = None,
            vias=False, rot=0):
        '''
        Wrapper for Arc:

        rbend is set to 100um by default. initAngle is the initial angle at
        which the bend starts, similar to in the unit circle. 
        
        degrees is the amount angle between start and end

        The flip option is used when placeInfo is a connector. In that case,
        flip toggles which side of the arc connects to the given connector
        '''

        #Default values
        if rbend == None: rbend = self.rbend
        
        print 'adding an Arc'
        self.arcs += 1
        #create launchers according to the list 'launcherpositions'
        setattr(self, name if name else 'arc'+str(self.arcs), Arc(self, initAngle, degrees,
            placeInfo, flip, rbend, vias, rot))


#    def pcbRoute(self, placeInfo1, placeInfo2, rot1=0, rot2=90):
#        '''
#        Draw a CPW from placeInfo1 to placeInfo2
#
#        startrot is an optional starting rotation that can be used with
#        placeInfo1 being an object, but when the rotation needs to be different
#        from that objects rotation
#        '''
#
#        #Get coordinates for placeInfo1
#        if type(placeInfo1) == str:
#            comp = getattr(self, placeInfo1.split('.')[0])
#            self.startcoords = getattr(comp, placeInfo1.split('.')[1])
#        else:
#            self.startcoords = placeInfo1
#            self.startrot = rot1 
#        print 'startrot is ', self.startrot
#
#        #Get coordinates for placeInfo2
#        if type(placeInfo2) == str:
#            comp = getattr(self, placeInfo2.split('.')[0])
#            self.endcoords = getattr(comp, placeInfo2.split('.')[1])
#            self.endrot = getattr(comp, 'rot')
#        else:
#            self.endcoords = placeInfo2
#
#        #going up
#        if self.startcoords[1] < self.endcoords[1]:
#            pass
#


    def route(self, placeInfo1, placeInfo2, rot1=None, vias=True, endrot=0):
        '''
        Draw a CPW from coords1 to coords2

        This function assumes that the final rotation is the same as the initial
        rotation

        In case placeInfo is a set of coordinates for component 1, the rotation
        at the start can be given in as rot1 (in degrees)

        startrot is an optional starting rotation that can be used with
        placeInfo1 being an object, but when the rotation needs to be different
        from that objects rotation
        '''

        #Get coordinates for placeInfo1
        if type(placeInfo1) == str:
            comp = getattr(self, placeInfo1.split('.')[0])
            self.startcoords = getattr(comp, placeInfo1.split('.')[1])
            self.startrot = getattr(comp, 'rot') - 90
        else:
            self.startcoords = placeInfo1
            self.startrot = 0
        if rot1 != None:
            self.startrot = rot1

        print 'startrot is ', self.startrot

        #Get coordinates for placeInfo2
        if type(placeInfo2) == str:
            comp = getattr(self, placeInfo2.split('.')[0])
            self.endcoords = getattr(comp, placeInfo2.split('.')[1])
        else:
            self.endcoords = placeInfo2

        dx = self.endcoords[0] - self.startcoords[0]
        dy = self.endcoords[1] - self.startcoords[1]

        print 'startcoordsx, endcoordsx are ', self.startcoords

        #Re-express as an upgoing problem
        if self.startrot%90 != 0:
            raise ValueError, 'Use only multiples of 90 degrees when connecting a line'

        if self.startrot == 90: #nothing changes
            tdx = dx
            tdy = dy
            rotBack = 0
        elif self.startrot == 180:
            tdx = dy
            tdy = -dx
            rotBack = 90
        elif self.startrot == 0:
            tdx = -dy
            tdy = dx
            rotBack = 270
        elif self.startrot == 270 or -90:
            tdx = -dx
            tdy = -dy
            rotBack = 180

        print 'tdx, tdy are', tdx, tdy
        print 'rotBack is ', rotBack

        if endrot == 'l': 
            tdx += self.rbend
            tdy -= self.rbend
        if endrot == 'r': 
            tdx -= self.rbend
            tdy -= self.rbend

        routeCell, allViaLocs = md.CPWroutePCB(self.startcoords, tdx, tdy, rot = rotBack,
                chipWidth=self.size[1], bridges=False, vias=vias)
        self.viaPositions.extend(allViaLocs)

        self.topCell.add(routeCell)

    def addRandomVias(self):
        '''
        adds vias to unoccupied places
        '''
        print 'length is ', len(self.viaPositions)
        
        #load design constants
        ivD = defaults['interviaDistance']
        rvD = defaults['randomViaDistance']
        ihD = defaults['viaHorizDistance']
        PCBSize = self.size

        rViaCell = cad.core.Cell('RANDOMVIA')

        #pick a random starting spot:
        x1s = np.arange(-PCBSize[0]/2+rvD/2,PCBSize[0]/2-ihD, rvD)
        x2s = np.arange(-PCBSize[0]/2+rvD,PCBSize[0]/2-ihD, rvD)
        ys = np.arange(-PCBSize[1]/2+rvD/2,PCBSize[1]/2-ihD, np.cos(rad(30))*rvD)
        counter=0
        for y in ys:
            xlist = [x1s, x2s][counter%2]
            counter += 1
            for x in xlist:
                rcoords = np.array([x,y]) #+ np.random.random(2)*[rvD, rvD]
                if not self.Forbidden(rcoords):
                    newVia = md.Via(rcoords)
                    rViaCell.add(newVia)
                    self.viaPositions.append(rcoords)

        self.topCell.add(rViaCell)


    def Forbidden(self, coords):
        ''' 
        checks if a point is within interviaDistance of an MMPX connector or a chip
        '''

        #design values
        mmpxSize = defaults['MMPXEdge']
        ivD = defaults['interviaDistance']
        rvD = defaults['randomViaDistance']
        ihD = defaults['viaHorizDistance']
        sd = defaults['PCBScrewHole']
        x, y = coords
        chipSize = self.chipSize

        #check for mmpx connectors
        for m in range(1,self.MMPXs+1):
            #get location
            cmmpx = getattr(self, 'mmpxEdge'+str(m))
            mx, my = cmmpx.coords
            mrot = cmmpx.rot
            if abs(x-mx) < (abs(np.cos(rad(mrot))*mmpxSize[0]/2) + abs(np.sin(rad(mrot))*mmpxSize[1]/2)) + 2*ihD:
                if abs(y-my) < (abs(np.cos(rad(mrot))*mmpxSize[1]/2) + abs(np.sin(rad(mrot))*mmpxSize[0]/2)) + 2*ihD:
                    return True

        #check for chips
        for c in range(1,self.chips+1):
            #get location
            cchip = getattr(self, 'Chip'+str(c))
            cx, cy = cchip.coords
            crot = cchip.rot
            if abs(x-cx/2) < (abs(np.cos(rad(crot))*chipSize[0]/2) + abs(np.sin(rad(crot))*chipSize[1]/2)) + 2*ihD:
                if abs(y-cy/2) < (abs(np.cos(rad(crot))*chipSize[1]/2) + abs(np.sin(rad(crot))*chipSize[0]/2)) + 2*ihD:
                    return True
        
        #check for other vias:
        for i in range(len(self.viaPositions)):
            vx, vy = self.viaPositions[i]
            if np.sqrt(np.power((x-vx),2)+np.power((y-vy),2)) < 2*ihD:
                return True

        #check for other screwHolesvias:
        for i in range(len(self.screwPositions)):
            sx, sy = self.screwPositions[i]
            if np.sqrt(np.power((x-sx),2)+np.power((y-sy),2)) < sd/2+ihD:
                return True
        return False



#====================================================================
#--------------------PCB--UTILITIES---------------------------------
#===================================================================


    def make_drillfile(self):
        pass

    def save(self):
        self.layout.add(self.topCell)
        self.layout.save(self.fileName)
    
    def show(self):
        self.layout.add(self.topCell)
        self.layout.show()

    def showLayer(self, layer=0):
        '''
        Move the layer of choice into a second cell and display it
        '''
        c1, c2 = cad.utils.split_layers(self.topCell, [layer])
        c2.show()


    def str_to_class(st):
        '''
        Takes a string, returns the class of the name str
        '''
        return getattr(st)


#=======================================================================
#-------------------------Components------------------------------------
#=======================================================================

class Chip:

    def __init__(self, PCBX, placeInfo, vias):

        #properties
        self.coords = placeInfo
        self.chipSize = PCBX.chipSize
        self.rot = PCBX.chipRot
        self.launcherConfig = PCBX.chipConfig
        self.vias = vias

        #connectors
        posNoAngle = []
        offs = PCBX.offCenters[self.launcherConfig]
        borX, borY = self.chipSize
        if self.launcherConfig == 'D':
            offX1, offX2 = offs
            #get all the positions
            posNoAngle.extend([[-offX1,borY/2,-90],[-offX2,borY/2,-90],[offX2,borY/2,-90],[offX1,borY/2,-90],[offX1,-borY/2,90],[offX2,-borY/2,90],[-offX2,-borY/2,90],[-offX1,-borY/2,90]])
            print 'posNoAngle is ', posNoAngle
            #rotation
            phi = rad(self.rot)
            pos = [[c[0]*np.cos(phi)+c[1]*np.sin(phi), 
                c[1]*np.cos(phi)-c[0]*np.sin(phi),c[2]+self.rot] for c in posNoAngle]
            for i in range(len(pos)):
                setattr(self, 'connect'+str(i), pos[i])
            
        else:
            raise Exception, 'Only chip configuration D is implemented so far'

        #draw and add Cell
        if self.vias:
            self.Cell, viaLocs = md.chip(self.coords, self.chipSize, vias=self.vias, rot=self.rot)
            PCBX.viaPositions.extend(viaLocs)
        else:
            self.Cell = md.chip(self.coords, self.chipSize, vias=self.vias, rot=self.rot)
        PCBX.topCell.add(self.Cell)


class ScrewHole:

    def __init__(self, PCBX, placeInfo):

        #properties
        self.coords = placeInfo#
        self.diameter = defaults['PCBScrewHole']

        self.Cell = md.screwHole(self.coords, self.diameter)
        PCBX.topCell.add(self.Cell)



class EdgeMMPX:

    def __init__(self, PCBX, placeInfo, vias=True, rot=0):
        '''
        initialize an MMPX Edge connector
        '''

        #init properties
        self.coords = placeInfo
        self.rot = rot
        self.vias = vias

        #make the cell
        mx, my = defaults['MMPXEdge']
        self.connect = (self.coords[0] + my/2*np.sin(rad(self.rot)),
            self.coords[1] - my/2*np.cos(rad(self.rot)))

        #draw and add the cell
        self.Cell, viaLocs = md.MMPXEdge(self.coords, rot=self.rot)
        PCBX.viaPositions.extend(viaLocs)
        PCBX.topCell.add(self.Cell)


class CPW:

    def __init__(self, PCBX, leng, placeInfo, flip, vias, rot):
        '''
        Initialize the object
        '''

        self.leng = leng
        self.flip = flip
        self.rot = rot
        
        #via properties
        self.vias = vias
        self.viaDiameter=defaults['viaDiameter']
        self.interviaDistance = defaults['interviaDistance']
        self.viaHorizDistance = defaults['viaHorizDistance']

        
        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(PCBX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for size of device
            if self.flip:
                self.coords = (self.cp[0] - self.leng/2.*np.cos(rad(self.rot)),
                        self.cp[1] - self.leng/2.*np.sin(rad(self.rot)))
            else:
                self.coords = (self.cp[0] + self.leng/2.*np.cos(rad(self.rot)),
                        self.cp[1] + self.leng/2.*np.sin(rad(self.rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #CPW is now centered, so connector A is just given by the coordinates
        self.connectA = (self.coords[0] - self.leng/2.*np.cos(rad(rot)),
                self.coords[1] + self.leng/2.*np.sin(rad(rot)))
        self.connectB = (self.coords[0] + self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] - self.leng/2.*np.sin(rad(rot)))

        self.makeCell(PCBX)
        if self.vias:
            PCBX.viaPositions.extend(self.viapos)
        else:
            self.Cell = self.makeCell(PCBX)

        #Add the CPW cell to the TopCell
        PCBX.topCell.add(self.Cell)
        
    def makeCell(self, PCBX):
        '''
        make the cad Cell reference of the CPW
        '''
        print 'drawing a CPW of ', self.leng/1e6, ' mm long' 
        #making the cell
        cellInfo = md.CPW(self.coords,self.leng, center=PCBX.a1,
                gap=PCBX.a1*PCBX.abr,vias=self.vias,rot=self.rot)
        if self.vias:
            self.Cell, self.viapos = cellInfo
        else:
            self.Cell = cellInfo


class Arc:

    def __init__(self, PCBX, initAngle, degrees, placeInfo,flip, rbend, vias, rot):
        '''
        Construct an Arc
        '''
        
        #attributes
        self.initAngle = initAngle
        self.degrees = degrees
        self.rbend = rbend
        self.rot = rot
        self.vias = vias

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(PCBX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            if flip:
                self.coords = (self.cp[0] -
                        self.rbend*(np.cos(rad(self.initAngle+degrees+self.rot))),
                    self.cp[1] -
                    self.rbend*np.sin(rad(self.initAngle+degrees+self.rot)))
            else:
                self.coords = (self.cp[0] -
                        self.rbend*(np.cos(rad(self.initAngle+self.rot))),
                    self.cp[1] - self.rbend*np.sin(rad(self.initAngle+self.rot)))
        else:
            #its coordinates
            self.coords = (placeInfo[0] +
                    self.rbend*(np.cos(self.initAngle+self.rot)),
                placeInfo[1] - np.cos(self.initAngle+self.rot))

        dxA = self.rbend*np.cos(rad(initAngle+self.rot)) 
        dxB = self.rbend*np.cos(rad(initAngle+degrees+self.rot))
        dyA = self.rbend*np.sin(rad(initAngle+self.rot))
        dyB = self.rbend*np.sin(rad(initAngle+degrees+self.rot)) 
            
        #Connector locations
        if flip:
            self.connectB = (self.coords[0] + dxA, self.coords[1] + dyA)
            self.connectA = (self.coords[0] + dxB, self.coords[1] + dyB)
        else:
            self.connectA = (self.coords[0] + dxA, self.coords[1] + dyA)
            self.connectB = (self.coords[0] + dxB, self.coords[1] + dyB)

        #make the cell
        self.makeCell(PCBX)


    def makeCell(self,PCBX):
        '''
        make the cad Cell reference of the CPW
        '''
        cellInfo = md.CPWArc(self.coords, self.initAngle, self.degrees,
                center =PCBX.a1, gap=PCBX.abr*PCBX.a1,  radius=self.rbend, vias=self.vias, rot = self.rot)
        if self.vias:
            self.Cell, pos = cellInfo
            PCBX.viaPositions.extend(pos)
        #Add the cell to the TopCell
        PCBX.topCell.add(self.Cell)



#==========================================================================
#-------------------------------UTILITIES----------------------------------
#==========================================================================
        
def rad(degrees):
    '''
    translates degrees to radians
    '''
    return degrees * 2 * np.pi / 360.


def arcrad(radians):
    '''
    translates degrees to radians
    '''
    return radians * 360 / 2 / np.pi 
<<<<<<< HEAD


def splitLayer(cell, layer):
    c1, c2 = cad.utils.split_layers(cell, [layer])
    return c2

def showLayers(cell, layers=[0,1,2]):
    '''
    Show the indicated layers

    Watch out: this function eats a cell (and layers to be shown), not a PCB object
    '''
    for l in range(len(layers)):
        lc = splitLayer(cell, layers[l])
        lc.show()


def makeDrillFile(PCB, PCBSize, viaLocations, screwLocations, fname = './PCBsGen1/drillFile.dlr'):
    '''
    make a drill file
    '''

    #open a file
    f = open(fname, 'w')

    f.write('M48\n') #This is where the header starts
    f.write('METRIC,LZ\n')

    #tool size
    vd = defaults['viaDiameter']
    sh = defaults['PCBScrewHole']
    f.write('T01C'+('%3.3f' % (vd/1e6)).zfill(7)+'\n')
    f.write('T02C'+('%3.3f' % (sh/1e6)).zfill(7)+'\n')
    f.write('%\n') #start pattern

    #main body: vias
    f.write('T01\n')
    #shift via positions by board size
    viaLocations = (np.array(viaLocations) + np.array(PCBSize)/2)/1e3
    viaLocations = viaLocations.tolist()
    for v in viaLocations:
        x, y = v
        xs = 'X0%i' % np.round(x)
        ys = 'Y0%i' % np.round(y)
        f.write(xs+ys+'\n')
        
    #main body: Screw holes
    f.write('T02\n')
    screwLocations = (np.array(screwLocations) + np.array(PCBSize)/2)/1e3
    screwLocations = screwLocations.tolist()
    for s in screwLocations:
        x, y = s
        xs = 'X0%i' % np.round(x)
        ys = 'Y0%i' % np.round(y)
        f.write(xs+ys+'\n')

    #end 
    f.write('T00\n')  #is this necessary?
    f.write('M30\n')  #Ending statement'
    f.close()
