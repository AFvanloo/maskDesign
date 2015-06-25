import maskDesign as md
import gdsCAD as cad
import numpy as np
import defaultParms as dpars
import pickle
import time
import os

um = 1e3
mm = 1e6
inch = 25.4*mm
defaults = dpars.dPars()

print 'loading wafer class'

class Mask:
    '''
    wafer class

    InPuts:
        size: Wafer size in nm
        sampleList: List object containing gdsCAD objects to go on the mask
        dphi: determines the size of the patch at the bottom of the wafer that is colored
        toNeg: If set to true, this draws an extra circle around the wafer-part of the mask, which can be used to invert the mask using boolean layer operations in KLayout. Default = False
        label: A label that appears at the top of the mask. Default = 'AwesomeMask'
        fileName: the path to save the gds file to. Also determines the pickle path. 

    '''




    def __init__(self, size, sampleList, dphi=10, toNeg=False, label='AwesomeMask', fileName ='./wafer2/wafer2.gds'):


        #init properties
        self.size = size
        self.dphi = dphi  # determines the size of the black edge at the bottom
        self.label = label
        self.sampleList = sampleList
        self.sizeList = []
        self.unitCell = []
        self.gap = 0

        self.labelPos = [-4.5*mm, 2*mm] 
        self.labelSize = fSize = defaults['labelFontSize']
        white = defaults['labelSpace']
        self.sampleLabels = [fSize/40, white-fSize/40]
        self.maskLabels = [white-fSize/40, fSize/70]
        self.maskLabel = ''
        self.labelList = []
        self.usedGrid = []
        self.boundaryPoints = []

        #make wafer
        self.initWafer()
        self.gdsFileName = fileName
        self.pickleName = fileName[:-4]+'_pickled'


    def initWafer(self):
        '''
        Construct a wafer
        '''
        #Topcell and Layout:
        self.topCell = cad.core.Cell('TOP')
        self.layout = cad.core.Layout('WAFER')
        #Put units to nm to allow fine spacing of object origins
        self.layout.unit = 1e-9

        self.borderCell = md.wafer(self.size, extraLayer=True)
        self.topCell.add(self.borderCell)

        #add label
        tinfo = time.gmtime()
        dateString = str(tinfo[0])+str(tinfo[1])+str(tinfo[2])
        fSize = 10*mm
        y = 2.5*inch - 1.2*fSize
        self.addText((-fSize,y), self.label, fontSize = fSize)
        self.addText((1.4*inch, -2.5*inch), dateString + ' AF', fontSize = fSize/2)

        #Generate Labels, Generate chip locations, and distribute the samples
        self.generateLabels()
        self.generateLocations()
        self.distributeSamples()
        #if len(self.usedGrid) > 4:
        #self.addEdge()

    
    def distributeSamples(self):

        #make a cell to hold the samples
        self.samplesCell = cad.core.Cell('SAMPLES')
        sampleLabelList = []

        for sample in self.sampleList:
            #Put sample at location, add label
            self.placeChip(sample)

        #add the samples
        self.topCell.add(self.samplesCell)

    
    def generateLocations(self):
        
        #get sizes
        diffsizes = []
        for sample in self.sampleList:
            self.sizeList.append(sample.borders)
            if sample.borders not in diffsizes:
                diffsizes.append(sample.borders)

        #find unit cell
        self.getUnitCell(diffsizes)

        #assign grid
        self.makeGrid()


    def generateLabels(self):

        #mask number
        self.maskLabel = self.label[0].upper()+self.label[-1].upper()

        # Generate labels
        for i in range(len(self.sampleList)):
            self.labelList.append(chr(65+i/16)+str(hex(i)).upper()[-1])
        print 'self labelList is ', self.labelList


    def placeChip(self, sample):

        #self.addLabel(sample) #add a label to the sample
        cellref = cad.core.CellReference(sample.topCell)

        #decide the number of unit cells needed
        ux, uy = self.unitCell
        nx, ny = (sample.borders[0]+self.gap)/ux, (sample.borders[1]+self.gap)/uy

        #offset of center of mass compared to center of unitCell 1
        offsets = [(nx-1)*ux/2, (ny-1)*uy/2]

        #pick location
        locnum = 0 
        foundLoc = False
        while foundLoc == False:
        #are adjacent unitcells still free?
            loc = self.grid[locnum]
            tempgrid = 1*self.grid
            tempUsedGrid = []
            foundLoc=True
            for i in range(int(nx)):
                for j in range(int(ny)):
                    if [loc[0]+i*ux, loc[1]+j*uy] not in self.grid:
                        foundLoc = False
                    else :
                        #add location to used list the cell from the temporary location list
                        tempgrid.remove([loc[0]+i*ux, loc[1]+j*uy])
                        tempUsedGrid.append([loc[0]+i*ux, loc[1]+j*uy])
                        print 'used a location! ', tempUsedGrid
            
            #place the chip at location
            if foundLoc == True:
                coords = [loc[0]+offsets[0], loc[1]+offsets[1]]  #location of chip center
                print 'creating cell ', sample.label, ' at ', coords[0]/1e6, coords[1]/1e6
                cellref.translate([loc[0]+offsets[0], loc[1]+offsets[1]])
                self.samplesCell.add(cellref)
                self.addLabel(sample, coords)
                #remove the used locations and from the list
                self.grid = tempgrid
                print 'tempUsedGrid looks like ', tempUsedGrid[0]
                self.usedGrid.append(tempUsedGrid[0])
            #else, go to next location    
            else:
                locnum += 1


    def getUnitCell(self, diffsizes):
        #Get the unit cell size
        xes = [diffsizes[i][0] for i in range(len(diffsizes))]
        ys = [diffsizes[i][1] for i in range(len(diffsizes))]
        minx, miny = min(xes), min(ys)

        for i in range(len(diffsizes)):
            if (xes[i]%minx != 0) or (ys[i]%miny != 0):
                Exception, 'Cannot assign a unit cell: some samples have sizes that are not integer multiples of the smallest sample sizes found'

        self.gap = self.sampleList[0].borderGap
        self.unitCell = [minx+self.gap, miny+self.gap]
        print 'unit-cell sizes are ', self.unitCell[0]/1e6, ' mm in x and ', self.unitCell[1]/1e6, ' mm in the y direction'


    def makeGrid(self):

        gridPositions = []
        #This gap is the amount of space at the top and bottom that cannot be allocated
        borderGapx = 1*mm
        borderGapy = 2*mm

        #self.size is a radius
        ux, uy = self.unitCell
        nx = (self.size-borderGapx)/ux
        ny = (self.size-borderGapy)/uy

        #all grid locations
        for i in range(int(-nx), int(nx+1)):
            for j in range(int(-ny), int(ny+1)):#
                dis = np.sqrt((i*ux)**2 + (j*uy)**2)
                if dis < self.size - min(borderGapx, borderGapy):
                    gridPositions.append([i*ux, j*uy, dis])

        #sort according to distance to center
        gridSorted = sorted(gridPositions, key= lambda gridPositions: gridPositions[2])
        partGrid = [[gridSorted[i][0],gridSorted[i][1]] for i in range(len(gridSorted))]
        self.grid = partGrid

    def addLabel(self, sample, coords):

        #get coordinates to be used
        x, y = sample.borders
        dx, dy = coords
        dxS, dyS = self.sampleLabels
        dxM, dyM = self.maskLabels

        #label spots
        coordsS = [-x/2+dx+dxS, y/2+dy-dyS]
        coordsM = [x/2+dx-dxM, -y/2+dy+dyM]

        #add labels to chips
        self.addText(coordsS, self.labelList[0], fontSize=self.labelSize)
        self.addText(coordsM, self.maskLabel, fontSize=self.labelSize)
        
        #remove used label from list
        self.labelList = self.labelList[1:]
        print 'labelList len is now ', len(self.labelList)


    def addEdge(self):

        edgeCell = cad.core.Cell('EDGE')
        bound = []
        
        for i in range(len(self.usedGrid)):
            print 'usedGrid currently is ', self.usedGrid[i]
            bound.extend(self.getBoundaryPoints(self.usedGrid[i]))

        #sort using phi in a lambda function
        bound = self.sortAngle(bound)
        self.boundaryPoints = bound

        #make a circle
        circ = md.flatCircle((0,0), self.size-1*mm, dphi=32)

        #combine all
        totbound = circ[::-1] + bound + [bound[0]] + [circ[-1]]
        boundr = cad.core.Boundary(totbound)

        #add and show
        edgeCell.add(boundr)
        self.topCell.add(edgeCell)

        
    def getBoundaryPoints(self, loc):
        #returns the boundary points if the cell is on the edge, and 0 otherwise
        #how many neighbouring cells:

        ux, uy = self.unitCell
        used = self.usedGrid
        bPoints = []
        left =  [loc[0] - ux, loc[1]] in used
        right =  [loc[0] + ux, loc[1]] in used
        above =  [loc[0], loc[1]+uy] in used
        below =  [loc[0], loc[1]-uy] in used
        dirs = [left, right, above, below]

        if sum(dirs)==4:
            return []
        if sum(dirs)==3:
            return []
        if sum(dirs)==2:
            print 'in boundary with two neigbours'
            if (left and right) or (above and below): return []
            else : 
                allcor =  [[loc[0]-ux/2,loc[1]+uy/2],[loc[0]+ux/2, loc[1]+uy/2],
                    [loc[0]+ux/2,loc[1]-uy/2],[loc[0]-ux/2, loc[1]-uy/2]]
                noncor =  [loc[0] - left*ux/2 + right*ux/2, loc[1] + above*uy/2 - below*uy/2]
                print 'allcor is ', allcor
                print 'noncor is ', noncor
                allcor.remove(noncor)
                print 'allcor removed is ', allcor
                return allcor
        if sum(dirs)<=1:
            print 'In boundary with 1 neighbour'
            #add all boundary points
            return [[loc[0]-ux/2,loc[1]+uy/2],[loc[0]+ux/2, loc[1]+uy/2],
                    [loc[0]+ux/2,loc[1]-uy/2],[loc[0]-ux/2, loc[1]-uy/2]]

    def sortAngle(self, pointList):
        sortList = self.sortAlgo(pointList)
        sortedPoints = [x for (x,y) in sorted(zip(pointList,sortList), key=lambda pair:pair[1])]
        return sortedPoints

    def sortAlgo(self, pointList):
        #sort according to angle. This can be done more cleverly using determinants
        sortList = []
        for i in range(len(pointList)):
            x,y = pointList[i]
            if x == 0:
                if y > 0: sortList.append(np.pi/2)
                else: sortList.append(3*np.pi/2)
            if x>0 and y>=0: sortList.append(np.arctan(y/x))
            if x>0 and y<0 : sortList.append(2*np.pi+np.arctan(y/x))
            if x<0:          sortList.append(np.pi + np.arctan(y/x))
        print 'sortList is ', sortList
        return sortList

    def addText(self, coords, text, font='romand', fontSize=.45*mm, rot=0):
        textCell = md.chipText(coords, text, fontSize, font, rot)
        self.topCell.add(textCell)

    def addChipText(self, sample, text, coords):
        textCell = md.chipText(coords, text, self.labelSize)
        sample.topCell.add(textCell)

    def show(self):
        self.layout.add(self.topCell)
        print 'calling matplotlib to show the wafer'
        self.layout.show()

    def save(self):
        print 'saving, fileName is ', self.gdsFileName
        self.layout.add(self.topCell)
        self.layout.save(self.gdsFileName)
    
    def storeAll(self, fileName = ''):

        if fileName == '':
            fileName = self.pickleName

        #first test if file exists
        if os.path.isfile(fileName):
            x = raw_input('file exists, overwrite? (Yy/*) ')
            if x.upper() == 'Y':
                newOpenFile = open(fileName, 'w')
            else: #
                ValueError, 'Please enter another fileName next time'
        else:
            newOpenFile = open(fileName,'w')

        #use pickle to store the objects with their labels
        self.generateLabels()
        labels = self.labelList
        everythingList = []

        for i in range(len(labels)):
            everythingList.append([labels[i], self.sampleList[i]])
        everythingList.append(['Wafer', self])

        pickle.dump(everythingList, newOpenFile)

    def retrieve(fileName):
        
        f = open(fileName, 'r')
        res = pickle.load(f)
        return res

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

