import gdsCAD as cad
import matplotlib as mpl
import numpy as np
import defaultParms as dp

defaults = dp.dPars()

#Separate file for sizes etc?

#TODO
#Qudev-style alignment marker:
#GateLines/FluxLines
#Easy way to add airbridges


#inner conductor
# ic-to-ground distance

um = 1e3
mm = 1e6
a1, b1 = defaults['centerConductor'], defaults['CPWGap'] 

cad.core.default_layer = 0


#Common abbreviations in the Mathematica file:
#a1 = half center width of CPW
#ar = half center width of launcher
#abrl = a/b ratio (b being outside of gap)
#abrr = a/b ratio of launcher
#
##in GateLine
#distance= gap between end center conductor and end of the line
#offset: offset of the end on the x-axis relative to launcher
#================ PRIMITIVES ====================================


def border(xlen,ylen,gap, layer=0):
    '''
    Makes a border for a chip, with a width of gap/2. 
    '''

    boxCell = cad.core.Cell('border')
  
    #Outer Box: Cw, inner_box CCW, keyhole
    outerpoints = [[0, ylen/2.+gap/2.],[xlen/2.+gap/2.,ylen/2.+gap/2.],
            [xlen/2.+gap/2.,-ylen/2.-gap/2.],[-xlen/2.-gap/2.,-ylen/2.-gap/2.],
            [-xlen/2.-gap/2.,ylen/2.+gap/2.],[0,ylen/2.+gap/2.]]
    innerpoints = [[0,ylen/2.],[-xlen/2.,ylen/2.],[-xlen/2.,-ylen/2.],
            [xlen/2.,-ylen/2.], [xlen/2.,ylen/2.],[0,ylen/2.]]
    allpoints = innerpoints + outerpoints
    
    bound = cad.core.Boundary(allpoints, layer=layer) 
    boxCell.add(bound)

    return boxCell 

def borderA(xlen,ylen,gap, alignPos):
    '''
    Makes a border for a chip, with a width of gap/2,
    Inlcudes Alignment Markers
    '''

    print 'generating borders'

    boxCell = cad.core.Cell('BORDER')
    boundbox = border(xlen,ylen,gap)
    boxCell.add(boundbox)

    #Alignment marks
    dis = defaults['alignDistance']   #distance from markers to edge
    alignCell = cad.core.Cell('ALIGN')

    #alignArray = cad.core.CellArray(Align, 2, 2, (xlen - 2*dis, ylen - 2*dis))
    #alignCell.add(alignArray)
    
    if 0 in alignPos:    
        Align0 = alignMarks((-xlen/2+dis, ylen/2-dis))
        boxCell.add(Align0)
    if 1 in alignPos:
        Align1 = alignMarks((xlen/2.-dis,ylen/2.-dis))
        boxCell.add(Align1)
    if 2 in alignPos:
        Align2 = alignMarks((xlen/2.-dis,-ylen/2.+dis))
        boxCell.add(Align2)
    if 3 in alignPos:
        Align3 = alignMarks((-xlen/2.+dis,-ylen/2.+dis))
        alignCell.add(Align3)
    
    boxCell.add(alignCell)
 
    return boxCell 


def CPW(coords,leng, center=10*um,gap=19*um, closeA=False, closeB=False,
        bridges=False, rot=0):
    '''
    A straight piece of co-planar waveguide
    center = the width of the center conductor
    gap = the width of the cut in the ground plane in which the center conductor is placed
    rot = rotation in degrees

    returns a cell
    '''
    cpwCell = cad.core.Cell('CPW')
    startx, starty = coords


    #points in the path
    guppoints = [(-leng/2, center/2.),(leng/2, center/2.),
            (leng/2, gap/2.),(-leng/2., gap/2.)]
            
    gdownpoints = [(-leng/2, -center/2.),(leng/2, -center/2.),
            (leng/2, -gap/2.), (-leng/2, -gap/2.)]

    #add to Boundary
    gapup = cad.core.Boundary(guppoints)
    gapdown = cad.core.Boundary(gdownpoints)

    #if close, close the line:
    if closeA:
        cad.shapes.Rectangle((-leng/2, -center/2),
                (-leng/2+(center-gap)/2, center/2))
    if closeB:
        cad.shapes.Rectangle((leng/2, -center/2),
                (leng/2-(center-gap)/2, center/2))


    #add to the cell
    cpwCell.add([gapup,gapdown])
      #airBridges
    if bridges:

        #default values
        bridgeDistance = defaults['ABdistance']
        bridgeStart = defaults['ABstart']
        bridgeEnd = defaults['ABend']

        #Cell for bridges
        bridgeCell = cad.core.Cell('AB')
        xloc = bridgeDistance/2.

        #generate airbride locations:
        xlocs1 = np.arange(0, -leng/2+bridgeStart, -bridgeDistance)[::-1] 
        #if leng/2-bridgeEnd > bridgeDistance:
        xlocs2 = np.arange(bridgeDistance, leng/2-bridgeEnd, bridgeDistance)
        xlocs = np.concatenate([xlocs1, xlocs2])
        
        #Generate airbridges symmetrically around 0
        for x in xlocs:
            ab = airBridge((x,0), rot=90)
            bridgeCell.add(ab)

        #add to main cell
        cpwCell.add(bridgeCell)
    
    cpwCellr = cad.core.CellReference(cpwCell,rotation=rot)
    cpwCellr.translate(coords)

    return cpwCellr


def CPWArc(coords,initangle=270,degrees=90,
        radius=100.*um,center=10.*um,gap=19.*um,rot=0.):
    '''
    draw a CPW arc of pirad * pi radians.
    Radius, centerconductor widht and gap width are input arguments

    '''

    arcCell = cad.core.Cell('ARC')
    
    startx, starty = coords[0], coords[1]
    #The discs
    discouter = cad.shapes.Disk((0.,0.),radius+gap/2., inner_radius=radius+center/2.,
            initial_angle=initangle,final_angle=initangle+degrees)

    discinner = cad.shapes.Disk((0.,0.),radius-center/2., inner_radius=radius-gap/2.,
            initial_angle=initangle,final_angle=initangle+degrees)

    arcCell.add([discinner,discouter])

    #rotate
    arcCellr = cad.core.CellReference(arcCell,rotation=rot)
    arcCellr.translate(coords)

    return arcCellr


def taper(coords,taperlen, startOuter, endOuter,
        startInner,endInner,rot=0):
    '''
    General purpose taper drawer, for use in example couplers and launchers
    tapers from any start to any end within length taperlen
    '''
    taperCell = cad.core.Cell('TAPER')

    #draw it!
    pointsup = [(-taperlen/2.,startOuter/2.),(taperlen/2.,endOuter/2.),
            (taperlen/2.,endInner/2.),(-taperlen/2.,startInner/2.)]

    pointsdown = [(-taperlen/2.,-startOuter/2.),(taperlen/2.,-endOuter/2.),
            (taperlen/2.,-endInner/2.),(-taperlen/2.,-startInner/2.)]

    #draw the boundaries
    bdup = cad.core.Boundary(pointsup)
    bddown = cad.core.Boundary(pointsdown)

    #add to cell
    taperCell.add([bdup,bddown])

    #rotate and translate
    taperCellr = cad.core.CellReference(taperCell, rotation=rot)
    taperCellr.translate(coords)

    return taperCellr


def launcher(coords,startcenterwidth=150*um,startgrwidth=150*1.9*um,
        startlength=250.*um,taperlength=250.*um, center=10.*um, gap=19.*um, rot=0.):
    '''
    draw a launcher:
    '''
    
    #init
    launcherCell = cad.core.Cell('LAUNCHER')
    startx, starty = coords

    #define points
    gapuppoints = [(0,startgrwidth/2.),
            (startlength,startgrwidth/2.),
            (taperlength+startlength,gap/2.),
            (taperlength+startlength,center/2.),
            (startlength,startcenterwidth/2.),
            (0,startcenterwidth/2.)]

    gapdownpoints = [(0,-startgrwidth/2.),
            (startlength,-startgrwidth/2.),
            (taperlength+startlength,-gap/2.),
            (taperlength+startlength,-center/2.),
            (startlength,-startcenterwidth/2.),
            (0,-startcenterwidth/2.)]

    #draw the boundaries
    bdup = cad.core.Boundary(gapuppoints)
    bddown = cad.core.Boundary(gapdownpoints)

    #add to the cell
    launcherCell.add([bdup,bddown])

    #rotate
    launcherCellr = cad.core.CellReference(launcherCell,rotation=rot)
    launcherCellr.translate(coords)

    return launcherCellr


def simpleCross(size,thick,layer=0):
    '''
    used for transmonAlignment, draws a cross and returns it
    '''

    crossCell = cad.core.Cell('CROSS')

    hsize, hthick = size/2., thick/2.
    points = [(-hsize,hthick),(-hthick, hthick),(-hthick,hsize),
            (hthick,hsize),(hthick,hthick),(hsize,hthick),
            (hsize,-hthick),(hthick,-hthick),(hthick,-hsize),
            (-hthick,-hsize),(-hthick,-hthick),(-hsize,-hthick)]
    sCross = cad.core.Boundary(points, layer=layer)

    crossCell.add(sCross)

    return crossCell

def transmonBox(coords,shape,rot=0):
    '''
    Empty box for the transmon, centered at coords
    '''

    transmonCell = cad.core.Cell('TR_BOX')

    startcoords = (coords[0]-shape[0]/2.,coords[1]-shape[1]/2.)
    endcoords = (coords[0]+shape[0]/2.,coords[1]+shape[1]/2.)
    
    trbox = cad.shapes.Rectangle(startcoords,endcoords)

    transmonCell.add(trbox)

    transmonCellr = cad.core.CellReference(transmonCell, rotation=rot)
    print 'generating a transmon box'

    return transmonCellr

def transmonBoxAlign(coords,shape, almarks = [2,2], rot=0):
    '''
    Empty box for the transmon, centered at coords
    For almarks, use [2,2] or [2,1] or [1,2]
    '''

    transmonCell = cad.core.Cell('TR_BOX')

    startcoords = (-shape[0]/2.,-shape[1]/2.)
    endcoords = (shape[0]/2.,shape[1]/2.)
    
    trbox = cad.shapes.Rectangle(startcoords,endcoords)
    
    transmonCell.add(trbox)

    #Alignment marks
    bCross = simpleCross(30*um,10*um)
    sCross = simpleCross(12*um, 2*um)
    bigDis = 300*um
    smallDis = 250*um

    for i in range(len(almarks)):
        if almarks[i]==2:
            ym = (-1)**i
            transmonCell.add(bCross,origin=(bigDis/2, ym*bigDis/2))
            transmonCell.add(bCross,origin=(-bigDis/2, ym*bigDis/2))
            transmonCell.add(sCross,origin=(smallDis/2, ym*smallDis/2))
            transmonCell.add(sCross,origin=(-smallDis/2, ym*smallDis/2))
        elif almarks[i]==1:
            transmonCell.add(bCross,origin=(0,bigDis/2))
            transmonCell.add(sCross,origin=(0,ym*smallDis/2))
        elif almarks[i]==0:
            continue
            
        elif almarks[i]>2 or almarks[i] < 0:
            print 'Use almarks of [2,2] or less'

    #translate to coords
    transmonCellr = cad.core.CellReference(transmonCell, rotation=rot)
    transmonCellr.translate(coords)
    print 'generating a transmon box with markers'

    return transmonCellr

def cornerTransmonBox(coords, shape=(300*um, 200*um), rot=0):
    '''
    Empty box for the corner transmon, centered at coords
    Height is the direction perpendicular to the transmission lines,
    Width is parallel
    '''

    transmonCell = cad.core.Cell('TR_BOX')
    alignCell = cad.core.Cell('ALIGN')

    # for easier reading and writing
    width, height = shape

    #points defining the box shape
    pointlist = [(-width/2,-width/2),(width/2.,-width/2.),
            (width/2, width/2),(width/2-height, width/2),
            (width/2-height, -width/2+height),(-width/2, -width/2+height),
            (-width/2., -width/2)]
    corner = cad.core.Boundary(pointlist)

    #add to Cell
    transmonCell.add(corner)

    #Alignment marks
    bCross = simpleCross(30*um,10*um)
    sCross = simpleCross(12*um, 2*um)

    #First implementation: standard alignment marks
    spacing = 75*um
    #Arange them first in a triangle through zero. Feel free to make spacing a
    #function parameter

    #Big crosses
    alignCell.add(bCross,origin=(-2*spacing, -2*spacing))
    alignCell.add(bCross,origin=(2*spacing, -2*spacing))
    alignCell.add(bCross,origin=(2*spacing, 2*spacing))
    #Small crosses
    alignCell.add(sCross,origin=(-spacing, -spacing))
    alignCell.add(sCross,origin=(spacing, -spacing))
    alignCell.add(sCross,origin=(spacing, spacing))
    
    #Translate crosses to center around the corner of the transmon
    alignCellr = cad.core.CellReference(alignCell, origin=(width/2,-width/2))
    transmonCell.add(alignCellr)
    
    #translate and rotate
    transmonCellr = cad.core.CellReference(transmonCell, rotation=rot)
    transmonCellr.translate(coords)
    print 'generating a transmon box with markers'

    return transmonCellr


def gapCoupler(coords,gapSize,center=10.*um,gap=19.*um,leng=100*um,rot=0):
    '''
    Build a gap capacitor, with a gap which is gapsize wide
    '''

    print 'adding a gap coupler'

    #init
    couplerCell = cad.core.Cell('COUPLER')

    #drawing the components
    theGap = cad.shapes.Rectangle((-gapSize/2.,-center/2.),(gapSize/2.,center/2.))
    cpw = CPW((0.,0),leng, center=center, gap=gap, rot=0)
    couplerCell.add([theGap,cpw])

    #rotate and translate
    couplerCellr = cad.core.CellReference(couplerCell, rotation=rot)
    couplerCellr.translate(coords)

    return couplerCellr

def fingerCap(coords, nfingers, fingerlen, fingerthick, gapheight, gapwidth, rot=0):
    '''
    Build a finger capacitor with nfinger fingers.
    The gap between the finger is 'gapheight' high and 'gapwidth' wide
    '''
    try:
        nfingers > 2
    except ValueError:
        print 'Needs at least two fingers'

    #init
    capCell = cad.core.Cell('CAP')

    capwidth = nfingers*fingerthick + (nfingers-1)*gapheight

    #for the gaps, make the squares in advance, origin in left upper point
    smallCell = cad.core.Cell('SMALL')
    smallCell.add(cad.shapes.Rectangle((0,0),(gapwidth,-fingerthick)))
    
    longCell = cad.core.Cell('LONG')
    longr = cad.shapes.Rectangle((0,0),(fingerlen+2*gapwidth,-gapheight))
    longCell.add(longr)

    #First block
    capCell.add(smallCell,origin=(-fingerlen/2-gapwidth,capwidth/2.))

    #Components 2: the gap
    for n in range(nfingers-1):
        smallCellt = cad.core.CellReference(smallCell, 
                origin=(((-1)**n)*(fingerlen/2.+gapwidth/2.)-gapwidth/2,capwidth/2.-(n+1)*(fingerthick+gapheight)))
        capCell.add(smallCellt)
        capCell.add(longCell,origin=(-fingerlen/2.-gapwidth,
            capwidth/2. - (n+1)*fingerthick - n*gapheight))

    #rotate and translate
    capCellr = cad.core.CellReference(capCell, rotation=rot)
    capCellr.translate(coords)

    return capCellr



def fingerCoupler(coords, nfingers, fingerlen, fingerthick, gapheight, gapwidth,
        taperlen, centerlen, center=10.*um,gap=19.*um,rot=0):
    '''
    Build a finger capacitor with nfinger fingers.
    The gap between the finger is 'gapheight' high and 'gapwidth' wide
    The taper is determined by 'capwidth' and 'capgapwidth'
    '''
    try:
        nfingers > 2
    except ValueError:
        print 'Needs at least two fingers'

    try:
        fingerlen < centerlen
    except ValueError:
        print 'The fingers cannot be longer than the capacitor'

    #init
    couplerCell = cad.core.Cell('COUPLER')

    capwidth = nfingers*fingerthick + (nfingers-1)*gapheight
    capgapwidth = capwidth*(gap/center)

    #components: tapers: dont draw if len = 0
    if taperlen != 0:
        tap1 = taper((-taperlen/2.-centerlen/2.,0),taperlen,gap,capgapwidth,
                center,capwidth)
        tap2 = taper((taperlen/2.+centerlen/2.,0),taperlen,capgapwidth,gap,
                capwidth,center)
        couplerCell.add([tap1, tap2])

    #CPW
    cpw = CPW((0.,0),centerlen,center=capwidth,gap=capgapwidth)
    couplerCell.add(cpw) 

    #Draw the capacitor by using the fingerCap function
    fingers = fingerCap((0,0), nfingers, fingerlen, fingerthick, gapheight,
            gapwidth, rot=0)

    #add to cell
    couplerCell.add(fingers)

    #rotate and translate
    couplerCellr = cad.core.CellReference(couplerCell, rotation=rot)
    couplerCellr.translate(coords)

    return couplerCellr


def gateLineEnd(coords,linelen,gaplen,center=10*um,gap=19.*um,rot=0):
    '''
    gateline end

    Origin in the center
    '''

    gateCell = cad.core.Cell('GATE')

    cpw = CPW((0.,0),linelen,center=center,gap=gap)
    gap = cad.shapes.Rectangle((linelen/2.-gaplen,-center/2.),
            (linelen/2.,center/2,))
    gateCell.add([cpw,gap])
 
    #rotate and translate
    gateCellr = cad.core.CellReference(gateCell, rotation=rot)
    gateCellr.translate(coords)

    return gateCellr


def fluxLineEnd(coords,totlen,fluxlen=40*um,taplen=10*um, fluxgap=2*um,
        fluxwidth=None, orient='down',center=10.*um, gap=19.*um,rot=0):
    '''
    fluxline end
    fluxwidth is total width of the fluxline structure close to the qubit.
    fluxlen is the total length of the fluxend structure
    fluxgap is the gap left for the current to flow at the end of the line:
    between the transmongap and the CPW gap
    orient determines on which side the line is closed
    '''

    if fluxwidth == None: fluxwidth = defaults['fluxWidth']
    if fluxgap == None: fluxgap = defaults['fluxGap']

    #Check 
    if orient not in ['up', 'down']:
        raise ValueError, 'orient has to be either up or down (pass as string)'

    fluxCell = cad.core.Cell('FLUX')
    endCell = cad.core.Cell('END')

    #drawing the structure
    fluxpointsup = [(0, gap/2.),
                (taplen, fluxwidth/2.),
                (fluxlen-fluxgap, fluxwidth/2.),
                (fluxlen-fluxgap, fluxgap/2.),
                (taplen, fluxgap/2.),
                (0, center/2.)]
    fluxpointsdown = [(0, -gap/2.),
                (taplen, -fluxwidth/2.),
                (fluxlen-fluxgap, -fluxwidth/2.),
                (fluxlen-fluxgap, -fluxgap/2.),
                (taplen, -fluxgap),
                (0, -center/2.)]
    fluxendup = cad.core.Boundary(fluxpointsup)  
    fluxenddown = cad.core.Boundary(fluxpointsdown)  
    
    fluxCell.add([fluxendup, fluxenddown])
    fluxCellr = cad.core.CellReference(fluxCell, 
            origin=(totlen/2. - fluxlen,0))

    cpw = CPW((-fluxlen/2.,0),totlen-fluxlen,center=center,gap=gap)
    endCell.add([cpw, fluxCellr])

    #rotate and translate
    endCellr = cad.core.CellReference(endCell, rotation=rot)
    endCellr.translate(coords)

    return endCellr

def fluxLineEndAsym(coords,totlen,fluxlen,taplen=10*um, fluxgap=2*um,
        fluxwidth=7*um, orient='down',center=10.*um, gap=19.*um,rot=0):
    '''
    fluxline end
    fluxwidth is the extra width the fluxline gets compared to gap and center
    fluxlen is the total length of the fluxend structure
    fluxgap is the gap left for the current to flow at the end of the line:
    between the transmongap and the CPW gap
    orient determines on which side the line is closed
    '''

    #Check 
    if orient not in ['up', 'down']:
        raise ValueError, 'orient has to be either up or down (pass as string)'

    fluxCell = cad.core.Cell('FLUX')
    endCell = cad.core.Cell('END')

    gapwidth = (gap-center)/2.

    fluxpoints = [(0, gapwidth/2.),
                (taplen, gapwidth/2. + fluxwidth),
                (fluxlen-fluxgap, gapwidth/2. + fluxwidth),
                (fluxlen-fluxgap, -gapwidth/2. - fluxwidth),
                (taplen, -gapwidth/2. - fluxwidth),
                (0, -gapwidth/2.)]
    fluxend = cad.core.Boundary(fluxpoints)  
    endCell.add(fluxend)

    cpw = CPW((-fluxlen,0),totlen-fluxlen,center=center,gap=gap)
    if orient == 'down':
        #up is an elongation of the cpw
        up = cad.shapes.Rectangle((totlen/2.-fluxlen,center/2.),(totlen/2.,gap/2.))
        #down is a translated version of the end
        endCellt = cad.core.CellReference(endCell,origin=(totlen/2.-fluxlen,-1*(center+gap)/4))
        fluxCell.add([up,cpw,endCellt])
    if orient == 'up':
        down = cad.shapes.Rectangle((totlen/2.-fluxlen,-center/2.),(totlen/2.,-gap/2.))
        #up
        endCellt = cad.core.CellReference(endCell,origin=(totlen/2.-fluxlen,(center+gap)/4))
        fluxCell.add([down,cpw,endCellt])
    #rotate and translate
    fluxCellr = cad.core.CellReference(fluxCell, rotation=rot)
    fluxCellr.translate(coords)

    return fluxCellr


def airBridge(coords,footerLen=30*um,bridgeSizeX=40*um,bridgeSizeY=10*um,
        reflowGap=3*um,irGap=40*um, layers = [2,1], rot=0):
    '''
    Create an Airbridge Qudev style:

        With default values (layers = [2,1,25]), you get:
        narrow bridge in layer 2
        footpoints in layer 1
        nothing in layer 0

        bridgeSize is a list of shape [width, height]
    '''
    #init
    bridgeCell = cad.core.Cell('BRIDGE')

    #bridge
    bridge = border(bridgeSizeX+2*footerLen, bridgeSizeY, 2*irGap, layer=layers[0])
    bridgeCell.add(bridge)

    #supportBoxes
    support1 = cad.shapes.Rectangle((-bridgeSizeX/2.-reflowGap-footerLen,-bridgeSizeY/2.-reflowGap),
        (-bridgeSizeX/2.+reflowGap,bridgeSizeY/2.+reflowGap),layer=layers[1])
    support2 = cad.shapes.Rectangle((bridgeSizeX/2.-reflowGap,-bridgeSizeY/2.-reflowGap),
        (bridgeSizeX/2.+footerLen+reflowGap,bridgeSizeY/2.+reflowGap),layer=layers[1])
    bridgeCell.add([support1, support2])

    #rotate and translate
    bridgeCellr = cad.core.CellReference(bridgeCell, rotation=rot)
    bridgeCellr.translate(coords)

    return bridgeCellr


def chipText(coords, text, fontsize=100*um, font='romand', layer=25,rot=0):
    '''
    Generate text
    '''
    textCell = cad.core.Cell('TEXT')

    #Special case for blockfont
    if font == 'blocky':
        texts = cad.shapes.Label(text,fontsize,coords,layer=layer)
    else:
        texts = cad.shapes.LineLabel('',fontsize,layer=layer)
        texts.add_text(text,font)

    textCell.add(texts)

    #rotate and translate
    textCellr = cad.core.CellReference(textCell, rotation=rot)
    textCellr.translate(coords)

    return textCellr


#=================COMBINED FUNCTIONS=============================

def doubleArc(coords, dy, rbend = 100*um, rot=0):

    dACell = cad.core.Cell('DOUBLEARC')

    #defaults
    center = defaults['centerConductor']
    gap = defaults['CPWGap']
    
    #Calculate angle
    phirad = np.arccos(1-abs(dy)/(rbend*2))
    print 'phirad is ', phirad
    phi = phirad*360/2/np.pi    #convert to degrees

    #start and end coords:
    startc = (-rbend*np.sin(phirad), rbend-abs(dy)/2)
    endc = (rbend*np.sin(phirad), -rbend+abs(dy)/2)
    xspan = endc[1]*2

    #draw Arcs
    if dy>=0:
        arc1Cell = CPWArc(startc, 270, phi, rbend, center, gap)
        arc2Cell = CPWArc(endc, 90, phi, rbend, center, gap)
    else:
        print 'less than zero'
        arc1Cell = CPWArc((startc[0], -startc[1]), 90, -phi, rbend, center, gap)
        arc2Cell = CPWArc((endc[0], -endc[1]), 270, -phi, rbend, center, gap)

    dACell.add([arc1Cell, arc2Cell])
    
    #translate, rotate, reflect
    dACellr = cad.core.CellReference(dACell, rotation=rot)
    dACellr.translate(coords)

    return dACellr, xspan


def sLine(coords,yspan,rbend=100.*um,enter=True,exit=True,reflect=False,
        bridges=False, rot=0):
    '''
    Makes a CPW line with connected arcs of total yspan as indicated
    If exit and enter are True, a quarter circle bend is generated at the end
    and/or start of the line
    '''

    sLineCell = cad.core.Cell('SLINE')
    
    #parameters for vertical piece depend on exit and enter
    vlen = yspan
    vstart = 0.
    vlen = float(vlen)

    #Arcs
    if enter:
        if reflect:
            enArc = CPWArc((-rbend,yspan/2.-rbend), initangle = 0., radius=rbend)
        else:
            enArc = CPWArc((-rbend,-yspan/2.+rbend),radius=rbend)
        vstart += rbend/2.
        vlen -= rbend
        sLineCell.add(enArc)

    if exit:
        if reflect:
            exArc = CPWArc((rbend,-yspan/2.+rbend),initangle =180., radius=rbend)
        else:
            exArc = CPWArc((rbend,yspan/2.-rbend),initangle =90., radius=rbend)
        vlen -= rbend
        vstart -= rbend/2.
        sLineCell.add(exArc)

    
    #straight piece
    if reflect:
        vPiece = CPW((0,vstart),vlen, bridges = bridges, rot=90.)
    else:
        vPiece = CPW((0,vstart),vlen, bridges = bridges, rot=90.)
    #add to cell
    sLineCell.add(vPiece)
   
    #rotate, translate
    sLineCellr = cad.core.CellReference(sLineCell, rotation=rot)
    sLineCellr.translate(coords)

    return sLineCellr

def jLine(coords, totlen, xspan, yspan, nWiggles, rbend=100*um, bridges= True, rot = 0):
        '''
        use Wiggle , sLine and CPW

        The origin of this piece is in the horizontal part of the sLine
        '''

        #Initialize the cell
        jCell = cad.core.Cell('JLINE')

        #sLine
        sline = sLine((0,0), yspan = xspan, enter=False, rot=-90)
        jCell.add(sline)

        #wiggle
        wigLen = totlen - xspan + (np.pi/2 - 1)*rbend
        wigOffset = yspan/2 - (2*nWiggles-2)*rbend
        #Build a wiggle to get the yspan
        wiggle, wigyspan1 = nWiggle((xspan/2, -yspan/2-rbend/2), wigLen, yspan-rbend, nWiggles,
                rbend=rbend, xOffset = -wigOffset, rot=-90)
        #build the wiggle to be used
        wiggle2, wigyspan = nWiggle((xspan/2, -yspan/2 - rbend/2), wigLen, yspan-rbend, nWiggles,
                rbend=rbend, xOffset = -wigOffset, yOffset = -wigyspan1 +
                2*rbend, rot=-90)
        jCell.add(wiggle2)

        #Close the ends
        r1 = cad.shapes.Rectangle((-xspan/2 - (b1/2-a1/2), -b1/2),
                (-xspan/2, b1/2))
        r2 = cad.shapes.Rectangle((xspan/2 - b1/2, -yspan),
                (xspan/2+b1/2, -yspan - (b1/2 - a1/2)))
        jCell.add([r1,r2])

        #rotate and translate
        jCellr = cad.core.CellReference(jCell, rotation=rot)
        jCellr.translate(coords)

        return jCellr, wigyspan


def nWiggle(coords,totlen,xspan,nwiggle,rbend=100.*um,
        center=10.*um,gap=19.*um,yOffset=0.,xOffset=0., skew=0, rot=0.):
    '''
    make a wiggled transmission line. 
    This function uses CPW and sLine

    Returns the wiggle Cell and yspan
    '''

    print 'generating a wiggle pattern'
    #SelfChecks
    if nWiggle < 1:
        raise Exception, 'nwiggle needs to be at least one for this function to work'

    if xspan <= (nwiggle+1)*2*rbend:
        raise Exception, 'xspan too short for the number of wiggles'

    if totlen - np.pi*rbend*(nwiggle+1) - (xspan - 2*rbend*(nwiggle+1)) < 0:
        raise Exception, 'number of wiggles causes a length longer than totlen \
            long vertical pieces!\n Reduce nwiggle or increase totlen'

    #total straight
    straightx = xspan - 2*rbend*(nwiggle+1)

    if nwiggle%2==0:
        ylentot = totlen - straightx - np.pi*rbend*(nwiggle+1) - 2* skew
    else:
        ylentot = totlen - straightx - np.pi*rbend*(nwiggle+1) 
    yspan = (ylentot+2*rbend*(nwiggle+1))/(2*nwiggle) #Beware the entry and exit arc,
    yspan = float(yspan)
    print 'yspan is', yspan

    if 2*yspan < yOffset + 2* rbend:
        raise ValueError, 'Your yOffset should be smaller than your wiggle is high plus twice rbend'

    #which make the first vertical pieces shorter!
    totlenc = 0

    #init
    wiggleCell = cad.core.Cell('WIGGLE')

    #left part of straight
    leftLine = CPW((-xspan/2.+straightx/4+xOffset/2.,-skew),straightx/2.+xOffset)
    rightLine = CPW((xspan/2.-straightx/4.+xOffset/2.,skew),straightx/2.-xOffset)
    wiggleCell.add([leftLine,rightLine])
    totlenc += straightx

    #enter and exit arc
    enArc = sLine((-xspan/2.+straightx/2.+xOffset+rbend,-skew/2+yspan/2.+yOffset/2.),yspan+yOffset+skew)

    totlenc += np.pi*rbend+yspan + skew-2.*rbend+yOffset
    if nwiggle%2==0:
        exArc = sLine((-xspan/2.+straightx/2.+xOffset+nwiggle*2*rbend+rbend,
            -yspan/2.+yOffset/2.+skew/2.),yspan-yOffset + skew)
        totlenc += np.pi*rbend +yspan + skew-2*rbend-yOffset
    else:
        exArc = sLine((-xspan/2.+straightx/2.+xOffset+nwiggle*2.*rbend+rbend,
            yspan/2.+yOffset/2.+skew/2.), yspan+yOffset-skew,reflect=True)
        totlenc += np.pi*rbend + yspan - skew + yOffset - 2.*rbend
    wiggleCell.add([enArc,exArc])
    
    #Wiggles in between
    for i in range(nwiggle-1):
        if i%2==1:
            wiggle = sLine((-xspan/2.+straightx/2.+xOffset+2.*rbend*(i+1)+rbend,
                yOffset),2.*yspan)
        else:
            wiggle = sLine((-xspan/2.+straightx/2.+xOffset+2.*rbend*(i+1)+rbend,
                yOffset),2.*yspan,reflect=True)
        wiggleCell.add([wiggle])
        totlenc += 2*(yspan-rbend)+np.pi*rbend

    print 'SelfCheck: total length is ', totlenc, ', wile it was supposed to be ', totlen

    #rotate and translate
    wiggleCellr = cad.core.CellReference(wiggleCell,rotation=rot)
    #translate for the skew
    #wiggleCellr.translate((0,100))
    wiggleCellr.translate(coords)
    
    return wiggleCellr, yspan

def CPWroute(coords, dx, dy, downBend = 0, bridges = True, rot=0, endrot=0):
    '''
    route a CPW from point (0,0) to (dx, dy)
    This function assumes dy to be positive. If you need negative dy, use rotate
    '''

    if dy<0:
        raise ValueError, 'dy must be positive, use rotate to get negative vertical distances'

    #init
    routeCell = cad.core.Cell('ROUTE')

    #default values
    center = defaults['centerConductor']
    gap = defaults['CPWGap']
    rbend = defaults['minimumRadius']

    #load airbridge Options



    print 'endrot is', endrot

    #calculate yspan of bend if dx < 2*rbend
    if abs(dx) < 2*rbend:
        phirad = np.arccos(1-abs(dx)/(rbend*2))
        yspan = 2*rbend*np.sin(phirad)

    #check in which direction to bend
    if dx >= 2*rbend and downBend == False:
        sCell = sLine((dx/2, rbend), dx, rbend=rbend, reflect=True, bridges=True, rot=90)
        cCell = CPW((dx, dy/2+rbend), dy-2*rbend, bridges=True, rot=90)
    elif dx <= -2*rbend and downBend == False:
        sCell = sLine((dx/2, rbend), abs(dx), rbend=rbend, bridges=True, rot=90)
        cCell = CPW((dx, dy/2+rbend), dy-2*rbend, bridges=True, rot=90)
    elif 0 <= dx <= 2*rbend and downBend == False:
        sCell, yspanc = doubleArc((dx/2, yspan/2), dx)
        cCell = CPW((dx, dy/2+yspan/2), dy-yspan, rot=90)
    elif -2*rbend < dx <= 0  and downBend == False:
        sCell, yspanc = doubleArc((dx/2, yspan/2), dx)
        cCell = CPW((dx, dy/2+yspan/2), dy-yspan, rot=90)
    routeCell.add([sCell, cCell])


    if downBend == True and abs(dx)< 4*rbend:
        raise ValueError, 'downBend cannot be used within such a small interval'

    if downBend == True and dx > 4*rbend:
        pass



    #Take care of the endrot
    if endrot == 'r':
        arcCell = CPWArc((dx+rbend, dy), 90, 90)
        routeCell.add(arcCell)
    elif endrot == 'l':
        arcCell = CPWArc((dx-rbend, dy), 0, 90)
        routeCell.add(arcCell)

    

    #rotate and translate
    routeCellr = cad.core.CellReference(routeCell, rotation = rot)
    routeCellr.translate(coords)

    return routeCellr




def resonator(coords, totlen, xspan, transmons=['lurd'], capacitors=['f3g'],  xoffset=0, yoffset=0, rotation=0):
    '''
    Construct a resonator including capacitors and transmon boxes
    '''
    #TODO NOT DONE!

    
def alignMarks(coords, rot=0):
    '''
    Build Alignment marks
    '''
    #use the smallcross with CellArray
    
    alCell = cad.core.Cell('ALIGN')
    al2Cell = cad.core.Cell('ALIGN')

    #Layer 0 : Crosses
    cross = simpleCross(20*um, 4*um, layer=0)
    crossArray = cad.core.CellArray(cross, 5, 5, (50*um, 50*um),origin=(-100*um,
        -100*um))
    alCell.add(crossArray)

    #layer 1 : weird box structure
    #Use border to build the keyhole
    box1 = border(12*um, 12*um, 76*um, layer=1)
    boxLine = cad.core.CellArray(box1, 5, 1, (50*um, 50*um),origin = (-100*um,0*um)) 
    boxCol = cad.core.CellArray(box1, 1, 5, (50*um, 50*um), origin = (00*um,
        -100*um)) 
    alCell.add([boxLine, boxCol])

    # layer 2 : use border again
    box2 = border(12*um, 12*um, 76*um, layer=2)
    #make a grid of four boxes
    boxSquare = cad.core.CellArray(box2, 2, 2, (50*um, 50*um), origin=(-100*um, -100*um))
    #Make into Cell to avoid making a CellArray of CellArrays, which messes up
    #export
    al2Cell.add(boxSquare)
    #make a grid of grids
    boxSqSq = cad.core.CellArray(al2Cell, 2, 2, (150*um, 150*um))

    #add to the cell
    alCell.add([boxSqSq])

    #translate and rotate
    alCellr = cad.core.CellReference(alCell, rotation=rot)
    alCellr.translate(coords)

    return alCellr



def TransmonCapA(coords, periods=2, width=250*um, height=150*um, sep=40*um,
        amp=30*um, gap = 10*um, rot=0):
    '''
    A transmon design to play with
    '''

    trCell = cad.core.Cell('TR')

    offset=20*um

    f = lambda x: amp*np.cos(2*np.pi*x/(width/periods))+sep/2.
    g = lambda x: amp*np.cos(2*np.pi*x/(width/periods))-sep/2.

    #part 1: upper transmon cap
    upper = [[x,f(x)] for x in np.arange(0,width, 1*um)]
    upper.extend([[width,height/2],[0,height/2],[0,f(0)]])
    upperShape = cad.core.Boundary(upper)
    trCell.add(upperShape)
    
    #part 2: lower transmon cap
    lower = [[x,g(x)] for x in np.arange(0,width, 1*um)]
    lower.extend([[width,-height/2],[0,-height/2],[0,g(0)]])
    lowerShape = cad.core.Boundary(lower)
    trCell.add(lowerShape)

    #rotate, translate
    trCellr = cad.core.CellReference(trCell, rotation=rot)
    trCellr.translate(coords)

    return trCellr

def TransmonCapBoxA(coords, periods=3, width=250*um, height=150*um, sep=40*um,
        amp=30*um, gap = 10*um, rot=0):
    '''
    A transmon design to play with
    '''

    trCell = cad.core.Cell('TR')

    offset=20*um
    gap = 3*um
    #extraspaces around the transmon for Left, Upper, Right, Down
    xS = [60*um, gap, gap, gap]

    f = lambda x: amp*np.sin(2*np.pi*x/(width/periods))+sep/2.
    g = lambda x: amp*np.sin(2*np.pi*x/(width/periods))-sep/2.

    #part 1: upper transmon cap
    upper = [[-offset, height/2], [-width/2, height/2]]
    upperp2 = [[x,f(x)] for x in np.arange(-width/2,width/2, 1*um)]
    upper.extend(upperp2)
    upper.extend([[width/2,height/2],[-offset,height/2]])
    #upperShape = cad.core.Boundary(upper)
    #trCell.add(upperShape)
    
    #part 2: outerBox, first half
    boxpoints1 = [[-offset, height/2.+xS[1]], [width/2+xS[2], height/2+xS[1]],
            [width/2+xS[2], -height/2-xS[3]],[-offset,-height/2-xS[3]]] 

    lower = [[-offset, -height/2],[width/2,-height/2]]
    lowerp2 = [[x,g(x)] for x in np.arange(width/2,-width/2,-1*um)]
    lower.extend(lowerp2)
    lower.extend([[-width/2,-height/2],[-offset, -height/2]])

    boxPoints2 = [[-offset, -height/2-xS[3]], [-width/2-xS[0], -height/2-xS[3]],
        [-width/2-xS[0], height/2 + xS[1]], [-offset, height/2 + xS[1]]]

    allPoints = upper + boxpoints1 + lower + boxPoints2

    allShape = cad.core.Boundary(allPoints)
    trCell.add(allShape)

    #rotate, translate
    trCellr = cad.core.CellReference(trCell, rotation=rot)
    trCellr.translate(coords)

    return trCellr




def crossArray(coords, smallSize = (6*um, 2*um), bigSize = (15*um, 5*um), bigDis =
        300*um, smallDis = 150*um):
    '''
    Array of simpleCross structures
    '''

    crossCell = cad.core.Cell('CROSS')
    
    small = simpleCross(smallSize[0], smallSize[1])
    big = simpleCross(bigSize[0], bigSize[1])

    smallArray = cad.core.CellArray(small, 2, 2, (smallDis, smallDis), 
            origin = (-smallDis/2, -smallDis/2))
    bigArray = cad.core.CellArray(big, 2, 2, (bigDis, bigDis),
            origin = (-bigDis/2, -bigDis/2))

    crossCell.add([smallArray, bigArray])
    crossCellr = cad.core.CellReference(crossCell, origin = coords)

    return crossCellr

def fourPoint(coords, ylen=419*um, xlen=438*um, gapSize=150*um, center = 10*um,
        gap = 19*um, rot=0):
    '''
    fourPointMeasure pads for measuring squid resistance

    This function is not intelligent, and was designed only for 
    '''
    
    fpCell = cad.core.Cell('fourPoint')

    center = defaults['centerConductor']
    gap = defaults['CPWGap']

    #four launchers
    launch1 = launcher((-xlen/2, ylen/2+500*um), rot=-90)
    launch2 = launcher((-xlen/2, -ylen/2-500*um), rot=90)
    launch3 = launcher((xlen/2, ylen/2+500*um), rot= -90)
    launch4 = launcher((xlen/2, -ylen/2-500*um), rot= 90)
    fpCell.add([launch1, launch2, launch3, launch4])
    
    #4 rectangles to close the launchers
    r1 = cad.shapes.Rectangle((-xlen/2 -.95*150*um, ylen/2+500*um),
            (-xlen/2 + .95*150*um, ylen/2+550*um))
    r2 = cad.shapes.Rectangle((-xlen/2 -.95*150*um, -ylen/2-500*um),
            (-xlen/2 + .95*150*um, -ylen/2-550*um))
    r3 = cad.shapes.Rectangle((xlen/2 - .95*150*um, -ylen/2-500*um),
            (xlen/2 + .95*150*um, -ylen/2-550*um))
    r4 = cad.shapes.Rectangle((xlen/2 -.95*150*um, ylen/2+500*um),
            (xlen/2 + .95*150*um, ylen/2+550*um))
    fpCell.add([r1, r2, r3, r4])

    #CPWs
    c1 = CPW((-xlen/2, ylen/4+center/2),ylen/2-center/2, rot=90)
    c2 = CPW((-xlen/2, -ylen/4-center/2),ylen/2-center/2, rot=90)
    c3 = CPW((xlen/2, ylen/4+center/2),ylen/2-center/2, rot=90)
    c4 = CPW((xlen/2, -ylen/4-center/2),ylen/2-center/2, rot=90)
    fpCell.add([c1,c2,c3,c4])

    #two small rectangles to close the CPWs
    r5 = cad.shapes.Rectangle((-xlen/2-gap/2,-gap/2),(-xlen/2-center/2, gap/2))
    r6 = cad.shapes.Rectangle((xlen/2+gap/2,-gap/2),(xlen/2+center/2, gap/2))
    fpCell.add([r5, r6])
    
    
    #gapCap
    gap = gapCoupler((0,0),gapSize,leng=xlen-center,rot=0)
    fpCell.add(gap)


    #crossArray
    crosses = crossArray((0,0))
    fpCell.add(crosses)

    #rotate and translate
    fpCellr = cad.core.CellReference(fpCell, rotation=rot)
    fpCellr.translate(coords)


    return fpCellr

    
def lumpedParamp(coords, islandX=300*um, finger1Thick=100*um, finger2Thick=50*um, cap1Len=100*um,
        cap2Len=200*um, nFinger1=14, nFinger2=7, rot=0):
    '''
    Since this is a rather irregular design, the code will be ugly

    Draws a lumped-element Paramp with align crosses in a symmetric design

    islandX = island length
    capLen = length of the capacitor
    fingerThick = width of the finger capacitor

    '''
 
    #make a cell
    LPCell = cad.core.Cell('LP')

    thick1 = finger1Thick/(2*nFinger1-1)
    thick2 = finger2Thick/(2*nFinger2-1)
    finger1Len =  cap1Len - 2* thick1
    finger2Len = cap2Len - 2* thick2

    #island properties
    dX = islandX

    #add fingerCaps
    F1 = fingerCap((-dX/2-cap1Len/2,0), nFinger1, finger1Len, thick1, thick1, thick1)
    F2 = fingerCap((0,finger1Thick/2+cap2Len/2), nFinger2, finger2Len, thick2,
            thick2, thick2, rot=90)
    F3 = fingerCap((0,-finger1Thick/2 - cap2Len/2), nFinger2, finger2Len,
            thick2, thick2, thick2, rot=-90)
    LPCell.add([F1,F2,F3])

    #Squares
    r1 = cad.shapes.Rectangle((-dX/2-cap1Len,finger1Thick/2),(-finger2Thick/2,
        finger1Thick/2+cap2Len))
    r2 = cad.shapes.Rectangle((-dX/2-cap1Len,-finger1Thick/2),(-finger2Thick/2,
        -finger1Thick/2-cap2Len))
    r3 = cad.shapes.Rectangle((finger2Thick/2,finger1Thick/2),
            (dX/2, finger1Thick/2+cap2Len))
    r4 = cad.shapes.Rectangle((finger2Thick/2, - finger1Thick/2),
            (dX/2, - finger1Thick/2-cap2Len))
    LPCell.add([r1,r2,r3,r4])

    #AlignBox
    alCell = cad.core.Cell('AL')
    alCell2 = cad.core.Cell('AL2')
    alDist = 150*um
    boxSize = 200*um
    crossSize = 10*um
    crossThick = 4*um
    d = (boxSize-alDist)/2

    bPoints1 = [[-boxSize/2, boxSize/2],
            [-alDist/2, boxSize/2]]

    cPoints = [[-alDist/2, alDist/2+crossSize/2],
            [-alDist/2-crossThick/2, alDist/2+crossSize/2],
            [-alDist/2-crossThick/2, alDist/2+crossThick/2],
            [-alDist/2-crossSize/2, alDist/2+crossThick/2],
            [-alDist/2-crossSize/2, alDist/2-crossThick/2],
            [-alDist/2-crossThick/2, alDist/2-crossThick/2],
            [-alDist/2-crossThick/2, alDist/2-crossSize/2],
            [-alDist/2+crossThick/2, alDist/2-crossSize/2],
            [-alDist/2+crossThick/2, alDist/2-crossThick/2],
            [-alDist/2+crossSize/2, alDist/2-crossThick/2],
            [-alDist/2+crossSize/2, alDist/2+crossThick/2],
            [-alDist/2+crossThick/2, alDist/2+crossThick/2],
            [-alDist/2+crossThick/2, alDist/2+crossSize/2],
            [-alDist/2, alDist/2+crossSize/2]]

    bPoints2 = [[-alDist/2, boxSize/2],
            [0, boxSize/2],
            [0, 0],
            [-boxSize/2, 0],
            [-boxSize/2, boxSize/2]]

    alPoints = bPoints1+cPoints+bPoints2

    bdy = cad.core.Boundary(alPoints)
    alCell.add(bdy)
    alCellr1 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0))
    alCellr2 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0), rotation=-90)
    alCellr3 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0), rotation=-180)
    alCellr4 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0), rotation=-270)
    alCell2.add([alCellr1, alCellr2, alCellr3, alCellr4])

    #add to topCell
    LPCell.add(alCell2)

    #add rectangles
    r5 = cad.shapes.Rectangle((dX/2, boxSize/2),
            (dX/2+boxSize, cap2Len+finger1Thick/2))
    r6 = cad.shapes.Rectangle((dX/2, -boxSize/2),
            (dX/2+boxSize, -cap2Len-finger1Thick/2))
    LPCell.add([r5,r6])
    
    #rotate and translate
    LPCellr = cad.core.CellReference(LPCell, rotation=rot)
    LPCellr.translate(coords)

    return LPCellr

