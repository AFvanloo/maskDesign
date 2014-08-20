#
import maskDesign as md
import gdsCAD as cad
import numpy as np
import defaultParms as dpars


#Units are nm, so to use um, multiply by 1000
um = 1e3
mm = 1e6

#default border and launcher configuration options:
borderTagList, offCenters = dpars.dLists()

#Default component design values
defaults = dpars.dPars()

class Sample:

    def __init__(self, border, launcherConfig='A', launcherPositions=[],
            alignPos=range(4), label = '', labelPos = None):
        '''
        Calling constructor

        The border (default set to 2) refers to the default border sizes and
        launcher configurations:

            1: 7*2mm
            2: 7*4.3mm
            3: 7*6.6mm

        The LauncherConfig determines the locations of the launchers

            'A'  1 launchers left/right, and 3 on top and bottom
            'B'  2 launchers left/right, and 2 on top and bottom
            'C'  16 port design: 4 launchers on each side. Only for chipsize 3
            
        The launcherlist refers to which launchers to put, clockwise from the
        left center

        alignPositions refers to which alignment marks to draw, clockwise from
        the left upper corner

        '''
        #TODO Default Values: hardcode or config file?
        self.fileName = 'test0123.gds'
        self.label = label
        self.labelPos = labelPos

        self.lambdahalf65 = defaults['lambdahalf65']

        #Sample border Options
        self.borders = borderTagList[border]
        self.borderTag = border
        self.borderGap = defaults['borderGap']

        #launcher options
        self.launcherPositions = launcherPositions
        self.launcherConfig = launcherConfig
        self.launchwidth = defaults['launcherWidth'] 
        self.launcherWlen = defaults['launcherWideLen']
        self.launcherTlen = defaults['launcherTaperLen']

        #Alignment mark options
        self.alignPos = alignPos

        #line options
        self.a1 = defaults['centerConductor']
        self.b1 = defaults['CPWGap']
        self.abr = self.b1/self.a1
        self.rbend = defaults['minimumRadius']

        #Transmon options
        self.transmonShape = (300*um, 150*um)

        #gapCoupler Options
        self.gapSize = defaults['gapCouplerSize']

        #fingerCoupler options
        self.fingerTaperLen = defaults['fingerTaperLen']
        self.fingerCenterLen = defaults['fingerCenterLen'] #Length of center part
        self.fingerLen = defaults['fingerLen']
        self.fingerThick = defaults['fingerThick']
        self.fingerGapWidth = defaults['fingerGapWidth']
        self.fingerGapHeight = defaults['fingerGapHeight']

        #Airbridge Options
        self.bridgeLenX = defaults['ABbridgeLenX']
        self.bridgeLenY = defaults['ABbridgeLenY']
        self.footerLen = defaults['ABfooterLen']
        self.reflowGap = defaults['ABreflowGap']
        self.irGap = defaults['ABirGap']
        self.ABlayers = defaults['ABlayers']

        self.bridgeDistance = defaults['ABdistance']

        #label Font
        self.labelFont = defaults['labelFont']

        # Bounding boxes for avoiding overlaps are kept in a np.array
        self.bbox = np.array([]) #TODO Not yet implemented

        #List of possible components
        self.complist = ['CPW','Resonator', 'GateLine', 'TransmonBox']
        self.compamounts = [0,0,0,0]

        #A 6.5 Lambda/2 resonator is 2*4670um long
        lambhalf65 = 2*4670*um

        #keeping track of present components:
        self.resonators = 0
        self.wiggles = 0
        self.transmonBoxes = 0
        self.fingerCouplers = 0
        self.gapCouplers = 0
        self.airbridges = 0
        self.CPWs = 0
        self.arcs = 0
        self.doubleArcs = 0
        self.slines = 0
        self.jlines = 0
        self.texts = 0
        self.tapers = 0
        self.crossArrays = 0
        self.fingerCaps = 0
        self.gateLines = 0
        self.gateEnds = 0
        self.fluxLines = 0
        self.newname = ''
        

        #Start Constructing the Sample
        print 'border type is ', border 
        if (border < 1) or (border > 4):
            raise Exception, 'Choose border between 1 and 4'
            #If using python 3, replace with following line
            #raise Exception('Choose border between 1 and 4')
        #Initialize actual Sample
        self.initSample()

    def initSample(self):
        '''
        Construct a sample layout with borders
        '''
        #Topcell and Layout:
        self.topCell = cad.core.Cell('TOP')
        self.layout = cad.core.Layout('SAMPLE')
        #Put units to nm to allow fine spacing of object origins
        self.layout.unit = 1e-9

        #borders and alignment markers
        self.border1 = Border(self)

        #add label
        self.addText(self.label, fontSize = 500*um, placeInfo = self.labelPos)

        #add Launchers
        self.addLaunchers()

#========================sampleX wrappers for objects===========================

    def addCPW(self, leng, placeInfo, bridges=False, bridgeDistance= None,
            bridgeStart=None, bridgeEnd=None, closeA=False, closeB=False, flip=False, rot=0):
        '''
        add a CPW line

        Input the length in nm

        PlaceInfo can be either a location or the connector of an object.
        Examples:
            (x, y)
            'launcher1.connect'

        if Bridges is set to true, airbridges are created as well, with optional 
        entries for an initial and final span without airbriges.

        If you need more control, keep bridges set to off and add them
        separately

        If closeA or closeB is set to true, a rectangle is drawn at that end of
        the CPW to close it.

        Flip is used when connecting to a component situated to the right of the
        CPW. By default flip is off, meaning a CPW is added to a component on
        its left
        '''

        #Keep track of the number of lines
        self.CPWs +=1
        setattr(self, 'CPW'+str(self.CPWs), CPW(self,leng, placeInfo, bridges,
            bridgeDistance, bridgeStart, bridgeEnd, closeA, closeB, flip, rot))


    def addArc(self, initAngle, degrees, placeInfo, flip=False, rbend=None,
            rot=0):
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
        
        print 'bla'
        self.arcs += 1
        #create launchers according to the list 'launcherpositions'
        setattr(self, 'arc'+str(self.arcs), Arc(self, initAngle, degrees,
            placeInfo, flip, rbend, rot))

#    def addResonator(self, freq, xspan, nwiggle, transmons = ['luru'], caps =
#    ['f3f3'], xOffset=0,
#            yOffset=0, skew=0, rot=0):
#        '''
#        Add a resonator, including transmons and capacitors
#
#        Not all options can be entered via this function. They are however all
#        available as attributes to the resonator class. 
#
#        Change the attributes you want to change, 
#
#        leng denotes the total length you want
#        xspan is the horizontal (or vertical if rotated) distance between start
#        and end point
#
#        xOffset and its Y variant displace the wiggles compared to the
#        start coordinates of the structure
#        '''
#        
#        self.resonators += 1
#        setattr(self, 'wiggle'+str(self.wiggles), Wiggle(self,nWiggle, leng,
#            xspan, placeInfo, xOffset, yOffset, skew, rot))



    def addDoubleArc(self, dx, placeInfo, rbend=None, flip=False, rot=0):
        '''
        Wrapper for Arc:

        rbend is set to 100um by default. initAngle is the initial angle at
        which the bend starts, similar to in the unit circle. 
        
        degrees is the amount angle between start and end

        The flip option is used to toggle if the component should be added from
        the top or from below

        addArc has no rotation variable, since the same functionality is reached
        by changing initAngle
        '''

        #Default values
        if rbend == None: rbend = self.rbend
        

        self.doubleArcs += 1
        #create launchers according to the list 'launcherpositions'
        setattr(self, 'doubleArc'+str(self.doubleArcs), DoubleArc(self, dx,
            placeInfo, rbend, flip, rot))



    def addWiggle(self, nWiggle, leng, xspan, placeInfo, xOffset=0,
            yOffset=0, rbend = None, bridges=True, skew=0, rot=0):
        '''
        Add a wiggly CPW

        leng denotes the total length you want
        xspan is the horizontal (or vertical if rotated) distance between start
        and end point

        xOffset and its Y variant displace the wiggles compared to the
        start coordinates of the structure
        '''

        if rbend == None: rbend = self.rbend
        
        self.wiggles += 1
        setattr(self, 'wiggle'+str(self.wiggles), Wiggle(self,nWiggle, leng,
            xspan, placeInfo, xOffset, yOffset, rbend, bridges, skew, rot))

        
    def addSLine(self, yspan, placeInfo, rbend = None, reflect=False, flip=False, enter=True,
            exit = True, bridges = False,  rot=0):
        '''
        Add an Sline (90 degree arc + CPW + 90 arc
        '''
        
        #default value
        if rbend == None: rbend = self.rbend

        self.slines += 1
        setattr(self, 'sLine'+str(self.slines), SLine(self, yspan, placeInfo,
            rbend, reflect, flip, enter, exit, rot))


    def addJLine(self, totLen, xspan, yspan, nWiggles, placeInfo, offsets,
            rbend=None, bridges=True, rot=0):
        '''
        Add a JLine to the sample, primarily as testresonators coupled to a
        feedLine

        Inputs: 
        totLen = total length of the resonator, determining its frequency
        xspan = length of horizontal line at the top
        yspan = vertical length of the resonator
        nWiggles = number of wiggles in the line
        placeInfo = location information, either a tuple of coordinates, or an
        object connector (as a string)
        offsets = offsets compared to the placeInfo connector
        '''

        #default value
        if rbend == None: rbend = self.rbend

        self.jlines += 1

        setattr(self, 'JLine'+str(self.jlines), JLine(self, totLen, xspan,
            yspan, nWiggles, placeInfo, offsets, rbend, bridges, rot))


    def addGapCoupler(self, gapSize, placeInfo, extralen=0,flip=False, rot=0):
        '''
        Add a gap Coupler. 

        By default, the gap coupler is only as long as the gap. If you would
        like it longer, just add a nonzero extralen.

        For placeInfo, input either a tuple of coordinates:
            (x, y)
        or a string containing what you want to connect it to, for example:
            CPW1.connectB
        '''

        self.gapCouplers += 1
        setattr(self, 'gapCoupler'+str(self.gapCouplers),
                GapCoupler(self,gapSize, placeInfo, extralen, flip, rot))


    def addTransmonBox(self, placeInfo, shape=(300*um, 150*um), offset=(300*um,0), almarks = [2,2],
            flip=False, corner=False,  rot=0):
        '''
        Add a TransmonBox. 

        The offset is an offset compared to placeInfo, such that the transmonbox
        can be connected directly to the connector of a CPW or Wiggle

        The offset is ignored when the placeInfo provided is a tuple with
        coordinates rather than a string to a connector

        if flip is set to true, the transmonbox is placed on the opposite side
        of the CPW

        if corner is set to True, you get a cornerTransmonBox instead. In that
        case, options almarks and flip are ignored
        '''

        #If gateLine is set to true, a gateLineEnd is created at the transmonBox.
        #Its options can be set in a list via gateOptions, in the order
        #[gapLen, xOffset]

        #If fluxLine is set to true, a fluxLineEnd is created at the transmonbox

        self.transmonBoxes += 1
        setattr(self, 'transmonBox'+str(self.transmonBoxes),
                TransmonBox(self, shape, placeInfo, offset, almarks, flip,
                    corner, rot))

    def addFingerCap(self, nFingers, placeInfo, fingerLen = None, 
            fingerThick=None, gapHeight = None, gapWidth = None, flip=False, rot=0):
        '''
        Add a finger Capacitor. 

        The finger Capacitor has loads of options, but there are default values
        for almost all of them. Change any of them as you like, according to:
            addFingerCap(3, <placeInfo>, gapWidth = 1*um, taperLen = 75*um)
        for example

        For placeInfo, input either a tuple of coordinates:
            (x, y)
        or a string containing what you want to connect it to, for example:
            'CPW1.connectB'
        '''

        #Set the default Values
        if fingerLen == None: fingerLen = self.fingerLen
        if fingerThick == None: fingerThick = self.fingerThick
        if gapHeight == None: gapHeight = self.fingerGapHeight
        if gapWidth == None: gapWidth = self.fingerGapWidth

        #Build the finger coupler
        self.fingerCaps += 1
        setattr(self, 'fingerCap'+str(self.fingerCaps),
                FingerCap(self,nFingers, placeInfo, fingerLen,
                fingerThick, gapHeight, gapWidth, flip=flip, rot=rot))



    def addFingerCoupler(self, nFingers, placeInfo, fingerLen = None, 
            fingerThick=None, gapHeight = None, gapWidth = None,
            taperLen = None, centerLen = None, flip=False, rot=0):
        '''
        Add a finger Coupler. 

        The finger Coupler has loads of options, but there are default values
        for almost all of them. Change any of them as you like, according to:
            addFingerCoupler(3, <placeInfo>, gapWidth = 1*um, taperLen = 75*um)
        for example

        For placeInfo, input either a tuple of coordinates:
            (x, y)
        or a string containing what you want to connect it to, for example:
            'CPW1.connectB'
        '''

        #Set the default Values
        if fingerLen == None: fingerLen = self.fingerLen
        if fingerThick == None: fingerThick = self.fingerThick
        if gapHeight == None: gapHeight = self.fingerGapHeight
        if gapWidth == None: gapWidth = self.fingerGapWidth
        if taperLen == None: taperLen = self.fingerTaperLen
        if centerLen == None: centerLen = self.fingerCenterLen

        #Build the finger coupler
        self.fingerCouplers += 1
        setattr(self, 'fingerCoupler'+str(self.fingerCouplers),
                FingerCoupler(self,nFingers, placeInfo, fingerLen,
                fingerThick, gapHeight, gapWidth, taperLen, centerLen, flip, rot=rot))

    def addAirbridge(self, placeInfo, bridgeLenX=None, bridgeLenY=None,
            footerLen = None, irGap=None, reflowGap = None, layers=None,rot=0):
        '''
        Add a single or multiple airbridges. 

        All options (except placeInfo and rot) are taken from the config dict,
        Unless if specified otherwise by YOU!

        For the placing, there are quite a few options for 
        '''

        #Set the default Values
        if bridgeLenX == None:  bridgeLenX =  self.bridgeLenX
        if bridgeLenY == None:  bridgeLenY =  self.bridgeLenY
        if footerLen == None:   footerLen =  self.footerLen
        if irGap == None:       irGap =  self.irGap
        if reflowGap == None:   reflowGap =  self.reflowGap
        if layers == None:      layers =  self.ABlayers

        #Build the finger coupler
        self.fingerCouplers += 1
        setattr(self, 'airBridge'+str(self.airbridges),
                AirBridge(self, placeInfo, bridgeLenX, bridgeLenY, footerLen, 
                    irGap, reflowGap, layers, rot=rot))
    
    def addTaper(self, taperLen, placeInfo, startCenter, endCenter=None, abr = None, rot=0):
        '''
        Add a Taper

        define the total width of the center conductor at start (startCenter)
        and end (endCenter)

        placeInfo can be either a string for a connector, or a tuple or list of
        coordinates
        '''

        #default variables
        if abr == None: abr = self.abr
        if endCenter == None: endCenter = self.a1

        self.tapers += 1
        setattr(self, 'taper'+str(self.tapers),
                Taper(self, taperLen, startCenter, endCenter, placeInfo,
                    abr=self.abr, rot=rot))


    def addLauncher(self, placeInfo, center=None, gap=None):
        '''
        add a single launcher

        For Launchers at standard positions at the borders, please use
        'addLaunchers' instead
        '''
        print 'constructing Launchers' 

        #default options
        if center == None: center = self.a1
        if gap == None: gap = self.b1

        #create launchers according to the list 'launcherpositions'
        setattr(self, 'launcher'+str(pos), Launcher(self, placeInfo, center, gap,
            rot=self.rot))


    def addLaunchers(self, center=None, gap=None):
        '''
        Wrapper for Launcher:
        Create Launcher objects with names according to their position
        '''
        print 'constructing Launchers' 

        #default options
        if center == None: center = self.a1
        if gap == None: gap = self.b1

        
        #get the position list associated with the chosen configuration 
        self.launcherLocations = self.launchPosList()


        #create launchers according to the list 'launcherpositions'
        [setattr(self, 'launcher'+str(pos), Launcher(self,pos, center, gap,
            rot=0)) for pos in self.launcherPositions]
        

   
    def launchPosList(self):
        '''
        make a list of launcher positions and locations depending on the
        launcherConfig and border

        Ugly implementation, feel free to efficify
        '''

        #force to string
        self.launcherConfig  = str(self.launcherConfig)

        #Check for valid input
        if self.launcherConfig not in ['A', 'B', 'C']:
            raise Exception, 'Launcherconfig must be either A, B or C (case sensitive)'
            #python 3 variant below
            #raise Exception('Launcherconfig must be either A, B or C (case sensitive)')

        #Decide on launcher locations
        borX, borY = self.borders[0]/2.,self.borders[1]/2.
        positions = []
        #Get the offcenter locations depending on launcherconfig
        offs = offCenters[self.launcherConfig]

        if self.launcherConfig == 'A':
            # 8 launchers max, 1 left/right, 3 top/bottom
            positions.append([-borX,0,0])
            positions.extend([[-offs,borY,-90],[0,borY,-90],[offs,borY,-90]])
            positions.append([borX,0,180])
            positions.extend([[offs,-borY,90],[0,-borY,90],[-offs,-borY,90]])

        if self.launcherConfig == 'B':
            #check if its the right chipsize
            if self.borderTag < 2 or self.borderTag > 4:
                raise Exception, 'Configuration B should be used with chipsize 2 or 3'
            #determine offCenterY
            offX, offY = offs[0], offs[self.borderTag-1]
            #populate position list
            positions.append([-borX, offY, 0])
            positions.extend([[-offX, borY, -90],[offX, borY, -90]])
            positions.extend([[borX, offY, 180],[borX, -offY, 180]])
            positions.extend([[offX, -borY, 90],[-offX, -borY, 90]])
            positions.append([-borX, -offY, 0])

        if self.launcherConfig == 'C':
            #first check if the border is 3:
            if self.borderTag != 3:
                raise Exception, 'Configuration C only works with bordersize 3'
                #Python 3 variant: raise Exception('Configuration 3 only works with bordersize 3')
            offX1, offX2, offY1, offY2 = offs
            positions.extend([[-borX, offY1, 0],[-borX, offY2, 0]])
            positions.extend([[-offX2, borY,-90],[-offX1, borY,-90], 
                [offX1, borY,-90], [offX2, borY,-90]])
            positions.extend([[borX, offY2, 180],[borX, offY1, 180], 
                [borX, -offY1, 180], [borX, -offY2, 180]])
            positions.extend([[offX2, -borY, 90],[offX1, -borY, 90], 
                [-offX1, -borY, 90], [-offX2, -borY, 90]])
            positions.extend([[-borX, -offY2, 0],[-borX, -offY1, 0]])

        return positions    
    
    def addCrossArray(self, placeInfo):
        '''
        Add alignment markers for e-beam at placeInfo

        At this moment, no options are given in the class (as I do not think
        they will be used), but they are available in the underlying function 
        in maskDesign, feel free to add the options here too
        '''

        self.crossArrays += 1
        setattr(self, 'crossArray'+str(self.crossArrays),
                CrossArray(self, placeInfo))




    def addText(self, text, fontSize=200*um, placeInfo=None, font = None, rot=0, layer=0):
        '''
        Add labels to the chip

        If the coords are left to default, the text will be placed in the upper
        center of the chip

        Chip labels go in layer 0, wafer Labels in layer 2

        Different fonts are available (all Hershey fonts are available, as is a
        blockfont). Look at the gdsCAD documentation for details.
        '''

        if font == None: font = self.labelFont
        #Determine some coordinates for the text
        if placeInfo == None: 
            mtext = max(text.split('\n'))
            x = -len(mtext)*fontSize/4
            y = self.borders[1]/2 - fontSize
            placeInfo = (x,y)

        self.texts += 1
        setattr(self, 'text'+str(self.texts), CText(self, text, fontSize,
            placeInfo, font, rot, layer))




    def addGateLine(self, placeInfoLaunch, placeInfoTransmon, gapLen=25*um,
            extraline=0, gapOffset = (0,0), endrot=0, startrot=0):
        '''
        Add a gateLine from the Launcher connector to a transmon box
u
        Options:
        gapLen: length of the gap
        extraLine: CPW connected to the gap

        gapXoffset: shift the connection relative to the connection point

        endrot: rotation of the endpoint, including an arc: Specify if the last
        turn is either left or right
            so endrot = 'l' or 'r' or 0

        When connecting to coordinates rather than a Launcher, use startRot to get
        the correct initial rotation (its automatic from Objects)

        '''

        self.gateLines += 1

        setattr(self, 'gateLine'+str(self.gateLines),
                GateLine(self, placeInfoLaunch, placeInfoTransmon, gapLen,
                    extraline, gapOffset, endrot, startrot))



    def addFluxLine(self, placeInfoLaunch, placeInfoTransmon, extraLine=0,
         fluxGap=None, fluxLen=None, fluxOffset = (0,0), endrot=0, startrot=0):
        '''
        Add a flux Line from the Launcher connector to a transmon box

        options:
        fluxGap = gap for current to flow between fluxLine and transmonbox
        fluxLen = Length of the structure
        fluxOffset = offsets in the x and y direction compared to the transmon
        box

        endrot: rotation of the endpoint, including an arc: Specify if the last
        turn is either left or right
            so endrot = 'l' or 'r' or 0


        When connecting to coordinates rather than a Launcher, use startRot to get
        the correct initial rotation (its automatic from Objects)

        '''

        if fluxGap == None: fluxGap = defaults['fluxGap']
        if fluxLen == None: fluxLen = defaults['fluxLen']

        self.fluxLines += 1

        setattr(self, 'fluxLine'+str(self.fluxLines),
                FluxLine(self, placeInfoLaunch, placeInfoTransmon, fluxGap,
                    extraLine, fluxLen, fluxOffset, endrot, startrot))



    def route(self, placeInfo1, placeInfo2, rot1=0, endrot=0):
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
            self.startrot = getattr(comp, 'rot')
        else:
            self.startcoords = placeInfo1
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

        #Re-express as an upgoing problem
        if self.startrot%90 != 0:
            raise ValueError, 'Use only multiples of 90 degrees when connecting a flux or gateline'

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
            rotBack = -90
        elif self.startrot == 270 or -90:
            tdx = -dy
            tdy = -dx
            rotBack = 180

        print 'tdy, tdx are', tdx, tdy

        if endrot == 'l': 
            tdx += self.rbend
            tdy -= self.rbend
        if endrot == 'r': 
            tdx -= self.rbend
            tdy -= self.rbend

        routeCell = md.CPWroute(self.startcoords, tdx, tdy, rot = rotBack,
                endrot=endrot) 
        return routeCell


    def save(self):
        self.layout.add(self.topCell)
        self.layout.save(self.fileName)
    

    def show(self):
        self.layout.add(self.topCell)
        self.layout.show()

#=============================================================================
#------------------------------COMPONENT OBJECTS-------------------------------
#=============================================================================


class Border:
    '''
    sample borders
    '''

    def __init__(self,sampleX):

        #make the cell
        self.Cell = md.borderA(sampleX.borders[0],sampleX.borders[1],
                sampleX.borderGap, sampleX.alignPos)
        sampleX.topCell.add(self.Cell)
        

class Launcher:
    '''
    Add the launchers to the chip
    '''

    def __init__(self, sampleX, placeInfo, center, gap, rot):
        '''
        make the launchers

        pos is the position of this specific launcher, counting from the center
        left
        '''
        
        #initialize variables
        self.rot = rot
        
        #Decide if we have coordinates or connection
        if type(placeInfo) == int:
            x, y, rot = sampleX.launcherLocations[placeInfo]


            self.coords = (x, y)
            self.rot = rot
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for size of device
            self.coords = (self.cp[0] + self.taperLen/2.*np.cos(rad(self.rot)),
                    self.cp[1] + self.taperLen/2.*np.sin(rad(self.rot)))
        if type(placeInfo) == tuple or type(placeInfo) == list:
            #its coordinates
            self.coords = placeInfo

        #make the cell, using default variables
        self.Cell = md.launcher(self.coords, center=center, gap=gap, rot=rot)

        #easier typing
        x, y  = self.coords

        #Define connection points
        totlen = sampleX.launcherTlen+sampleX.launcherWlen
        self.connectDistance = (totlen*np.cos(rad(rot)), totlen*np.sin(rad(rot)))
        self.connect = (x + self.connectDistance[0], y + self.connectDistance[1])

        #add cell to sample topcell
        sampleX.topCell.add(self.Cell)


class Taper:

    def __init__(self, sampleX, taperLen, startCenter, endCenter, placeInfo,
            abr, rot):

        #Initialize attributes
        self.startCenter = startCenter
        self.endCenter = endCenter
        self.taperLen = taperLen
        self.abr = abr
        self.rot = rot

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for size of device
            self.coords = (self.cp[0] + self.taperLen/2.*np.cos(rad(self.rot)),
                    self.cp[1] + self.taperLen/2.*np.sin(rad(self.rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #Taper is centered around the origin
        self.connectA = (self.coords[0] - self.taperLen/2.*np.cos(rad(rot)),
                self.coords[1] + self.taperLen/2.*np.sin(rad(rot)))
        self.connectB = (self.coords[0] + self.taperLen/2.*np.cos(rad(rot)), 
                self.coords[1] - self.taperLen/2.*np.sin(rad(rot)))

        #create and add the Cell
        self.makeCell()
        sampleX.topCell.add(self.Cell)

    def makeCell(self):
        '''
        make the cad Cell reference of the Taper
        '''
        print 'drawing a Taper, startCenter  = ', self.startCenter 

        # outer lines
        startOuter = self.abr*self.startCenter
        endOuter = self.abr*self.endCenter

        self.Cell = md.taper(self.coords, self.taperLen, startOuter, endOuter,
                self.startCenter, self.endCenter, self.rot)



class CPW:

    def __init__(self, sampleX, leng, placeInfo, bridges, bridgeDistance, bridgeStart,
            bridgeEnd, closeA, closeB, flip, rot):
        '''
        Initialize the object
        '''

        self.leng = leng
        self.rot = rot
        self.bridges = bridges
        self.bridgeStart= bridgeStart
        self.bridgeEnd= bridgeEnd
        self.bridgeDistance = bridgeDistance
        self.closeA = closeA
        self.closeB = closeB
        self.flip = flip

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
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

        #Make the Cell
        self.makeCell()

  #      if bridges:
  #          self.addBridges()
  #          sampleX.topCell.add(self.ABCellr)

        #Add the CPW cell to the TopCell
        sampleX.topCell.add(self.Cell)
        
    def makeCell(self):
        '''
        make the cad Cell reference of the CPW
        '''
        print 'drawing a CPW of ', self.leng/1e6, ' mm long' 
        self.Cell = md.CPW(self.coords,self.leng, closeA =
                self.closeA, closeB = self.closeB, bridges=self.bridges, rot=self.rot)
#
#    def addBridges(self):
#
#        #Cell for bridges
#        bridgeCell = cad.core.Cell('AB')
#        xloc = self.bridgeDistance/2.
#        
#        #Generate airbridges symmetrically around 0
#        while xloc < self.leng/2:
#            if xloc < self.leng/2. - self.bridgeEnd:
#                ab1 = md.airBridge((xloc,0), rot=90)
#                bridgeCell.add(ab1)
#            if -xloc > -self.leng/2. + self.bridgeStart:
#                ab2 = md.airBridge((-xloc,0), rot=90)
#                bridgeCell.add(ab2)
#            xloc = xloc + self.bridgeDistance
#
#        self.ABCellr = cad.core.CellReference(bridgeCell, rotation=self.rot)
#        self.ABCellr.translate(self.coords)
#
class Arc:

    def __init__(self, sampleX, initAngle, degrees, placeInfo,flip, rbend, rot):
        '''
        Construct an Arc
        '''
        
        #attributes
        self.initAngle = initAngle
        self.degrees = degrees
        self.rbend = rbend
        self.rot = rot

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
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
        self.makeCell(sampleX)


    def makeCell(self,sampleX):
        '''
        make the cad Cell reference of the CPW
        '''
        self.Cell = md.CPWArc(self.coords, self.initAngle, self.degrees,
                radius=self.rbend, rot = self.rot)
        #Add the cell to the TopCell
        sampleX.topCell.add(self.Cell)


class DoubleArc:

    def __init__(self, sampleX, dy, placeInfo, rbend, flip, rot):

        self.dy = dy
        self.rot = rot
        self.rbend = rbend

        #Calculate angle
        phirad = np.arccos(1-abs(dy)/(rbend*2))
        self.xspan = 2*rbend*np.sin(phirad)

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            if flip:
                 self.coords = (self.cp[0] - self.dy/2*np.sin(rad(self.rot)) -
                    self.xspan/2.*np.cos(rad(self.rot)), self.cp[1] +
                    self.xspan/2.*np.sin(rad(self.rot)) - self.dy/2*np.cos(rad(self.rot)))
            else:
                self.coords = (self.cp[0] + self.dy/2*np.sin(rad(self.rot)) +
                    self.xspan/2.*np.cos(rad(rot)), self.cp[1] +
                    self.xspan/2.*np.sin(rad(self.rot)) + self.dy/2*np.cos(rad(self.rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #Define Connectors
        self.connectB = (self.coords[0] - self.dy/2*np.sin(rad(self.rot)) -
                self.xspan/2.*np.cos(rad(self.rot)), self.coords[1] +
                self.xspan/2.*np.sin(rad(self.rot)) - self.dy/2*np.cos(rad(self.rot)))
        self.connectA = (self.coords[0] + self.dy/2*np.sin(rad(self.rot)) +
                self.xspan/2.*np.cos(rad(self.rot)), self.coords[1] +
                self.xspan/2.*np.sin(rad(self.rot)) + self.dy/2*np.cos(rad(self.rot)))

        self.makeCell()
        sampleX.topCell.add(self.Cell)

    def makeCell(self):
        self.Cell, b = md.doubleArc(self.coords, self.dy, rot = self.rot)

        
class SLine:

    def __init__(self, sampleX, yspan, placeInfo, rbend, reflect, flip, enter, exit, rot):
        '''
        Construct an Sline 
        '''
        
        print 'drawing an S-shape Line'

        #attributes
        self.yspan = yspan
        self.rbend = rbend
        self.flip = flip
        self.reflect = reflect
        self.rot = rot
        self.enter = enter
        self.exit = exit

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            if flip:
                if reflect:
                     self.coords = (self.cp[0] - self.rbend*np.cos(rad(self.rot)) +
                        self.yspan/2.*np.sin(rad(self.rot)), self.cp[1] +
                        self.yspan/2.*np.cos(rad(self.rot)) -self.rbend*np.sin(rad(self.rot)))
                else:
                    self.coords = (self.cp[0] - self.rbend*np.cos(rad(self.rot)) -
                        self.yspan/2.*np.sin(rad(rot)), self.cp[1] -
                        self.yspan/2.*np.cos(rad(self.rot)) + self.rbend*np.sin(rad(self.rot)))
            else:
                if reflect:
                     self.coords = (self.cp[0] + self.rbend*np.cos(rad(self.rot)) -
                        self.yspan/2.*np.sin(rad(self.rot)), self.cp[1] +
                        self.yspan/2.*np.cos(rad(self.rot)) +self.rbend*np.sin(rad(self.rot)))
                else:
                    self.coords = (self.cp[0] + self.rbend*np.cos(rad(self.rot)) +
                        self.yspan/2.*np.sin(rad(rot)), self.cp[1] +
                        self.yspan/2.*np.cos(rad(self.rot)) - self.rbend*np.sin(rad(self.rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #Connector locations
        if self.reflect:
            self.connectB = (self.coords[0] - self.rbend*np.cos(rad(self.rot)) +
                    self.yspan/2.*np.sin(rad(self.rot)), self.coords[1] -
                    self.yspan/2.*np.cos(rad(self.rot)) + self.rbend*np.sin(rad(self.rot)))
            self.connectA = (self.coords[0] - self.rbend*np.cos(rad(self.rot)) -
                    self.yspan/2.*np.sin(rad(self.rot)), self.coords[1] +
                    self.yspan/2.*np.cos(rad(self.rot)) - self.rbend*np.sin(rad(self.rot)))
        else:
            self.connectB = (self.coords[0] + self.rbend*np.cos(rad(self.rot)) -
                    self.yspan/2.*np.sin(rad(self.rot)), self.coords[1] +
                    self.yspan/2.*np.cos(rad(self.rot)) + self.rbend*np.sin(rad(self.rot)))
            self.connectA = (self.coords[0] - self.rbend*np.cos(rad(self.rot)) +
                    self.yspan/2.*np.sin(rad(self.rot)), self.coords[1] -
                    self.yspan/2.*np.cos(rad(self.rot)) - self.rbend*np.sin(rad(self.rot)))


        #make the cell
        self.makeCell(sampleX)

    def makeCell(self,sampleX):
        '''
        make the cad Cell reference of the CPW
        '''
        self.Cell = md.sLine(self.coords, self.yspan, rbend=self.rbend,
                reflect=self.reflect, enter=self.enter, exit = self.exit, rot=self.rot)
        #Add the cell to the TopCell
        sampleX.topCell.add(self.Cell)

class JLine:

    def __init__(self, sampleX, totLen, xspan, yspan, nWiggles, placeInfo,
            offsets, rbend, bridges, rot):
        '''
        Construct a Jline 
        '''
    
        print 'drawing a J-shape Line'

        #attributes
        self.totLen = totLen
        self.xspan = xspan
        self.yspan = yspan
        self.rbend = rbend
        self.nWiggles = nWiggles
        self.offsets = offsets
        self.bridges = bridges
        self.rot = rot

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Apply offsets
            self.coords = (self.cp[0]+self.offsets[0],
                    self.cp[1]+self.offsets[1])
        else:
            #its coordinates
            self.coords = placeInfo
        
        #Make the Cell
        self.makeCell()

        #Add airbridges
        if bridges:
            self.addBridges()
            sampleX.topCell.add(self.abCellr)

        #Add cell to total
        sampleX.topCell.add(self.Cell)

    def makeCell(self):

        self.Cell, self.wigyspan = md.jLine(self.coords, self.totLen, self.xspan, self.yspan,
                self.nWiggles, rbend=self.rbend, rot = self.rot)

    def addBridges(self):
        '''
        add airbridges, by default 2 symmetrically around the center
        '''


        wigOffset = self.yspan/2 - (2*self.nWiggles-2)*self.rbend - self.rbend/2
        abYOffset = - self.yspan/2 + wigOffset 
        
        abCell = cad.core.Cell('AB')
        if self.nWiggles%2 == 1:
            ab1 = md.airBridge((self.xspan/2 -2*self.wigyspan + 2*self.rbend,
                abYOffset - 2*self.rbend))
            ab2 = md.airBridge((self.xspan/2 - 2* self.wigyspan +2*self.rbend,
                abYOffset + 2*self.rbend))
        else: 
            ab1 = md.airBridge((self.xspan/2 +2*self.rbend - 2*self.wigyspan, 
                abYOffset - self.rbend))
            ab2 = md.airBridge((self.xspan/2 +2*self.rbend,
                abYOffset + self.rbend))        
        abCell.add([ab1, ab2])
        self.abCellr = cad.core.CellReference(abCell, origin=self.coords)
        self.abCellr.rotate(self.rot)


class Wiggle:
    
    def __init__(self, sampleX, nWiggles, leng, xspan, placeInfo, xOffset,
            yOffset, rbend, bridges, skew, rot):
        '''
        Construct a Wiggles
        '''
        
        #attributes
        self.nWiggles = nWiggles
        self.leng = leng
        self.xspan = xspan
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.rbend = rbend
        self.bridges = bridges
        self.skew = skew
        self.rot = rot
        
        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            self.coords = (self.cp[0] + self.xspan/2.*np.cos(rad(rot)) - self.skew*np.sin(rad(rot)),
                    self.cp[1] + self.xspan/2.*np.sin(rad(rot)) + self.skew*np.cos(rad(rot)))
        else:
            #its coordinates
            self.coords = placeInfo
        
        print 'wiggle Coords are :', self.coords

        #Connector locations
        self.connectA = (self.coords[0] - self.xspan/2.*np.cos(rad(rot)), 
                self.coords[1] - self.xspan/2.*np.sin(rad(rot)) - self.skew*np.cos(rad(rot)))
        self.connectB = (self.coords[0] + self.xspan/2.*np.cos(rad(rot)), 
                self.coords[1] + self.xspan/2.*np.sin(rad(rot)) + self.skew*np.cos(rad(rot)))
        print 'wiggle connector A at: ', self.connectA, ' and B at : ', self.connectB

        #make the cell
        self.makeCell()
 
        if bridges:
            self.addBridges(sampleX)
            sampleX.topCell.add(self.abCellr)

        #add Wigglecell to topCell
        sampleX.topCell.add(self.Cellr)


    def makeCell(self):

        #construct object
        self.Cellr, self.yspan = md.nWiggle(self.coords, self.leng, self.xspan, 
                self.nWiggles, xOffset = self.xOffset, 
                yOffset = self.yOffset, skew = self.skew, rot=self.rot)
   

    def addBridges(self, sampleX):
        '''
        add airbridges, by default 2 symmetrically around the center
        '''
        
        abCell = cad.core.Cell('AB')

        #multiplier to get the wiggles at the right spot 
        m = (-1)**(self.nWiggles/2)
        if self.nWiggles%2 == 1:
            ab1 = md.airBridge((self.xOffset - 2*self.rbend, self.yOffset - m*self.yspan),
                    rot = 90)
            ab2 = md.airBridge((self.xOffset + 2*self.rbend, self.yOffset - m*self.yspan),
                    rot = 90)
        else: 
            ab1 = md.airBridge((self.xOffset - self.rbend, self.yOffset - m*self.yspan),
                    rot = 90)
            ab2 = md.airBridge((self.xOffset + self.rbend, self.yOffset + m*self.yspan),
                    rot = 90)

        abCell.add([ab1, ab2])
        self.abCellr = cad.core.CellReference(abCell, origin=self.coords)
        self.abCellr.rotate(self.rot)



class GateLine:

    def __init__(self, sampleX, placeInfoLaunch, placeInfoTransmon, gapLen,
            extraLen, gapOffset, endrot, startrot):


        self.gapLen = gapLen
        self.extraLen = extraLen
        self.gapOffset = gapOffset
        self.endrot = endrot

        #Decide if we have coordinates or connection: For the Launcher
        if type(placeInfoLaunch) == str:
            #its a connection: get the coordinates!
            compL = getattr(sampleX, placeInfoLaunch.split('.')[0])
            self.Lcoords = getattr(compL, placeInfoLaunch.split('.')[1])
            self.Lrot = getattr(compL, 'rot')
        else:
            #its coordinates
            self.Lcoords = placeInfoLaunch
            self.Lrot = startrot
           
        #First, Add a gateLine End
        self.addGateLineEnd(sampleX, placeInfoTransmon)

        routeCell = sampleX.route(placeInfoLaunch, self.gateEndConnect,
                endrot=self.endrot, rot1 = self.Lrot)
        sampleX.topCell.add(routeCell)


    def addGateLineEnd(self, sampleX, placeInfoTransmon):
        '''
        Add a CPW + gap, as a gateLine end.
        Inputs:
            gapLen (taken from default values if not specified)
            gapOffset (default zero, otherwise a tuple (x, y)
            rot: rotation: ignored if placeInfo is a string
        '''

        totLen = self.gapLen + self.extraLen


        #PlaceInfo for the Transmon Box, compensated for the gateLineEnd
        if type(placeInfoTransmon) == str:
            #its a connection: get the coordinates!
            compT = getattr(sampleX, placeInfoTransmon.split('.')[0])
            self.Tcoords = getattr(compT, placeInfoTransmon.split('.')[1])
            Trot = getattr(compT, 'rot')

            #Endrot
            if self.endrot == 'l':
                GLErot = self.Lrot + 90
            elif self.endrot == 'r':
                GLErot = self.Lrot - 90
            else:
                GLErot = self.Lrot

            self.GLcoords = (self.Tcoords[0] + self.gapOffset[0]*np.cos(rad(Trot))
                    - np.cos(rad(GLErot))*(totLen/2+self.gapOffset[1]),
                    self.Tcoords[1]-(self.gapOffset[1]+totLen/2)*np.sin(rad(GLErot)) -
                    np.cos(rad(GLErot))*self.gapOffset[0])
        else:
            #its coordinates
            self.GLcoords = placeInfoTransmon
            self.GLErot = self.Lrot

        #draw!
        self.Cell = md.gateLineEnd(self.GLcoords, totLen, self.gapLen, rot=GLErot)

        #Connector
        self.gateEndConnect = (self.GLcoords[0] - np.cos(rad(GLErot))*(totLen/2),
                    self.GLcoords[1] -(totLen/2)*np.sin(rad(GLErot)))

        sampleX.topCell.add(self.Cell)

class FluxLine:

    def __init__(self, sampleX, placeInfoLaunch, placeInfoTransmon, fluxGap,
            extraLine, fluxLen, fluxOffset, endrot, startrot):

        #init
        self.fluxGap = fluxGap
        self.extraLine = extraLine
        self.fluxLen = fluxLen
        self.fluxOffset = fluxOffset
        self.endrot = endrot

        #Decide if we have coordinates or connection: For the Launcher
        if type(placeInfoLaunch) == str:
            #its a connection: get the coordinates!
            compL = getattr(sampleX, placeInfoLaunch.split('.')[0])
            self.Lcoords = getattr(compL, placeInfoLaunch.split('.')[1])
            self.Lrot = getattr(compL, 'rot')
        else:
            #its coordinates
            self.Lcoords = placeInfoLaunch
            self.Lrot = startrot
           
        #First, Add a gateLine End
        self.addFluxLineEnd(sampleX, placeInfoTransmon)

        routeCell = sampleX.route(placeInfoLaunch, self.fluxEndConnect, endrot =
                self.endrot, rot1 = self.Lrot)
        sampleX.topCell.add(routeCell)

    def addFluxLineEnd(self, sampleX, placeInfoTransmon):
        '''
        Add a CPW + gap, as a gateLine end.
        Inputs:
            gapLen (taken from default values if not specified)
            gapOffset (default zero, otherwise a tuple (x, y)
            rot: rotation: ignored if placeInfo is a string
        '''

        totLen = self.fluxLen + self.extraLine


        #PlaceInfo for the Transmon Box, compensated for the gateLineEnd
        if type(placeInfoTransmon) == str:
            #its a connection: get the coordinates!
            compT = getattr(sampleX, placeInfoTransmon.split('.')[0])
            self.Tcoords = getattr(compT, placeInfoTransmon.split('.')[1])
            Trot = getattr(compT, 'rot')

            #Endrot
            if self.endrot == 'l':
                FLErot = self.Lrot + 90
            elif self.endrot == 'r':
                FLErot = self.Lrot - 90
            else:
                FLErot = self.Lrot 

            self.FLcoords = (self.Tcoords[0] + self.fluxOffset[0]*np.cos(rad(Trot))
                    - np.cos(rad(FLErot))*(totLen/2+self.fluxOffset[1]),
                    self.Tcoords[1]-(self.fluxOffset[1]+totLen/2)*np.sin(rad(FLErot)) -
                    np.cos(rad(FLErot))*self.fluxOffset[0])
        else:
            #its coordinates
            self.FLcoords = placeInfoTransmon

        #draw!
        self.Cell = md.fluxLineEnd(self.FLcoords, totLen, fluxlen=self.fluxLen,
                fluxgap = self.fluxGap, rot=FLErot)

        #Connector
        self.fluxEndConnect = (self.FLcoords[0] - np.cos(rad(FLErot))*(totLen/2),
                    self.FLcoords[1] -(totLen/2)*np.sin(rad(FLErot)))

        sampleX.topCell.add(self.Cell)


class TransmonBox:
    '''
    Box for Transmon
    '''

    def __init__(self, sampleX, shape, placeInfo, offset, almarks, flip, corner, rot):
        '''
        Initialize Transmon Box properties

        The offset is relative to the placeInfo, such that the
        transmonBox can be connected to a resonator or wiggle connector

        When setting corner to True, shape is [widht, height]
        '''

        self.shape = shape
        self.offset = offset
        self.alMarks = almarks
        self.flip = flip
        self.corner = corner
        self.rot = rot

        #Include the CPW dimensions for easier connecting
        xlen2 = self.offset[0]# + self.shape[0]/2
        ylen2 = self.shape[not self.corner]/2. + sampleX.b1/2 + self.offset[1]
        
        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            if self.flip:
                self.coords = (self.cp[0] + (xlen2*np.cos(rad(rot)) + ylen2*np.sin(rad(rot))),
                    self.cp[1] - xlen2*np.sin(rad(rot)) + ylen2*np.cos(rad(rot)))
            else:
                self.coords = (self.cp[0] + (xlen2*np.cos(rad(rot)) - ylen2*np.sin(rad(rot))),
                    self.cp[1] + xlen2*np.sin(rad(rot)) - ylen2*np.cos(rad(rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #Add connectors for non-corner transmon
        (w, h) = self.shape #for easier typing
        if self.corner == False:
            self.connectA = (self.coords[0]-w/2*np.cos(rad(rot)), 
                    self.coords[1] + np.sin(rad(rot))*w/2)
            self.connectC = (self.coords[0]+w/2*np.cos(rad(rot)), 
                    self.coords[1] - np.sin(rad(rot))*w/2)
            if self.flip:
                self.connectB = (self.coords[0] + h/2*np.sin(rad(rot)),
                        self.coords[1]+self.shape[1]/2*np.cos(rad(rot)))
            else:
                self.connectB = (self.coords[0] -h/2*np.sin(rad(rot)),
                        self.coords[1]-self.shape[1]/2*np.cos(rad(rot)))
        else: #if its a corner transmon
            if flip:
                self.connectA = (self.coords[0] -w/2*np.cos(rad(rot)) + (w/2-h/2)*np.sin(rad(rot)), 
                    self.coords[1] - (w/2 - h/2)*np.cos(rad(rot)) + w/2*np.sin(rad(rot)))
                self.connectB = (self.coords[0] -(w/2-h/2)*np.cos(rad(rot)) + (w/2-h)*np.sin(rad(rot)), 
                    self.coords[1] - (w/2-h)*np.cos(rad(rot)) + (w/2-h/2)*np.sin(rad(rot)))
                self.connectC = (self.coords[0] +(w/2-h)*np.cos(rad(rot)) - (w/2-h/2)*np.sin(rad(rot)), 
                    self.coords[1] + (w/2-h/2)*np.cos(rad(rot)) - (w/2-h)*np.sin(rad(rot)))
                self.connectD = (self.coords[0] +(w/2-h/2)*np.cos(rad(rot)) -(w/2)*np.sin(rad(rot)), 
                    self.coords[1] + w/2*np.cos(rad(rot)) - (w/2-h/2)*np.sin(rad(rot)))
            else:
                self.connectA = (self.coords[0] -w/2*np.cos(rad(rot)) - (w/2-h/2)*np.sin(rad(rot)), 
                    self.coords[1] + (w/2 - h/2)*np.cos(rad(rot)) + w/2*np.sin(rad(rot)))
                self.connectB = (self.coords[0] -(w/2-h/2)*np.cos(rad(rot)) - (w/2-h)*np.sin(rad(rot)), 
                    self.coords[1] + (w/2-h)*np.cos(rad(rot)) + (w/2-h/2)*np.sin(rad(rot)))
                self.connectC = (self.coords[0] +(w/2-h)*np.cos(rad(rot)) + (w/2-h/2)*np.sin(rad(rot)), 
                    self.coords[1] - (w/2-h/2)*np.cos(rad(rot)) - (w/2-h)*np.sin(rad(rot)))
                self.connectD = (self.coords[0] +(w/2-h/2)*np.cos(rad(rot)) +(w/2)*np.sin(rad(rot)), 
                    self.coords[1] - w/2*np.cos(rad(rot)) - (w/2-h/2)*np.sin(rad(rot)))

        #make the cell
        self.makeCell()
        #Add to sample Cell
        sampleX.topCell.add(self.Cell)


    def makeCell(self):
        '''
        Use the maskDesign module to generate the object
        '''

        #construct object
        if self.corner:
            self.Cell = md.cornerTransmonBox(self.coords, self.shape,
                    rot=self.rot+(not self.flip)*90)
        else:
            self.Cell = md.transmonBoxAlign(self.coords, self.shape, self.alMarks, self.rot)



class AirBridge:

    def __init__(self, sampleX, placeInfo, bridgeLenX, bridgeLenY, footerLen,
            irGap, reflowGap, layers, rot):
        '''
        Initialize the Airbridge

        '''
        
        #Iinitialize Attributes
        self.bridgeLenX = bridgeLenX
        self.bridgeLenY = bridgeLenY
        self.footerLen = footerLen
        self.irGap = irGap
        self.reflowGap = reflowGap
        self.layers = layers
        self.rot = rot

        #Decide if we have coordinates or connection
        if type(placeInfo) ==  list:
            if type(placeInfo[0]) == str:
                print 'PlaceInfo not completely implemented yet'
            else:
                print 'PlaceInfo not completely implemented yet'
        if type(placeInfo) == str:
            print 'PlaceInfo not completely implemented yet'
            #its a connection: put one airbridge perpendicular to whatever I got
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.coords = getattr(comp, placeInfo.split('.')[1])
        if type(placeInfo) == tuple:
            #its coordinates
            self.coords = placeInfo

        #Make the Cell
        self.makeCell(sampleX)
        
    def makeCell(self,sampleX):
        '''
        make the cad Cell reference of the CPW
        '''
        self.Cell = md.airBridge(self.coords, footerLen = self.footerLen,
                bridgeSizeX = self.bridgeLenX, bridgeSizeY = self.bridgeLenY,
                reflowGap = self.reflowGap, irGap = self.irGap,
                layers = list(self.layers), rot=self.rot)

        #Add the cell to the TopCell
        sampleX.topCell.add(self.Cell)



class GapCoupler:

    def __init__(self, sampleX, gapSize, placeInfo, extralen, flip, rot):
        '''
        Construct a gapCoupler
        '''
        
        self.rot = rot
        self.gapSize = gapSize
        self.flip = flip
        
        #By default, make the length as long as the gap
        self.leng = self.gapSize + extralen

        #decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #adjust for the size of the component
            if flip:
                self.coords = (self.cp[0] - self.leng/2.*np.cos(rad(rot)),
                        self.cp[1] - self.leng/2.*np.sin(rad(rot)))
            else:
                self.coords = (self.cp[0] + self.leng/2.*np.cos(rad(rot)),
                        self.cp[1] - self.leng/2.*np.sin(rad(rot)))
      
        else:
            #its coordinates
            self.coords = placeinfo

        #Connector locations
        self.connectA = (self.coords[0] + self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] - self.leng/2.*np.sin(rad(rot)))
        self.connectB = (self.coords[0] - self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] + self.leng/2.*np.sin(rad(rot)))

        self.makeCell(sampleX)

    def makeCell(self, sampleX):

        #construct object
        self.Cell = md.gapCoupler(self.coords,self.gapSize,leng=self.leng,rot=self.rot)
        #Add to sample Cell
        sampleX.topCell.add(self.Cell)
        

class FingerCap:
    
    def __init__(self, sampleX, nFingers, placeInfo, fingerLen, fingerThick,
            gapHeight, gapWidth, flip, rot):
        '''
        Construct a gapCoupler
        '''
        
        #attributes
        self.nFingers = nFingers
        self.fingerLen = fingerLen
        self.fingerThick = fingerThick
        self.gapHeight = gapHeight
        self.gapWidth = gapWidth
        self.flip = flip
        self.rot = rot
        
        self.leng = fingerLen + 2*gapWidth
        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            if flip:
                self.coords = (self.cp[0] - self.leng/2.*np.cos(rad(rot)),
                        self.cp[1] + self.leng/2.*np.sin(rad(rot)))
            else:
                self.coords = (self.cp[0] + self.leng/2.*np.cos(rad(rot)),
                        self.cp[1] - self.leng/2.*np.sin(rad(rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #Connector locations
        self.connectA = (self.coords[0] - self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] + self.leng/2.*np.sin(rad(rot)))
        self.connectB = (self.coords[0] + self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] - self.leng/2.*np.sin(rad(rot)))

        self.makeCell(sampleX)

    def makeCell(self, sampleX):

        #construct object
        self.Cell = md.fingerCap(self.coords,self.nFingers, self.fingerLen,
                self.fingerThick, self.gapHeight, self.gapWidth, rot=self.rot)
        #Add to sample Cell
        sampleX.topCell.add(self.Cell)



class FingerCoupler:
    
    def __init__(self, sampleX, nFingers, placeInfo, fingerLen, fingerThick,
            gapHeight, gapWidth, taperLen, centerLen, flip, rot):
        '''
        Construct a gapCoupler
        '''
        
        #attributes
        self.nFingers = nFingers
        self.fingerLen = fingerLen
        self.fingerThick = fingerThick
        self.gapHeight = gapHeight
        self.gapWidth = gapWidth
        self.taperLen = taperLen
        self.centerLen = centerLen
        self.flip = flip
        self.rot = rot
        
        self.leng = centerLen + 2*taperLen
        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.cp = getattr(comp, placeInfo.split('.')[1])
            #Adjust for the size of the component
            if flip:
                self.coords = (self.cp[0] - self.leng/2.*np.cos(rad(rot)),
                        self.cp[1] + self.leng/2.*np.sin(rad(rot)))
            else:
                self.coords = (self.cp[0] + self.leng/2.*np.cos(rad(rot)),
                        self.cp[1] - self.leng/2.*np.sin(rad(rot)))
        else:
            #its coordinates
            self.coords = placeInfo

        #Connector locations
        self.connectA = (self.coords[0] - self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] + self.leng/2.*np.sin(rad(rot)))
        self.connectB = (self.coords[0] + self.leng/2.*np.cos(rad(rot)), 
                self.coords[1] - self.leng/2.*np.sin(rad(rot)))

        self.makeCell(sampleX)

    def makeCell(self, sampleX):

        #construct object
        self.Cell = md.fingerCoupler(self.coords,self.nFingers, self.fingerLen,
                self.fingerThick, self.gapHeight, self.gapWidth, 
                self.taperLen, self.centerLen, rot=self.rot)
        #Add to sample Cell
        sampleX.topCell.add(self.Cell)
        

class CText:
    
    def __init__(self, sampleX, text, fontSize, placeInfo, font, rot, layer):

        self.text = text
        self.fontSize = fontSize
        self.coords = placeInfo
        self.rot = rot
        self.layer = layer
        self.font = font

        #add to the total layout
        self.makeCell()
        sampleX.topCell.add(self.Cell)

    def makeCell(self):
        self.Cell = md.chipText(self.coords, self.text, self.fontSize,
                self.font, self.layer, self.rot)



class CrossArray:

    def __init__(self, sampleX, placeInfo):

        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.coords = getattr(comp, placeInfo.split('.')[1])
        else:
            #its coordinates
            self.coords = placeInfo

        self.makeCell()
        sampleX.topCell.add(self.Cell)

    def makeCell(self):
        self.Cell = md.crossArray(self.coords)


class FourPoint:

    def __init__(self, sampleX, placeInfo, rot):
        '''
        Currently all options are hardcoded in fourPoint, 
        but they are ready to be adapted to here
        '''
        #attributes
        self.rot = rot
        
        #Decide if we have coordinates or connection
        if type(placeInfo) == str:
            #its a connection: get the coordinates!
            comp = getattr(sampleX, placeInfo.split('.')[0])
            self.coords = getattr(comp, placeInfo.split('.')[1])
        else:
            #its coordinates
            self.coords = placeInfo

        
        self.Cell = md.fourPoint(self.coords, rot) 

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

