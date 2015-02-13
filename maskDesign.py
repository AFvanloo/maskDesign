import gdsCAD as cad
import matplotlib as mpl
import numpy as np
import defaultParms as dp

defaults = dp.dPars()
dLists = dp.dLists()

#Separate file for sizes etc?

#TODO
#Qudev-style alignment marker:
#ChargeLines/FluxLines
#Easy way to add airbridges

print 'loading maskDesign'

#inner conductor
# ic-to-ground distance

um = 1e3
mm = 1e6
inch = 25.4*mm
a1, b1 = defaults['centerConductor'], defaults['CPWGap'] 

cad.core.default_layer = 0


#Common abbreviations in the Mathematica file:
#a1 = half center width of CPW
#ar = half center width of launcher
#abrl = a/b ratio (b being outside of gap)
#abrr = a/b ratio of launcher
#
##in ChargeLine
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

def borderA(xlen,ylen,gap, alignPos, layer=0):
    '''
    Makes a border for a chip, with a width of gap/2,
    Inlcudes Alignment Markers
    '''

    print 'generating borders'

    boxCell = cad.core.Cell('BORDER')
    boundbox = border(xlen,ylen,gap, layer=layer)
    boxCell.add(boundbox)

    #Alignment marks
    dis = defaults['alignDistance']   #distance from markers to edge

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
        boxCell.add(Align3)

    return boxCell 

def cornerL(coords, leng=500*um, thick=100*um, rot=0):
    '''
    L-shape to put into the corner of the chip for aligning
    '''

    print 'adding alignment L'

    LCell = cad.core.Cell('L')
    hl = leng/2

    #draw the shape
    lShape = [[-hl,hl],[hl,hl],[hl,-hl],[hl-thick,-hl],
            [hl-thick, hl-thick],[-hl,hl-thick],[-hl,hl]]
    lbound = cad.core.Boundary(lShape)
    LCell.add(lbound)

    LCellr = cad.core.CellReference(LCell,rotation=rot)
    LCellr.translate(coords)

    return LCellr


def CPW(coords,leng, center=10*um,gap=19*um, closeA=False, closeB=False,
        bridges=False, bridgeDistance= defaults['ABdistance'], 
        bridgeStart=defaults[ 'ABstart'], bridgeEnd=defaults[ 'ABend'], vias=False, viaDiam = None,
        interviaDistance=None, viaHorizDistance=None, rot=0):
    '''
    A straight piece of co-planar waveguide
    center = the width of the center conductor
    gap = the width of the cut in the ground plane in which the center conductor is placed
    rot = rotation in degrees

    if via is set to true, the via distance will be slightly changed from the default value in order to 
    ensure that vias are placed at close to the ends

    returns a cell, and if vias=True, a list of via locations
    '''
    #defaults for AB here until I find out how to make it properly
        
    if bridgeDistance == None: bridgeDistance = defaults['ABdistance']
    if bridgeStart == None: bridgeStart =defaults[ 'ABstart']
    if bridgeEnd == None: bridgeEnd = defaults[ 'ABend']
    
    #via properties
    if viaDiam == None: viaDiam = defaults['viaDiameter']
    if interviaDistance == None: interviaDistance = defaults['interviaDistance']
    if viaHorizDistance == None: viaHorizDistance = defaults['viaHorizDistance']
    
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
        r1=cad.shapes.Rectangle((-leng/2+(gap-center)/2, -center/2),
                (-leng/2, center/2))
        cpwCell.add(r1)
    if closeB:
        r2=cad.shapes.Rectangle((leng/2, -center/2),
                (leng/2-(gap-center)/2, center/2))
        cpwCell.add(r2)


    #add to the cell
    cpwCell.add([gapup,gapdown])
     #airBridges
    if bridges:

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

    if not vias:
        cpwCellr = cad.core.CellReference(cpwCell,rotation=rot)
        cpwCellr.translate(coords)
        return cpwCellr

    else:
        #Cell for vias
        pb1 = defaults['PCBgap']
        viaCell = cad.core.Cell('VIA')
        xloc = interviaDistance/2.
        y = pb1/2+viaHorizDistance
        viaLocs = []

        #generate locations:
        nums = np.round(leng/(2*xloc))
        dis = (leng-2*xloc)/(nums-1)
        xlocs = np.arange(-leng/2+xloc,leng/2-xloc+1 ,dis)
        for x in xlocs:
            viaLocs.append([x,y])
            v1 = Via(viaLocs[-1], viaDiam)
            viaLocs.append([x,-y])
            v2 = Via(viaLocs[-1], viaDiam)
            cpwCell.add([v1, v2])

        #rotate and translate vias
        viaLocsE = transRotVias(viaLocs, trans=coords, rot=rot)

        #rotate and translate Cell
        cpwCellr = cad.core.CellReference(cpwCell, rotation=rot)
        cpwCellr.translate(coords)

        return cpwCellr, viaLocsE



def CPWArc(coords,initangle=270,degrees=90,
        radius=100.*um,center=10.*um,gap=19.*um, vias=False, rot=0.):
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
    if not vias:
        arcCellr = cad.core.CellReference(arcCell,rotation=rot)
        arcCellr.translate(coords)
        return arcCellr

    else:
        #cal len of arc
        viaCell, posList  = arcVias(initangle, degrees, radius, center, gap)
        arcCell.add(viaCell)

        #rotate, translate
        posListR = transRotVias(posList, trans=coords, rot=rot)
        arcCellr = cad.core.CellReference(arcCell,rotation=rot)
        arcCellr.translate(coords)
        
        return arcCellr, posListR


def circBoundary(coords, radius, init_angle=0, final_angle=360, nopoints=199):
    '''
    make a boundary of circular shape
    Note that 199 is the maximum number of points permissable by GDS
    Also note that when defining boundaries, the order matters: make sure you
    draw your circle in the right direction
    '''
    dphi = float(final_angle-init_angle)/(nopoints-1)
    angles = np.arange(init_angle, final_angle+dphi, dphi)
    x,y = coords

    return [[x + radius*np.cos(rad(phi)), y + radius*np.sin(rad(phi))] for phi in angles]


def taper(coords,taperlen, startOuter, endOuter,
        startInner,endInner,rot=0, flip = False, noground = False):
    '''
    General purpose taper drawer, for use in example couplers and launchers
    tapers from any start to any end within length taperlen
    '''
    taperCell = cad.core.Cell('TAPER')
    flipit = -1 if flip else 1

    #draw it!
    if noground:
        pointsup = [(flipit*taperlen/2.,startInner/2.),
                (flipit*taperlen/2.,endInner/2.),(flipit*-taperlen/2.,startInner/2.)]
        pointsdown = [(flipit*taperlen/2.,-startInner/2.),
                (flipit*taperlen/2.,-endInner/2.),(flipit*-taperlen/2.,-startInner/2.)]
    else:
        pointsup = [(flipit*-taperlen/2.,startOuter/2.),(flipit*taperlen/2.,endOuter/2.),
                (flipit*taperlen/2.,endInner/2.),(flipit*-taperlen/2.,startInner/2.)]

        pointsdown = [(flipit*-taperlen/2.,-startOuter/2.),(flipit*taperlen/2.,-endOuter/2.),
                (flipit*taperlen/2.,-endInner/2.),(flipit*-taperlen/2.,-startInner/2.)]


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
        ym = (-1)**i
        if almarks[i]==2:
            transmonCell.add(bCross,origin=(bigDis/2, ym*bigDis/2))
            transmonCell.add(bCross,origin=(-bigDis/2, ym*bigDis/2))
            transmonCell.add(sCross,origin=(smallDis/2, ym*smallDis/2))
            transmonCell.add(sCross,origin=(-smallDis/2, ym*smallDis/2))
        elif almarks[i]==1:
            transmonCell.add(bCross,origin=(0,ym*bigDis/2))
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


def chargeLineEnd(coords,linelen,gaplen,center=10*um,gap=19.*um,rot=0):
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
                (taplen, -fluxgap/2),
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


def chipText(coords, text, fontsize=100*um, font='romand', layer=0,rot=0):
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

def chipSides(x,y):
    '''
    Makes the left and right side of the chip, with a maskLabel space on the right bottom,
    a chip label space on the left top, and L-shaped marks for alignment elsewhere
    '''

    sideCell = cad.core.Cell('SIDES')

    white = defaults['labelSpace']
    lthick = defaults['LAlignThick']

    r1 = cad.shapes.Rectangle([-x/2, -y/2+white],[-x/2+white, y/2-white])
    r2 = cad.shapes.Rectangle([x/2-white, -y/2+white],[x/2, y/2-white])
    r3 = cad.shapes.Rectangle([-x/2+lthick, -y/2+lthick], [-x/2+white, -y/2+white])
    r4 = cad.shapes.Rectangle([x/2-lthick, y/2-lthick], [x/2-white, y/2-white])
    sideCell.add([r1,r2,r3,r4])

    return sideCell


#=================COMBINED FUNCTIONS=============================

def doubleArc(coords, dy, rbend = 100*um, center=a1, gap=b1, vias=False, rot=0):

    dACell = cad.core.Cell('DOUBLEARC')

    #Calculate angle
    phirad = np.arccos(1-abs(dy)/(rbend*2))
    phi = phirad*360/2/np.pi    #convert to degrees

    #start and end coords:
    startc = (-rbend*np.sin(phirad), rbend-abs(dy)/2)
    endc = (rbend*np.sin(phirad), -rbend+abs(dy)/2)
    xspan = endc[0]*2

    #draw Arcs
    if dy>=0:
        arc1Cell = CPWArc(startc, 270, phi, rbend, center, gap, vias=vias)
        arc2Cell = CPWArc(endc, 90, phi, rbend, center, gap, vias=vias)
    else:
        arc1Cell = CPWArc((startc[0], -startc[1]), 90, -phi, rbend, center, gap, vias=vias)
        arc2Cell = CPWArc((endc[0], -endc[1]), 270, -phi, rbend, center, gap, vias=vias)

    if vias:
        arc1Cell, pos1 = arc1Cell
        print 'pos1 is ', pos1
        arc2Cell, pos2 = arc2Cell
        print 'pos2 is ', pos2
        viaLocs = pos1
        viaLocs.extend(pos2)
        print 'viaLocs is ', viaLocs
        viaLocs = transRotVias(viaLocs, trans=coords, rot=rot)

    dACell.add([arc1Cell, arc2Cell])
    
    #translate, rotate, reflect
    dACellr = cad.core.CellReference(dACell, rotation=rot)
    dACellr.translate(coords)
    
    if vias:
        return dACellr, xspan, viaLocs
    else:
        return dACellr, xspan


def sLine(coords,yspan,rbend=100.*um,enter=True,exit=True,reflect=False,
        bridges=False, center=a1, gap=b1, rot=0):
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
            enArc = CPWArc((-rbend,yspan/2.-rbend), initangle = 0., radius=rbend, center=center, gap=gap)
        else:
            enArc = CPWArc((-rbend,-yspan/2.+rbend),radius=rbend, center=center, gap=gap)
        vstart += rbend/2.
        vlen -= rbend
        sLineCell.add(enArc)

    if exit:
        if reflect:
            exArc = CPWArc((rbend,-yspan/2.+rbend),initangle =180., radius=rbend, center=center, gap=gap)
        else:
            exArc = CPWArc((rbend,yspan/2.-rbend),initangle =90., radius=rbend, center=center, gap=gap)
        vlen -= rbend
        vstart -= rbend/2.
        sLineCell.add(exArc)

    
    #straight piece
    if reflect:
        vPiece = CPW((0,vstart),vlen, bridges = bridges, center=center, gap=gap, rot=90.)
    else:
        vPiece = CPW((0,vstart),vlen, bridges = bridges, center=center, gap=gap, rot=90.)
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
        center=10.*um,gap=19.*um,yOffset=0.,xOffset=0., skew=0, closeA = False,
        closeB= False, rot=0.):
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
    leftLine = CPW((-xspan/2.+straightx/4+xOffset/2.,-skew),straightx/2.+xOffset, closeA=closeA)
    rightLine = CPW((xspan/2.-straightx/4.+xOffset/2.,skew),straightx/2.-xOffset, closeB=closeB)
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

def CPWroute(coords, dx, dy, bridges = True, rot=0, endrot=0, PCB=False):
    '''
    route a CPW from point (0,0) to (dx, dy)
    This function assumes dy to be positive. If you need negative dy, use rotate
    '''

    if dy<0:
        raise ValueError, 'dy must be positive, use rotate to get negative vertical distances'

    #init
    routeCell = cad.core.Cell('ROUTE')

    #default values
    if PCB:
        rbend = min(dx, dy)/2
        gap = defaults['PCBgap']
        center = defaults['PCBcenter']
    else:
        gap = defaults['CPWGap']
        center = defaults['centerConductor']
        rbend = defaults['minimumRadius']

    #calculate yspan of bend if dx < 2*rbend
    if abs(dx) < 2*rbend:
        phirad = np.arccos(1-abs(dx)/(rbend*2))
        yspan = 2*rbend*np.sin(phirad)

    #check in which direction to bend
    if dx >= 2*rbend: 
        sCell = sLine((dx/2, rbend), dx, rbend=rbend, reflect=True, bridges=bridges, rot=90)
        cCell = CPW((dx, dy/2+rbend), dy-2*rbend, bridges=bridges, rot=90)
    elif dx <= -2*rbend and dx!=0:
        sCell = sLine((dx/2, rbend), abs(dx), rbend=rbend, bridges=bridges, rot=90)
        cCell = CPW((dx, dy/2+rbend), dy-2*rbend, bridges=bridges, rot=90)
    elif 0 < dx <= 2*rbend:
        sCell, yspanc = doubleArc((dx/2, yspan/2), -dx, rot=90)
        cCell = CPW((dx, dy/2+yspan/2), dy-yspan, bridges=bridges, rot=90)
    elif -2*rbend < dx < 0:
        sCell, yspanc = doubleArc((dx/2, yspan/2), -dx, rot=90)
        cCell = CPW((dx, dy/2+yspan/2), dy-yspan, bridges=bridges, rot=90)
    elif dx == 0:
        cCell = CPW((dx, dy/2+yspan/2), dy-yspan, bridges=bridges, rot=90)
    if dx==0:
        routeCell.add([cCell])
    else:
        routeCell.add([sCell, cCell])

    #Take care of the endrot
    if endrot == 'r':
        arcCell = CPWArc((dx+rbend, dy), 90, 90, gap=gap, center=center)
        routeCell.add(arcCell)
    elif endrot == 'l':
        arcCell = CPWArc((dx-rbend, dy), 0, 90, gap=gap, center=center)
        routeCell.add(arcCell)

    #rotate and translate
    routeCellr = cad.core.CellReference(routeCell, rotation = rot)
    routeCellr.translate(coords[:2])

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

def twoPoint(coords, ylen=419*um, xlen=438*um, gapSize=150*um, center = 10*um,
        gap = 19*um, rot=0):
    '''
    two point measurement pads for measuring squid resistance
	'''
    
    tpCell = cad.core.Cell('twoPoint')

    #two launchers
    launch1 = launcher((0, ylen/2+500*um), rot=-90)
    launch2 = launcher((0, -ylen/2-500*um), rot=90)
    tpCell.add([launch1, launch2])
    
    #4 rectangles to close the launchers
    r1 = cad.shapes.Rectangle((-.95*150*um, ylen/2+500*um),
            ( .95*150*um, ylen/2+550*um))
    r2 = cad.shapes.Rectangle((-.95*150*um, -ylen/2-500*um),
            ( .95*150*um, -ylen/2-550*um))
    tpCell.add([r1, r2])

    #CPWs
    c1 = CPW((0, ylen/4+center/2),ylen/2-center/2, rot=90)
    tpCell.add(c1)
   
    #gapCap
    gap = gapCoupler((0,0),gapSize,leng=xlen-center,rot=90)
    tpCell.add(gap)

    #crossArray
    crosses = crossArray((0,0))
    tpCell.add(crosses)

    #rotate and translate
    tpCellr = cad.core.CellReference(tpCell, rotation=rot)
    tpCellr.translate(coords)

    return tpCellr

def smallPad(coords, pad = 150.*um, ins = 50.*um, gapSize=150.*um, dis=400.*um, rot=0):
    center = defaults['centerConductor']
    gap = defaults['CPWGap']
        
    padCell = cad.core.Cell('PAD')	
	
    #draw boundary of small pad
    points = [(-center/2,dis/2),(-center/2-pad/2-ins,dis/2), (-center/2-pad/2-ins,dis/2+2*ins+pad),
	(+center/2+pad/2+ins,dis/2+2*ins+pad),(+center/2+pad/2+ins,dis/2),(center/2,dis/2),
	(center/2,dis/2+ins),(pad/2,dis/2+ins), (pad/2,dis/2+ins+pad),(-pad/2,dis/2+ins+pad),
	(-pad/2,dis/2+ins),(-center/2,dis/2+ins)]
    pre = cad.core.Boundary(points)
    padCell.add(pre)

    #rotate and translate
    padCellr = cad.core.CellReference(padCell, rotation=rot)
    padCellr.translate(coords)
	
    return padCellr
	
def twoPointSmall(coords, pad = 150.*um, ins = 50.*um, dis=400.*um, gapSize=150.*um, rot=0):
    '''
    two point measurement square pads for measuring squid resistance
    '''
    center = defaults['centerConductor']
    gap = defaults['CPWGap']
        
    tpCell = cad.core.Cell('twoPoint')
    
   # add pads
    pre1 = smallPad((0,0),pad = pad, ins = ins, dis=dis, gapSize=gapSize, rot=rot)
    pre2 = smallPad((0,+dis/2-(pad+ins)),pad = pad, ins = ins, dis=dis, gapSize=gapSize, rot=rot+180)
    tpCell.add([pre1,pre2])

    #add cpw of len dis
    cpw = CPW((0,0),dis, rot=90)
    tpCell.add(cpw)

    #gapCap
    gap = gapCoupler((0,0),gapSize,rot=90)
    tpCell.add(gap)
   
    #rotate and translate
    tpCellr = cad.core.CellReference(tpCell, rotation=rot)
    tpCellr.translate(coords)
	   
    return tpCellr
	
def twoPointIslandsInSquare(coords, pad = 50.*um,  ins = 50.*um, almarks = [2,2], rot=0):
    ''',
    two point measurement square pads for measuring squid resistance, other version
    '''
    center = defaults['centerConductor']
    gap = defaults['CPWGap']
        
    tpCell = cad.core.Cell('twoPoint')
	
   # add pads
    pad1 = cad.shapes.Box((-pad/2-ins,0),(pad/2+ins,2*ins+pad),ins,layer=0)
    pad2 = cad.shapes.Box((-pad/2-ins,-2*ins-pad),(pad/2+ins,0),ins,layer=0)
    tpCell.add([pad1,pad2])

    #Alignment marks (from transmonBoxAlign)
    bCross = simpleCross(30*um,10*um)
    sCross = simpleCross(12*um, 2*um)
    bigDis = 300*um
    smallDis = 250*um

    for i in range(len(almarks)):
        ym = (-1)**i
        if almarks[i]==2:
            tpCell.add(bCross,origin=(bigDis/2, ym*bigDis/2))
            tpCell.add(bCross,origin=(-bigDis/2, ym*bigDis/2))
            tpCell.add(sCross,origin=(smallDis/2, ym*smallDis/2))
            tpCell.add(sCross,origin=(-smallDis/2, ym*smallDis/2))
        elif almarks[i]==1:
            tpCell.add(bCross,origin=(0,ym*bigDis/2))
            tpCell.add(sCross,origin=(0,ym*smallDis/2))
        elif almarks[i]==0:
            continue
            
        elif almarks[i]>2 or almarks[i] < 0:
            print 'Use almarks of [2,2] or less'

    #rotate and translate
    tpCellr = cad.core.CellReference(tpCell, rotation=rot)
    tpCellr.translate(coords)
	
    return tpCellr
    
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
            thick2, thick2, thick2, rot=270)
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
    alCell3 = cad.core.Cell('AL3')
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
    alCellr1 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0),rotation=0)
    alCellr2 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0), rotation=270)
    alCellr3 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0), rotation=180)
    alCellr4 = cad.core.CellReference(alCell, origin=(dX/2+boxSize/2, 0),
            rotation=-270)
    alCell2.add([alCellr1, alCellr2, alCellr3, alCellr4])

    #add to topCell
    LPCell.add(alCell2)

    #add rectangles
    r5 = cad.shapes.Rectangle((dX/2, boxSize/2),
            (dX/2+boxSize, cap2Len+finger1Thick/2))
    r6 = cad.shapes.Rectangle((dX/2, -boxSize/2),
            (dX/2+boxSize, -cap2Len-finger1Thick/2))
    LPCell.add([r5,r6])
    
    #flatten, rotate and translate
    LPCellr = cad.core.CellReference(LPCell, rotation=rot)
    LPCellr.translate(coords)

    return LPCellr


def antenna(coords,fingerThick=10*um, ySize=1*mm, fingerDis = 50*um, nFingers=25,
        xtraLeft = 200*um, xtraRight=200*um, xtraTop=200*um, xtraBottom=200*um, rot=0):

    #if nFingers%2 == 0:
    #    print 'currently, nFingers should be odd, adding one'
    #    nFingers += 1

    Acell = cad.core.Cell('ANTENNA')

    #inside radius, outside radius
    iR = (fingerDis - fingerThick)/2
    oR = (fingerDis + fingerThick)/2
    ystraight = ySize/2 - oR

    #create lower half
    lowerx = np.arange(-nFingers+1, nFingers+1,2)
    lowerx = fingerDis*lowerx
    for x in lowerx[1:-1]:
        cut = fingerInside([x,0],iR,oR,fingerDis, ystraight, sides = 'rl')
        Acell.add(cut)
    cutl = fingerInside([lowerx[0],0],iR,oR,fingerDis, ystraight, sides = 'r')
    cutr = fingerInside([lowerx[-1],0],iR,oR,fingerDis, ystraight, sides = 'l')
    Acell.add([cutl,cutr])


    #upper half
    upperx = np.arange(-nFingers+2, nFingers-1,2)
    upperx = upperx*fingerDis #+ fingerDis
    for x in upperx:
        cut = fingerInside([x,0],iR,oR,fingerDis, ystraight, sides = 'lr',
                rot=180)
        Acell.add(cut)


    #Upper Boundary
    bound = [[-(nFingers-.5)*fingerDis-fingerThick/2-xtraLeft, -ySize/2-xtraBottom],
            [-(nFingers-.5)*fingerDis-fingerThick/2, -ySize/2-xtraBottom],
            [-(nFingers-.5)*fingerDis-fingerThick/2, ystraight]]
    bound += circBoundary([-(nFingers-1)*fingerDis,ystraight],oR, init_angle=180,
            final_angle=90)
    bound += [[-(nFingers-.5)*fingerDis-fingerThick/2+oR,ySize/2],
            [(nFingers-.5)*fingerDis+fingerThick/2-oR,ySize/2]]
    bound += circBoundary([(nFingers-1)*fingerDis,ystraight],oR, init_angle=90,
            final_angle=0)
    bound += [[(nFingers-.5)*fingerDis+fingerThick/2, -ySize/2-xtraBottom],
              [(nFingers-.5)*fingerDis+fingerThick/2+xtraRight, -ySize/2-xtraBottom],
              [(nFingers-.5)*fingerDis+fingerThick/2+xtraRight, ySize/2+xtraTop],
              [-(nFingers-.5)*fingerDis-fingerThick/2-xtraLeft, ySize/2+xtraTop],
              [-(nFingers-.5)*fingerDis-fingerThick/2-xtraLeft, -ySize/2-xtraBottom]]
    bdy = cad.core.Boundary(bound)
    Acell.add(bdy)
    
    #lower boundary
    r = cad.shapes.Rectangle((-(nFingers-.5)*fingerDis+fingerThick/2,-ySize/2),
            ((nFingers-.5)*fingerDis-fingerThick/2,-ySize/2-xtraBottom))
    Acell.add(r)

    #flatten, rotate, translate
    Acellr = cad.core.CellReference(Acell, rotation=rot)
    Acellr.translate(coords)

    return Acellr
    
def fingerInside(coords, iR, oR, fingerDis, ystraight, rot=0, sides='lr'):
    '''
    sides = ['l','r'] determines whether or not to draw a quarter circle on the
    left of right side
    '''

    FICell  = cad.core.Cell('FI')

    #lower left
    thick = oR-iR
    points = []
    if sides.count('l')>=1:
        points+= circBoundary([-fingerDis,-ystraight], oR, init_angle=270,
                final_angle=360)
        points += [[-iR,-ystraight],[-iR, ystraight]]
    else:
        points += [[-iR, -ystraight-oR],[-iR, ystraight]]
    points += circBoundary([0,ystraight], iR, final_angle=180)
    if sides.count('r')>=1:
        points += [[iR,ystraight],[iR, -ystraight]]
        points += circBoundary([fingerDis, -ystraight], oR, init_angle=180,
                final_angle=270)
    else:
        points += [[iR, ystraight],[iR, -ystraight-oR]]
    bd = cad.core.Boundary(points)
    FICell.add(bd)

    #flatten, rotate, translate
    FICellr = cad.core.CellReference(FICell, rotation=rot)
    FICellr.translate(coords)

    return FICellr


def thinTenna(coords, totLen, thinLen, thin=2*um, tapLen=100*um, preLen=0,
        a1=None, b1=None, rot=0):
    '''
    makes a thin antenna
    '''

    if a1 == None:
        a1 = defaults['centerConductor']
    if b1 == None:
        b1 = defaults['CPWGap']
    abr = float(b1)/a1

    ttCell = cad.core.Cell('TTENNA')

    cp1 = CPW([-totLen/2+preLen/2,0],preLen, center=a1, gap=b1)
    cp2 = CPW([totLen/2-preLen/2,0], preLen,center=a1, gap=b1)

    tap1 = taper([-totLen/2+preLen+tapLen/2,0],tapLen,b1,abr*thin,a1,thin)
    tap2 = taper([totLen/2-preLen-tapLen/2,0],tapLen,b1,abr*thin,a1,thin, flip=True)
    
    thinLen = totLen - 2*tapLen - 2*preLen
    innerCPW = CPW([0,0], thinLen, center=thin, gap=abr*thin)
    ttCell.add([cp1, cp2, tap1, tap2, innerCPW])

    #flatten, rotate, translate
    ttCellr = cad.core.CellReference(ttCell, rotation=rot)
    ttCellr.translate(coords)

    return ttCellr



#
#def circBoundary(coords, radius, init_angle=0, final_angle=180, nopoints=199):
#    '''
#    make a boundary of circular shape
#
#    Note that 199 is the maximum number of points permissable by GDS
#
#    Also note that when defining boundaries, the order matters: make sure you
#    draw your circle in the right direction
#    '''
#    dphi = float(final_angle-init_angle)/(nopoints-1)
#    angles = np.arange(init_angle, final_angle+dphi, dphi)
#    x,y = coords
#
#    points = []
#    for phi in angles:
#        points.append([x + radius*np.cos(rad(phi)), y + radius*np.sin(rad(phi))])
#
#    return points
#

def wireNoGround(coords, thick, ySize, xtraLeft=.5*mm, xtraRight=.5*mm, launcherX=300*um, launcherY=500*um, rot=0):
    '''
    Make a wire while getting rid of the surrounding groundplane
    '''

    wgCell = cad.core.Cell('NOGROUNDWIRE')
    
    left = [[-launcherX/2, -ySize/2],[-xtraLeft, -ySize/2],[-xtraLeft, ySize/2],
            [-launcherX/2, ySize/2], [-thick/2, ySize/2-launcherY],
            [-thick/2, -ySize/2 + launcherY], [-launcherX/2, -ySize/2]]
    leftb = cad.core.Boundary(left)
    
    right = [[launcherX/2, -ySize/2],[xtraRight, -ySize/2],[xtraRight, ySize/2],
            [launcherX/2, ySize/2], [thick/2, ySize/2-launcherY],
            [thick/2, -ySize/2 + launcherY], [launcherX/2, -ySize/2]]
    rightb = cad.core.Boundary(right)

    wgCell.add([leftb, rightb])

    #flatten, rotate, translate
    wgCellr = cad.core.CellReference(wgCell, rotation=rot)
    wgCellr.translate(coords)

    return wgCellr

#===========================================================================
#---------------------------PositivePhotoresist-----------------------------
#===========================================================================

def DCwire(coords, ySize, thick, launcherY=500*um, launcherX=300*um, rot=0):
    '''
    Make a wire at coords of width 'thick' with triangular contact of dimensions
    launcherY, launcherX

    By default, this structure is vertical
    '''

    DCCell = cad.core.Cell('DCWIRE')

    wireLen = ySize- 2*launcherY

    #create the boundary
    points = [[-launcherX/2, -ySize/2],[-thick/2, -wireLen/2],
            [-thick/2,wireLen/2],[-launcherX/2,ySize/2],
            [launcherX/2, ySize/2], [thick/2, wireLen/2],
            [thick/2, -wireLen/2], [launcherX/2, -ySize/2],
            [-launcherX/2, -ySize/2]]
    bdy = cad.core.Boundary(points)

    #Add to cell
    DCCell.add(bdy)

    #translate, rotate
    DCCellr = cad.core.CellReference(DCCell, rotation=rot)
    DCCellr.translate(coords)

    return DCCellr


def antennaP(coords, nFinger, fingerThick, fingerDis, ySize, xtraY=1*mm, launch=True, rot=0):
    '''
    Make a positive resist antenna
    '''
    
    #create the cell
    APCell = cad.core.Cell('ANTENNAP')

    #calculate various positions
    posX = np.arange(-(nFinger-1.)/2, (nFinger-1.)/2+1)*2*fingerDis

    #create the main antenna
    #left and right finger
    fl = posFinger((posX[0],0), fingerThick, fingerDis, ySize, leftBend=False)
    fr = posFinger((posX[-1],0), fingerThick, fingerDis, ySize, rightBend=False)
    APCell.add([fl, fr])
    #rest fingers
    for pos in posX[1:-1]:
        f = posFinger((pos,0), fingerThick, fingerDis, ySize)
        APCell.add(f)
    
    #create the extra legs
    yLim = coords[1]-ySize/2-xtraY
    xLims = [posX[0]-fingerDis/2, posX[-1]+fingerDis/2]
    r1 = cad.shapes.Rectangle([xLims[0]-fingerThick/2,yLim+xtraY],[xLims[0]+fingerThick/2,yLim])
    r2 = cad.shapes.Rectangle([xLims[1]-fingerThick/2,yLim+xtraY],[xLims[1]+fingerThick/2,yLim])
    APCell.add([r1,r2])

    #add Launchers
    if launch:
        #Define launch shape (its a triangle):
        lX = 300*um
        lY = 500*um
        t1 = [[xLims[0]-lX/2,yLim],[xLims[0], yLim+lY],[xLims[0]+lX/2, yLim],[xLims[0]-lX/2,yLim]]
        t2 = [[xLims[1]-lX/2,yLim],[xLims[1], yLim+lY],[xLims[1]+lX/2, yLim],[xLims[1]-lX/2,yLim]]
        tr1 = cad.core.Boundary(t1)
        tr2 = cad.core.Boundary(t2)
        APCell.add([tr1,tr2])

    #translate, rotate
    APCellr = cad.core.CellReference(APCell)
    APCellr.translate(coords)

    return APCellr

  

def posFinger(coords, fingerThick, fingerDis, ySize, leftBend=True, rightBend=True):

    fCell = cad.core.Cell('FINGER')
    
    #parametrize
    ir = fingerDis/2 - fingerThick/2
    our = fingerDis/2 + fingerThick/2
    straightY = ySize - 2*our
    
    #x=0 is at the top, in the center of the disc
    upperdisc = cad.shapes.Disk((0,straightY/2),our, inner_radius=ir, final_angle=180)
    fCell.add(upperdisc)

    #left part
    if leftBend:
        r = cad.shapes.Rectangle((-our,-straightY/2),(-ir, straightY/2))
        d = cad.shapes.Disk((-fingerDis, -straightY/2),our, inner_radius=ir, initial_angle=270, final_angle=360)
        fCell.add([r,d])
    else:
        r = cad.shapes.Rectangle((-our,-ySize/2),(-ir, straightY/2))
        fCell.add(r)

    #right part
    if rightBend:
        r = cad.shapes.Rectangle((our,-straightY/2),(ir, straightY/2))
        d = cad.shapes.Disk((fingerDis, -straightY/2),our, inner_radius=ir, initial_angle=180, final_angle=270)
        fCell.add([r,d])
    else:
        r = cad.shapes.Rectangle((our,-ySize/2),(ir, straightY/2))
        fCell.add(r)

    #translate, rotate
    fCellr = cad.core.CellReference(fCell)
    fCellr.translate(coords)

    return fCellr

#=========================================================================
#-----------------------------WAFER---------------------------------------
#=========================================================================


def wafer(size=1.5*inch, edge=0*mm, dphi=35, extraLayer=False):
    '''
    draw a wafer
    '''

    WC = cad.core.Cell('WAFER')

    size = size-edge

    r1 = border(5*inch, 5*inch, 1*mm)

    c1 = cad.shapes.Disk((0,0), size, inner_radius=size-.4*mm)
    c2 = cad.shapes.Disk((0,0), size, initial_angle=270-dphi, final_angle = 270+dphi)
    WC.add([r1, c1, c2])

    if extraLayer:
        c3 = cad.shapes.Disk((0,0), size+.2*mm, layer=2)
        WC.add(c3)

    #bottom stripes
    #c3b = circleSlice((0,0), size, phi=-70, dphi=5)
    #c4b = circleSlice((0,0), size, phi=-65, dphi=5)
    #c5b = circleSlice((0,0), size, phi=-60, dphi=5)
    #c3 = cad.core.Boundary(c3b)
    #c4 = cad.core.Boundary(c4b)
    #c5 = cad.core.Boundary(c5b)
    #WC.add([r1, c1,c2, c3, c4,c5])
    
    return WC

def flatCircle(coords, radius, dphi):
    ''' 
    make a flattened circle using the circBoundary function that starts on the right, 
    #goes clocwise and 
    #dphi is in degrees
    '''

    b1 = circBoundary(coords, radius, init_angle=0, final_angle=90-dphi)
    b2 = circBoundary(coords, radius, init_angle=90+dphi, final_angle=270-dphi)
    b3 = circBoundary(coords, radius, init_angle=-90+dphi, final_angle=0)
    
    return b1+b2+b3

def circBoundary(coords, radius, init_angle=0, final_angle=360, nopoints=199):
    '''
    make a boundary of circular shape
    Note that 199 is the maximum number of points permissable by GDS
    Also note that when defining boundaries, the order matters: make sure you
    draw your circle in the right direction
    '''
    dphi = float(final_angle-init_angle)/(nopoints-1)
    angles = np.arange(init_angle, final_angle+dphi, dphi)
    x,y = coords

    return [[x + radius*np.cos(rad(phi)), y + radius*np.sin(rad(phi))] for phi in angles]

def circleSlice(coords, radius, phi, dphi):
    '''
    Draws a horizontal slice of a circle
    phi is the angle for positive x around which the slice is drawn. dphi depends the angular width of the slice
    '''
    phi2 = 180 - phi
    b1 = circBoundary(coords, radius, init_angle=phi-dphi/2, final_angle = phi+dphi/2)
    b2 = circBoundary(coords, radius, init_angle=phi2-dphi/2, final_angle = phi2+dphi/2)

    return b1+b2


#==========================================================================
#------------------------------PCB-----------------------------------------
#==========================================================================

def PCBShape1(PCBSize, chipSize=(5*mm,10*mm)):
    '''
    circular design
    '''
    PC = cad.core.Cell('PCB')

    x,y = chipSize

    c1 = cad.shapes.Disk((0,0), PCBSize/2, inner_radius=PCBSize/2+1*mm)
    c2 = cad.shapes.Disk((0,0), PCBSize/2, inner_radius=PCBSize/2+1*mm,layer=1)
    #r1 = cad.shapes.Rectangle((-x/2, -y/2),(x/2,y/2))
    r2 = cad.shapes.Rectangle((-x/2, -y/2),(x/2,y/2),layer=1)
    
    #c2 = cad.shapes.Disk((0,0), size, initial_angle=270-dphi, final_angle = 270+dphi)
    PC.add([r1, c1, r2, c2])
    return PC


def PCBShape2(PCBSize, chipSize=(10*mm,5*mm)):
    '''
    square design
    '''

    PC = cad.core.Cell('PCB')

    #boundary
    xp, yp = PCBSize
    linethick = 1*mm
    b = border(xp,yp,linethick, layer=1)

    PC.add(b)
    return PC

def chip(coords, chipSize, chipType='D', vias=True, rot=0):
    '''
    draw a chip
    '''

    CC = cad.core.Cell('CHIP')

    x,y = chipSize
    r1 = cad.shapes.Rectangle((-x/2, -y/2),(x/2,y/2), layer=1)
    CC.add(r1) 

    #vias:
    if vias:
        viaCell, viaLocs = chipVias(chipSize, coords, chipType, rot)
        CC.add(viaCell)

    #rotate, translate
    CCr = cad.core.CellReference(CC, rotation=rot)
    CCr.translate(coords)

    if vias:
        return CCr, viaLocs
    else:
        return CCr

def MMPXEdge(coords, vias=True, layer=1, rot=0):
    '''
    MMPX Edge Connector
    '''

    PXCell = cad.core.Cell('MMPX')

    x, y = defaults['MMPXEdge']
    r = cad.shapes.Rectangle((-x/2,-y/2),(x/2,y/2), layer=layer)
    PXCell.add(r)

    if not vias:
        #translate, rotate
        PXCellr = cad.core.CellReference(PXCell, rotation=rot)
        PXCellr.translate(coords)
        return PXCellr

    else:
        #constants
        viaLocs = []
        ivD = defaults['interviaDistance']
        vhD = defaults['viaHorizDistance']
        #vertical part
        x1 = -x/2 - vhD
        ylocs = np.arange(-y/2-vhD,y/2,ivD)
        for y in ylocs:
            viaLocs.append([x1,y])
            viaLocs.append([-x1,y])
            v1, v2 = Via((x1,y)), Via((-x1,y))
            PXCell.add([v1,v2])
        #horizontal part
        y1 = ylocs[0]
        xlocs1 = np.arange(-x/2-vhD+ivD, -b1-vhD-ivD, ivD)
        xlocs2 = np.arange(x/2+vhD-ivD, b1+vhD+ivD, -ivD)
        xlocs = np.hstack((xlocs1,xlocs2))
        for x in xlocs:
            viaLocs.append([x,y1])
            v1 = Via([x,y1])
            PXCell.add(v1)


        #translate, rotate
        viaLocsR = transRotVias(viaLocs, trans=coords, rot=rot)
        PXCellr = cad.core.CellReference(PXCell, rotation=rot)
        PXCellr.translate(coords)
        return PXCellr, viaLocsR

def CPWroutePCB(coords, dx, dy, chipWidth=.5*mm, bridges=False, vias=True, rot=0, endrot=0):
    '''
    route a CPW from point (0,0) to (dx, dy)
    This function assumes dy to be positive. If you need negative dy, use rotate
    '''

    if dy<0:
        raise ValueError, 'dy must be positive, use rotate to get negative vertical distances'

    #init
    routeCell = cad.core.Cell('ROUTE')
    minrbend = defaults['PCBrbend']
    gap = defaults['PCBgap']
    center = defaults['PCBcenter']
    allViaLocs = []

    if endrot not in ['r', 'l']:
        if abs(dy) > abs(dx):
            if  abs(dx) >= minrbend:
                cCell, viaLocs = CPW((0, (dy-abs(dx))/2), dy-abs(dx), center=center, gap=gap, vias=True, rot=90)
                allViaLocs.append(viaLocs)
                if coords[0] < 0:
                    arcCell, viapos = CPWArc((dx, (dx+dy)), 180, 90, radius=dx, center=center, vias=True, gap=gap)
                elif coords[0] > 0:
                    arcCell, viapos = CPWArc((dx, (dy-dx)), 90, 90, radius=dx, center=center, vias=True, gap=gap)
                allViaLocs.append(viapos)
                routeCell.add([arcCell, cCell])
            
            #in case the horizontal distance is small
            elif (0 < abs(dx) < abs(minrbend)):
                #calculate span of double arc
                phirad = np.arccos(1-(abs(dx)+minrbend)/(2*minrbend))
                yspan = 2*minrbend*np.sin(phirad) # span of double arc

                if coords[0] < 0:
                    arcCell, pos1 = CPWArc((dx, (dy-minrbend)), 0, 90, radius=minrbend, center=center, gap=gap, vias=True)
                    sCell, yspanc, pos2 = doubleArc(((minrbend+dx)/2, dy-1*minrbend-yspan/2), -dx-minrbend, rbend=minrbend, center=center, gap=gap, vias=True, rot=90)
                elif coords[0] > 0:
                    arcCell, pos1 = CPWArc((dx, (dy-minrbend)), 90, 90, radius=minrbend, center=center, vias=True, gap=gap)
                    sCell, yspanc, pos2 = doubleArc((-(minrbend-dx)/2, dy-minrbend-yspan/2), minrbend-dx, rbend=minrbend, center=center, gap=gap, vias=True, rot=90)
                allViaLocs.append(pos1)
                allViaLocs.append(pos2)
                cCell, viaLocs = CPW((0, (dy-minrbend-yspan)/2), dy-minrbend-yspan, center=center, gap=gap, vias=True, rot=90)
                routeCell.add([arcCell, sCell, cCell])#, sCell, cCell])
                allViaLocs.append(viaLocs)
            else:
                print 'Undefined situation in CPWroutePCB'
    else:
        #check in which direction to bend
        print 'USING AN UNKNOWN ROUTING ALGO!!!!'
#        if dx >= 2*rbend: 
#            sCell = sLine((dx/2, rbend), dx, rbend=rbend, reflect=True, bridges=bridges, rot=90)
#            cCell = CPW((dx, dy/2+rbend), dy-2*rbend, bridges=bridges, rot=90)
#        elif dx <= -2*rbend and dx!=0:
#            sCell = sLine((dx/2, rbend), abs(dx), rbend=rbend, bridges=bridges, rot=90)
#            cCell = CPW((dx, dy/2+rbend), dy-2*rbend, bridges=bridges, rot=90)
#        elif 0 < dx <= 2*rbend:
#            sCell, yspanc = doubleArc((dx/2, yspan/2), -dx, rot=90)
#            cCell = CPW((dx, dy/2+yspan/2), dy-yspan, bridges=bridges, rot=90)
#        elif -2*rbend < dx < 0:
#            sCell, yspanc = doubleArc((dx/2, yspan/2), -dx, rot=90)
#            cCell = CPW((dx, dy/2+yspan/2), dy-yspan, bridges=bridges, rot=90)
#        elif dx == 0:
#            cCell = CPW((dx, dy/2+yspan/2), dy-yspan, bridges=bridges, rot=90)
#        if dx==0:
#            routeCell.add([cCell])
#        else:
#            routeCell.add([sCell, cCell])
#
        #Take care of the endrot
        if endrot == 'r':
            arcCell, pos = CPWArc((dx+rbend, dy), 90, 90, gap=gap, center=center, vias=True)
            allViaLocs.append(pos)
            routeCell.add(arcCell)
        elif endrot == 'l':
            arcCell, pos = CPWArc((dx-rbend, dy), 0, 90, gap=gap, center=center)
            routeCell.add(arcCell)
            allViaLocs.append(pos)
    #rotate and translate
    routeCellr = cad.core.CellReference(routeCell, rotation = rot)
    routeCellr.translate(coords[:2])

    return routeCellr, allViaLocs

def Via(coords, viaDiam=None, layer=2):

    if viaDiam==None:
        viaDiam = defaults['viaDiameter']

    VC = cad.core.Cell('VIA')
    h = cad.shapes.Disk((0,0), viaDiam/2, layer=layer)
    VC.add(h)
    
    VCr = cad.core.CellReference(VC, origin=coords)

    return VCr

def arcVias(initAngle, degrees, radius, center, gap):
    '''
    Draws vias along an arc, returns the Cell and the locations
    '''

    VA = cad.core.Cell('ARCVIA')
    vhD = defaults['PCBgap']/2+defaults['viaHorizDistance']
    ivD = defaults['interviaDistance']
    posList = []

    for i in range(1,3):
        r = radius+vhD*np.power(-1,i)
        arcLen = abs(2*np.pi*r*degrees/360)
        #TODO Just changed arcLen to abs arcLen
        if arcLen <= 2*ivD:
            locs = (r*np.cos(rad(initAngle+degrees/2)), r*np.sin(rad(initAngle+degrees/2)))
            posList.append(locs)
            VA.add(Via(locs))
        else:
            nums = np.round(arcLen/ivD)
            phi1 = degrees * (ivD/2/arcLen)
            dphi = abs((degrees/nums) * (arcLen-ivD)/(arcLen))
            phiList = np.arange(initAngle+phi1, initAngle+degrees, np.sign(degrees)*dphi)

            for p in phiList:
                nx, ny = r*np.cos(rad(p)), r*np.sin(rad(p))
                posList.append([nx, ny])
                VA.add(Via([nx,ny]))
    
    #return
    return VA, posList


def chipVias(chipSize, coords, chipType, rot):

    #make cell, define constants
    VA = cad.core.Cell('ARCVIA')
    vhD = defaults['PCBgap']/2+defaults['viaHorizDistance']
    ivD = defaults['interviaDistance']
    posList = []

    x, y = chipSize
    xv=  x+vhD
    yv = y+vhD
    
    if chipType != 'D':
        raise Exception, 'Automatic via allocation to chip is only implemented for chipType D'

    #sides
    ynums = np.round(y/ivD)
    ydis = y/(ynums-1)
    ys = np.arange(-y/2, y/2+ydis, ydis)
    for yn in ys:
        posList.extend([[-xv/2, yn],[xv/2, yn]])
        VA.add(Via([-xv/2, yn]))
        VA.add(Via([xv/2, yn]))
    
    #place 1 via between each 2 connectors:
    a, offCenters = dLists
    oC = offCenters['D'] 
    print 'oC is ', oC
    np.mean(oC)
    pos = [-np.mean(oC), 0 , np.mean(oC)] #0 is mean between oC[0] and -oC[0]
    print 'pos is ', pos
    for p in pos:
        posList.extend([[p, -yv/2],[p, yv/2]])
        VA.add(Via([p,-yv/2]))
        VA.add(Via([p,yv/2]))
     
    viaLocs = transRotVias(posList, trans=coords, rot=rot)

    return VA, viaLocs

#==========================================================================
#-------------------------------UTILITIES----------------------------------
#==========================================================================
        
def transRotVias(viaLocs, trans=(0,0), rot=0):
    '''
    rotate and translate via locations
    Input: via Locations, translation coords, rotation in degrees
    '''
    viaLocsR = []
    for viacoord in viaLocs:
        x,y = viacoord
        viaLocsR.append([x*np.cos(rot)-y*np.sin(rot)+trans[0],
            y*np.cos(rot)+x*np.sin(rot)+trans[1]])
    return viaLocsR


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

