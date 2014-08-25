# Example chip design using Maskdesign and Chipclass
#Code by A. F. van Loo (arjanvanloo@gmail.com), GNU public license etc.
#Use at your own risk
#
import chipclass as cc
import maskDesign as md
import defaultParms as dpars
import gdsCAD as cad

#get default design values
defaults = dpars.dPars()

um = 1e3
mm = 1e6
lambdaquarter65 = 4670*um  #length-to-freq number

#default values from the config lib
center = defaults['centerConductor']
gap = defaults['CPWGap']

def singleParamp(barefreq, label, exportName='0123test.gds', bridges=True, export=False, show=True):
    '''
    build a single Paramp

    Inputs:
    barefreq (in GHz) determines the length of the coplanar waveguide
    Note that this is only the frequency of the quarter lambda resonator, and
    therefore by NO MEANS is the paramp frequency! Not even close!
    
    label: the label on the chip.

    ExportName: the filename to export to

    export = False: by default, the file is not exported. If you want to export
    it, set export = True

    show= True: disable this to  not show the output when calling the function
    '''

    #Make sure sample starts drawing from scratch:
    if 'P1' in locals():
        del(P1)
        print 'deleted previous instance'

    #define some parameters
    taperLen = 200*um #taper after the cap
    capLen = 100*um #capacitor
    gapLen = 150*um

    #calculate the length from the bare frequency of the resonator
    #subtract the capacitor, taperlength and gaplength
    cpwLen = lambdaquarter65/barefreq*6.5 - capLen - taperLen - gapLen
    print 'cpwlen, this time, is ', cpwLen

    #Initialize sample. Paramp has no normal launchers
    P1 = cc.Sample(1,label=label, alignPos = [0,2], labelPos = (-3.4*mm,-.9*mm))

    #The first part of the params: use a launcher with non-default options
    P1.launcherPositions = [0]
    P1.addLaunchers(center=69*um, gap=1.9*69*um)

    #add fingerCap
    P1.addFingerCoupler(12, 'launcher0.connect',taperLen=0, fingerLen=94*um,centerLen = capLen)

    #Add a taper from the ChipClass
    P1.addTaper(taperLen, 'fingerCoupler1.connectB', 69*um)

    #Add a CPW and a gap
    if bridges:
        P1.addCPW(cpwLen, 'taper1.connectB', bridges=True, bridgeDistance=400*um,
                bridgeEnd = cpwLen/2-400*um)
    else:
        P1.addCPW(cpwLen, 'taper1.connectB')
    P1.addGapCoupler(gapLen, 'CPW1.connectB')

    #Add Isolation
    xpoint = cpwLen
    r1 = cad.shapes.Rectangle((1050*um+cpwLen-3500*um,-1100*um),
            (cpwLen+1550*um-3500*um, 1100*um)) 
    r2 = cad.shapes.Rectangle((850*um+cpwLen-3500*um, 100*um+gap/2),
            (cpwLen+1050*um-3500*um, 1100*um)) 
    r3 = cad.shapes.Rectangle((850*um+cpwLen-3500*um, -1100*um),
            (cpwLen+1050*um-3500*um,-100*um-gap/2)) 
    P1.topCell.add([r1,r2,r3])

    fP = md.fourPoint((2600*um,0))
    P1.topCell.add(fP)

    P1.addCrossArray('gapCoupler1.coords')

    if show:
        P1.show()

    if export:
        P1.fileName = exportName
        P1.save()

    return P1

def doubleParamp(barefreq1, barefreq2, label, exportName='./wafer1/0123test.gds',
        bridges = True, fourPoint = True, export=False, show=True):
    '''
    build two Paramps with a fourPointMeasurement device in the center

    Inputs:
    barefreq1 and barefreq2 (in GHz) determine the length of the coplanar waveguide
    Note that these are only the frequencies of the quarter lambda resonators, and
    therefore by NO MEANS are the paramp frequencies! Not even close!
    
    label: the label on the chip.

    ExportName: the filename to export to

    export = False: by default, the file is not exported. If you want to export
    it, set export = True

    show= True: disable this to now show the output when calling the function
    '''

    #Make sure sample starts drawing from scratch:
    if 'P1' in locals():
        del(P1)
        print 'deleted previous instance'

    #define some parameters
    taperLen = 200*um #taper after the cap
    capLen = 100*um #capacitor
    gapLen = 150*um

    #calculate the length from the bare frequency of the resonator
    #subtract the capacitor, taperlength and gaplength
    cpwLen1 = lambdaquarter65/barefreq1*6.5 - capLen - taperLen - gapLen
    cpwLen2 = lambdaquarter65/barefreq2*6.5 - capLen - taperLen - gapLen
    print 'cpwlen1 is  ', cpwLen1
    print 'cpwlen2 is  ', cpwLen2

    #initialize sample. paramp has no normal launchers
    P1 = cc.Sample(1,label=label, alignPos = [0,1,2], labelPos = (-3.4*mm,-.9*mm))
    P1.fileName = exportName

    #the first part of the params: use a launcher with non-default options
    P1.launcherPositions = [0,4]
    P1.addLaunchers(center=69*um, gap=1.9*69*um)

    #add fingerCap2
    P1.addFingerCoupler(12, 'launcher0.connect',taperLen=0, fingerLen=94*um,centerLen = capLen)
    P1.addFingerCoupler(12, 'launcher4.connect',taperLen=0, fingerLen=94*um,centerLen = capLen, rot=180)

    #Add a taper from the ChipClass
    P1.addTaper(taperLen, 'fingerCoupler1.connectB', 69*um)
    P1.addTaper(taperLen, 'fingerCoupler2.connectB', 69*um, rot=180)

    #Add a CPW and a gap
    if bridges:
        P1.addCPW(cpwLen1, 'taper1.connectB', bridges=True, bridgeEnd = 400*um)
        P1.addCPW(cpwLen2, 'taper2.connectB', rot=180, bridges=True, bridgeEnd = 400*um)
    else:
        P1.addCPW(cpwLen1, 'taper1.connectB')
        P1.addCPW(cpwLen2, 'taper2.connectB', rot=180)
    P1.addGapCoupler(gapLen, 'CPW1.connectB')
    P1.addGapCoupler(gapLen, 'CPW2.connectB', flip=True)

    #Add Isolation: left
    l1 = cad.shapes.Rectangle((1050*um+cpwLen1-3500*um,-1100*um),
            (cpwLen1+1550*um-3500*um, 1100*um)) 
    l2 = cad.shapes.Rectangle((850*um+cpwLen1-3500*um, 100*um+gap/2),
            (cpwLen1+1050*um-3500*um, 1100*um)) 
    l3 = cad.shapes.Rectangle((850*um+cpwLen1-3500*um, -1100*um),
            (cpwLen1+1050*um-3500*um,-100*um-gap/2)) 
    #Add Isolation Right
    r1 = cad.shapes.Rectangle((-1050*um-cpwLen2+3500*um,-1100*um),
            (-cpwLen2-1550*um+3500*um, 1100*um)) 
    r2 = cad.shapes.Rectangle((-850*um-cpwLen2+3500*um, 100*um+gap/2),
            (-cpwLen2-1050*um+3500*um, 1100*um)) 
    r3 = cad.shapes.Rectangle((-850*um-cpwLen2+3500*um, -1100*um),
            (-cpwLen2-1050*um+3500*um,-100*um-gap/2)) 

    P1.topCell.add([l1, l2, l3, r1,r2,r3])

    if fourPoint:
        xfp = (cpwLen1 - cpwLen2)/2
        fP = md.fourPoint((xfp,0))
        P1.topCell.add(fP)

    P1.addCrossArray('gapCoupler1.coords')
    P1.addCrossArray('gapCoupler2.coords')
    
    if show:
        P1.show()

    if export:
        P1.fileName = exportName
        P1.save()

    return P1

def lunmpedParamp(label = 'LP1', exportName = './wafer1/LumpedParamp1.gds', export= False):
    '''
    Since this is a rather irregular design, the code will be ugly
    '''

    #Capacitor properties
    finger1Thick = 100*um
    finger2Thick = 80*um
    cap1Len = 100*um
    cap2Len = 200*um
    thick1 = finger1Thick/27
    thick2 = finger2Thick/27
    finger1Len =  cap1Len - 2* thick1
    finger2Len = cap2Len - 2* thick2

    #island properties
    iY = -00*um
    dX = 300*um
    #X position
    iX = -3000*um +dX/2 + cap1Len

    #Initialize sample. Paramp has no normal launchers
    LP = cc.Sample(1,label=label, alignPos = [1,2])
    LP.fileName = exportName

    #the first part of the params: use a launcher with non-default options
    Lp.launcherPositions = [0,4]
    Lp.addLaunchers(center=100*um, gap=1.9*100*um)

    #add fingerCaps
    LP.addFingerCap(14, (iX-dX/2-cap1Len/2, iY), fingerLen=finger1Len, fingerThick = thick1,
            gapHeight = thick1, gapWidth=thick1)
    LP.addFingerCap(14, (iX, iY+finger1Thick/2+cap2Len/2), fingerLen=finger2Len, 
            fingerThick = thick2, gapHeight = thick2, gapWidth=thick2, rot=90)
    LP.addFingerCap(14, (iX, iY-finger1Thick/2-cap2Len/2), fingerLen=finger2Len, 
            fingerThick = thick2, gapHeight = thick2, gapWidth=thick2,rot=90)

    #Squares
    r1 = cad.shapes.Rectangle((iX-dX/2-cap1Len,iY+finger1Thick/2),(iX-finger2Thick/2,
        iY + finger1Thick/2+cap2Len))
    r2 = cad.shapes.Rectangle((iX-dX/2-cap1Len,iY-finger1Thick/2),(iX-finger2Thick/2,
        iY-finger1Thick/2-cap2Len))
    r3 = cad.shapes.Rectangle((iX+finger2Thick/2,iY+finger1Thick/2),
            (iX+dX/2, iY+finger1Thick/2+cap2Len))
    r4 = cad.shapes.Rectangle((iX+finger2Thick/2, iY - finger1Thick/2),
            (iX+dX/2, iY - finger1Thick/2-cap2Len))
    LP.topCell.add([r1,r2,r3,r4])

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
    alCellr1 = cad.core.CellReference(alCell)
    alCellr2 = cad.core.CellReference(alCell, rotation=270)
    alCellr3 = cad.core.CellReference(alCell, rotation=180)
    alCellr4 = cad.core.CellReference(alCell, rotation=90)
    
    alCell2.add([alCellr1, alCellr2, alCellr3, alCellr4])
    alCell2r = cad.core.CellReference(alCell2, origin=(iX+dX/2+boxSize/2, iY))

    #add to topCell
    LP.topCell.add(alCell2r)

    #add rectangles
    r5 = cad.shapes.Rectangle((iX+dX/2,iY+boxSize/2),
            (iX+dX/2+boxSize, iY+cap2Len+finger1Thick/2))
    r6 = cad.shapes.Rectangle((iX+dX/2,iY-boxSize/2),
            (iX+dX/2+boxSize, iY-cap2Len-finger1Thick/2))
    LP.topCell.add([r5,r6])
    
    LP.show()

    if export:
        LP.fileName = exportName
        LP.save()

    return LP


def lumpedParamps(label='MLP', exportName = './wafer1/multiLumpedParamp.gds',
        export=False):


    
    #Initialize sample. Paramp has no normal launchers
    LPs = cc.Sample(1,label=label, labelPos = (-2.2*mm,-1*mm))
    LPs.fileName = exportName

    #the first part of the params: use a launcher with non-default options
    LPs.launcherPositions = range(1,4)+range(5,8)
    LPs.addLaunchers(center=100*um, gap=1.9*100*um)

    #Figure out the x-spacing of launchers
    x = LPs.launcher3.coords[0]

    #set the islandsize of vertical paramps to 100um
    isl = 100*um
    vsize = isl+200*um #add twice default length of fingerCap1

    #add lumped element paramps
    #LP1 = md.lumpedParamp((-2.8*mm,0), islandX=300*um, nFinger1=20, nFinger2=10, rot=0)
    LP2 = md.lumpedParamp((-x,.5*mm-vsize/2), islandX=isl, nFinger1=18, nFinger2=9, rot=270)
    LP3 = md.lumpedParamp((0,.5*mm-vsize/2), islandX=isl, nFinger1=16,nFinger2=8, rot=270)
    LP4 = md.lumpedParamp((x,.5*mm-vsize/2), islandX=isl, nFinger1=14, nFinger2=7, rot=270)
    #LP5 = md.lumpedParamp((2.8*mm,0), islandX=300*um, nFinger1=12, nFinger2=6, rot=180)
    LP6 = md.lumpedParamp((x,-.5*mm+vsize/2), islandX=isl, nFinger1=10, nFinger2=5, rot=90)
    LP7 = md.lumpedParamp((0,-.5*mm+vsize/2), islandX=isl, nFinger1=8, nFinger2=4, rot=90)
    LP8 = md.lumpedParamp((-x,-.5*mm+vsize/2), islandX=isl, nFinger1=8, nFinger2=6, rot=90)

    LPs.topCell.add([LP2, LP3, LP4, LP6, LP7, LP8])

    #add boundaries:
    hthick = 50*um #half of the thickness
    rH = cad.shapes.Rectangle((-3.5*mm, -hthick),(3.5*mm, hthick)) 
    rV1 = cad.shapes.Rectangle((-x/2-hthick, -1*mm),(-x/2+hthick, 1*mm)) 
    rV2 = cad.shapes.Rectangle((x/2-hthick, -1*mm),(x/2+hthick, 1*mm)) 

    LPs.topCell.add([rH, rV1, rV2])

    LPs.show()

    if export == True:
        LPs.save()

    return LPs


def lumpedParampsFourPoint(label='', exportName = './wafer1/lumpedParampsFourPoint.gds',
        export=False, show=True):
    
    #Initialize sample. Paramp has no normal launchers
    LPs = cc.Sample(1,label=label, labelPos = (-2.2*mm,-1*mm), alignPos=[])
    LPs.fileName = exportName

    #the first part of the params: use a launcher with non-default options
    LPs.launcherPositions = [1,3,5,7]
    LPs.addLaunchers(center=100*um, gap=1.9*100*um)

    #Figure out the x-spacing of launchers
    x = LPs.launcher3.coords[0]

    #set the islandsize of vertical paramps to 100um
    isl = 100*um
    vsize = isl+200*um #add twice default length of fingerCap1

    #add lumped element paramps
    LP1 = md.lumpedParamp((-x,.5*mm-vsize/2), islandX=isl, nFinger1=18, nFinger2=9, rot=270)
    LP3 = md.lumpedParamp((x,.5*mm-vsize/2), islandX=isl, nFinger1=14, nFinger2=7, rot=270)
    LP5 = md.lumpedParamp((x,-.5*mm+vsize/2), islandX=isl, nFinger1=10, nFinger2=5, rot=90)
    LP7 = md.lumpedParamp((-x,-.5*mm+vsize/2), islandX=isl, nFinger1=8, nFinger2=4, rot=90)
    LPs.topCell.add([LP1, LP3, LP5, LP7])

    #add a fourpoint measurement thing
    fP = md.fourPoint((0,0))
    LPs.topCell.add(fP)



    #add boundaries:
    hthick = 50*um #half of the thickness
    rH1 = cad.shapes.Rectangle((-3.5*mm, -hthick),(-x/2-hthick, hthick)) 
    rH2 = cad.shapes.Rectangle((x/2+hthick, -hthick),(3.5*mm, hthick)) 
    rV1 = cad.shapes.Rectangle((-x/2-hthick, -1*mm),(-x/2+hthick, 1*mm)) 
    rV2 = cad.shapes.Rectangle((x/2-hthick, -1*mm),(x/2+hthick, 1*mm)) 
    LPs.topCell.add([rH1, rH2, rV1, rV2])

    if show:
        LPs.show()

    if export == True:
        LPs.save()

    return LPs

    #Inductor _ NOT NEEDED!
#    thin = 4*um
#    thick = 10*um
#    dis = 12*um     #distance at snaky part
#    thickLen = 80*um
#    cellLen = 150*um
#    cellHigh = 50*um
#    xLen = 20*um    #extra Len next to thick for snaky part
#
#    #Inductor Cell, origin center Left
#    inCell = cad.core.Cell('INDUC')
#
#    points1 = [[0,cellHigh],[cellLen, cellHigh],
#            [cellLen, -dis-thin/2],[cellLen/2+thickLen/2, -dis-thin/2],
#            [cellLen/2+thickLen/2, -thin + thick/2 - dis],
#            [cellLen/2-thickLen/2, -thin + thick/2 - dis],
#            [cellLen/2-thickLen/2, -dis - thin/2],
#            [cellLen/2-thickLen/2-xLen, -dis - thin/2],
#            [cellLen/2-thickLen/2-xLen, - thin/2],
#            [cellLen/2+thickLen/2+xLen+thin, - thin/2],
#            [cellLen/2+thickLen/2+xLen+thin, dis + 3*thin/2],
#            [cellLen/2+thickLen/2, dis + 3*thin/2],
#            [cellLen/2+thickLen/2, dis + thin+thick/2],
#            [cellLen/2-thickLen/2, dis + thin+thick/2],
#            [cellLen/2-thickLen/2, dis + 3*thin/2],
#            [0, dis + 3*thin/2],
#            [0, cellHigh]]
#    sq1 = cad.core.Boundary(points1)
#
#    points2 = [[0, dis+thin/2], [cellLen/2-thickLen/2, dis+thin/2],
#            [cellLen/2-thickLen/2, dis+thin-thick/2],
#            [cellLen/2+thickLen/2, dis+thin-thick/2],
#            [cellLen/2+thickLen/2, dis+thin/2],
#            [cellLen/2+thickLen/2+xLen, dis+thin/2],
#            [cellLen/2+thickLen/2+xLen, thin/2],
#            [cellLen/2-thickLen/2-xLen-thin, thin/2],
#            [cellLen/2-thickLen/2-xLen-thin, -dis - 3*thin/2],
#            [cellLen/2-thickLen/2, -dis - 3*thin/2],
#            [cellLen/2-thickLen/2, -dis - thin - thick/2],
#            [cellLen/2+thickLen/2, -dis - thin - thick/2],
#            [cellLen/2+thickLen/2, -dis - 3*thin/2 ],
#            [cellLen, -dis - 3*thin/2 ],
#            [cellLen, -cellHigh], [0,-cellHigh],[0,dis+thin/2]]
#    sq2 = cad.core.Boundary(points2)
#
    #add squares
    #r5 = cad.shapes.Rectangle((0,cellHigh),
    #        (0+cellLen, cellHigh + cap2Len))
    #r6 = cad.shapes.Rectangle((0, -cellHigh),
    #        (0+cellLen, -cellHigh - cap2Len ))
    #r7 = cad.shapes.Rectangle((0,-cellHigh),(0+cellLen, cellHigh))

    #inCell.add([sq1,sq2, r5, r6])
    #inCell.add([sq1,sq2, r5, r6, r7])
    #inCellr = cad.core.CellReference(inCell, rotation = 0)
    #inCellr.translate((iX+dX/2,iY))

    #LP.topCell.add(inCellr)
            

    


if __name__ == '__main__':
    singleParamp(15.4)
