# Example chip design using Maskdesign and Chipclass
#Code by A. F. van Loo (arjanvanloo@gmail.com), GNU public license etc.
#Use at your own risk
#
import chipclass as cc
import maskDesign as md
import defaultParms as dpars
import gdsCAD as cad
import numpy as np

#get default design values
defaults = dpars.dPars()

um = 1e3
mm = 1e6
lambdahalf65 = 2*4670*um  #length-to-freq number

#default values from the config lib
center = defaults['centerConductor']
gap = defaults['CPWGap']

##################################################################################
#----------     Resonators with different frequencies on a feedLine   ------------
##################################################################################


def testResonators(freqList = np.arange(4,9,1), label = 'TR1', sharedLen
        = 200*um, yDis = 5*um, bridges=True,
        exportName = './wafer1/testresonators.gds', export=False):
    '''
    Make a bunch of test resonators

    freqList is a list of desired frequencies for the half-wavelength resonators

    sharedLen is the length overlap of the L-shaped resonator

    yDis is the centerConductor - centerConductor distance between feedLine
    and resonators
    '''

    print 'frequencies are ', freqList
    
    # Get resonator lengths from frequencies
    lenList = [lambdahalf65 / freq * 6.5 for freq in freqList]

    #Initialize a sample Instance 
    TR = cc.Sample(2, label=label, launcherConfig = 'B', alignPos = [0,1,2,3],
            launcherPositions = [0,3])
    TR.fileName = exportName

    #add the feedLine: connect a 6mm line to launcher0
    TR.addCPW(6*mm, 'launcher0.connect')

    #Calculate the horizontal distance between resonators
    horDist = 6*mm / (len(freqList)+1)
    #horPos = horDist*np.arange(1,len(freqList)+1) - 3*mm
    
    #manual position list
    horPos = [-2.1*mm,  -.6*mm, .75*mm, 1.7*mm, 2.5*mm]

    print 'horPos is ', horPos
    #Generate the JLines
    for i in range(len(freqList)):
        TR.addJLine(lenList[i], sharedLen, 3*mm, 9,  'CPW1.coords', (horPos[i],
            -gap-yDis), bridges=bridges)

    TR.show()

    if export:
        TR.save()

    return TR

##################################################################################
#----------    Single Resonator with Four Qubits                      ------------
##################################################################################
    
def singleRes(freq, wiggles=5, label='1R4QBA', exportName='./wafer1/singleResonator4Qubits.gds',
        labelPos = (-.8*mm, -3.1*mm), offset1=300*um, offset2 = 800*um,
        show=True, export=False):
    '''
    Single Resonator, four qubits
    '''

    #Initialize a sample Instance 
    SR = cc.Sample(3, label=label, launcherConfig='C', 
            launcherPositions =[0,2,5,6,7,8,10,13,14,15,],
            labelPos=labelPos)
    SR.fileName = exportName

    #Figure out vertical pos of launcher
    vpos = abs(SR.launcher15.coords[1])
    print 'vpos is ', vpos

    # Add CPW on either side of launcher to center the CPW
    SR.addSLine(vpos, 'launcher15.connect', bridges=True)
    SR.addSLine(vpos, 'launcher7.connect', bridges=True, reflect=False, flip=True)

    #Add fingerCouplers
    SR.addFingerCoupler(5, 'sLine1.connectB')
    SR.addFingerCoupler(5, 'sLine2.connectA', flip=True)
    
    #Calculate the resonator length and add the wiggle object:
    xspan = SR.fingerCoupler2.connectA[0] - SR.fingerCoupler1.connectB[0]
    leng = lambdahalf65/freq*6.5 - 300*um #subtract 2* half a gate cap
    SR.addWiggle(wiggles, leng, xspan, 'fingerCoupler1.connectB')
 
    #Qubit 1 and lines
    SR.addTransmonBox('wiggle1.connectA', offset=(offset1, 0), almarks=[1,2])
    SR.addChargeLine('launcher13.connect', 'transmonBox1.connectB',
            chargeOffset=(-00*um,00*um), endrot=0)
    SR.addDoubleArc(200*um, 'launcher14.connect', rbend=200*um) #prevent cableClash
    SR.addFluxLine('doubleArc1.connectB', 'transmonBox1.connectA', endrot=0)

    #Qubit 2 and lines
    SR.addTransmonBox('wiggle1.connectA', offset=(offset2,0), flip=True,
            almarks=[2,1])
    SR.addChargeLine('launcher2.connect', 'transmonBox2.connectB',
            chargeOffset=(-00*um,00*um), endrot=0)
    SR.addCPW(800*um, 'launcher0.connect', bridges=True) #prevent cableClash
    SR.addFluxLine('CPW1.connectB', 'transmonBox2.connectA', endrot=0)

    #qubit 3: diagonal mirror of 2
    SR.addTransmonBox('wiggle1.connectB', offset=(-offset2,0), flip=False,
            almarks=[1,2])
    SR.addChargeLine('launcher10.connect', 'transmonBox3.connectB',
        chargeOffset=(-00*um,00*um), endrot=0)
    SR.addCPW(800*um, 'launcher8.connect', bridges=True, rot=180) #prevent cableClash
    SR.addFluxLine('CPW2.connectB', 'transmonBox3.connectC', endrot=0)

    #qubit 4: diagonal mirror of 1
    SR.addTransmonBox('wiggle1.connectB', offset= (-offset1,0),flip=True,
            almarks=[2,1])
    SR.addChargeLine('launcher5.connect', 'transmonBox4.connectB',
            chargeOffset=(-00*um,00*um), endrot=0)
    SR.addDoubleArc(200*um, 'launcher6.connect', rbend=200*um, rot=180) #prevent cableClash
    SR.addFluxLine('doubleArc2.connectB', 'transmonBox4.connectC', endrot=0)

    #SR.addFluxLine('CPW2.connectB', 'transmonBox4.connectC', endrot='l')
    if show:
        SR.show()

    if export:
        SR.save()
   
    return SR


def singleRes2(freq = 7.2, export=False):
    '''
    UNFINISHED
    '''

    labelPos = (-3*mm, 2.8*mm)

    #Initialize a sample Instance 
    SR = cc.Sample(3, label='1Res4Qb2', launcherConfig='C', 
            launcherPositions =[0,3,4,5,6,7,10,11,12,13,14,15],
            labelPos=labelPos)
    SR.fileName = './wafer1/singleResv2.gds'

    #length of the resonator
    lambdahalf65 = defaults['lambdahalf65']
    totLen = lambdahalf65/freq*6.5 - 300*um
    print 'totalLen = ', totLen

    #divide into parts
    yLen = 5*mm
    bbend = 200*um
    xLen2 = totLen - yLen - bbend*np.pi
    print ' ylen2 is ', xLen2
    
    #Build the resonator from the center!
    SR.addCPW(totLen/2,(0,0))

  
    SR.addDoubleArc(100*um, 'launcher14.connect')
    SR.addCPW(200*um, 'doubleArc1.connectB')
    SR.addFingerCoupler(4, 'CPW1.connectB')

    SR.show()

    if export==True:
        SR.save()

    return SR

def singleRes3(freq = 7.2, export=False):
    '''
    UNFINISHED
    '''

    labelPos = (-3*mm, 2.8*mm)

    #Initialize a sample Instance 
    SR = cc.Sample(3, label='1Res4Qb2', launcherConfig='C', 
            launcherPositions =[0,3,4,5,6,7,10,11,12,13,14,15],
            labelPos=labelPos)
    SR.fileName = './wafer1/singleResv2.gds'

    #length of the resonator
    lambdahalf65 = defaults['lambdahalf65']
    totLen = lambdahalf65/freq*6.5 - 300*um
    print 'totalLen = ', totLen

    #totlen = 2*2*np.pi *radius * cpart/360
    cpart = 120.
    startangle = 135 - cpart/2
    radius = totLen/ (2*2*np.pi*cpart/360) 

    SR.addArc(startangle, cpart,
            (-radius*np.cos(rad(startangle+cpart)),-radius*np.sin(rad(startangle+cpart))),
            rbend = radius)
    SR.addArc(startangle-180+cpart, -cpart, 'arc1.connectB', rbend = radius)
    SR.addFingerCoupler(3, 'arc1.connectA', rot=90+startangle, flip=True)
    SR.addFingerCoupler(3, 'arc2.connectB', rot=90+startangle, flip=False)

  
    SR.addDoubleArc(100*um, 'launcher14.connect')
    SR.addCPW(200*um, 'doubleArc1.connectB')
    #SR.addFingerCoupler(4, 'CPW1.connectB')

    SR.show()

    if export==True:
        SR.save()

    return SR


###################################################################################
#---------------------- Open Transmission Line Samples     ------------------------
###################################################################################


def openTrans3qb(freq = 6.4, label='OT3Q',
        exportName ='./wafer1/openTransmissionLine3Qubits.gds', 
        export=False, show=True):
    '''
    Makes a chip with an open transmission line and 3 qubits, no charge and
    gate lines.
    '''

    #Initialize a sample Instance 
    OT = cc.Sample(1, label=label, launcherConfig='A', 
            launcherPositions =[0,4], alignPos=range(3),
            labelPos=(-3.45*mm, -1.05*mm))
    OT.fileName = exportName

    #calculate length between qubits
    #load length of a 6.5GHz lambdahalf resonator
    lambdahalf65 = defaults['lambdahalf65']
    transLen = 2*lambdahalf65/freq*6.5
    
    #start and end with a CPW, so that the transmons can be connected at wiggle ends
    OT.addCPW(300*um, 'launcher0.connect')
    OT.addWiggle(11, transLen, 2.7*mm, 'CPW1.connectB', bridges='more')
    OT.addCPW(300*um, 'launcher4.connect',flip=True)
    OT.addWiggle(11, transLen, 2.7*mm, 'wiggle1.connectB', bridges='more')

    #add Transmons
    OT.addTransmonBox('wiggle1.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectB', offset=(0,0))

    #manual airbridges at launchers and qubits
    OT.addAirbridge('launcher0.connect', offset=(50*um, 0), rot=90)
    OT.addAirbridge('launcher4.connect', offset=(-50*um, 0), rot=90)
    
    if show:
        OT.show()

    if export:
        OT.save()

    return OT


def openTrans3qbC(freq = 7.2, label='',
        exportName ='./wafer1/openTransmissionLine3QubitsCharge.gds', 
        export=False, show=True):
    '''
    Makes a chip with an open transmission line and 3 qubits, no charge and
    gate lines.
    '''

    #delete previous instance
    if 'OT' in locals():
        del(OT)
        print 'previous instance deleted'

    #Initialize a sample Instance 
    OT = cc.Sample(1, label=label, launcherConfig='A', 
            launcherPositions =[0,4,5,6,7], alignPos=range(1,4),
            labelPos=(-3.15*mm, .55*mm))
    OT.fileName = exportName

    OT.addText('D17_v1', (-3.25*mm, .2*mm), fontSize = 250*um,
            font='gothgbt',rot=90)

    #calculate length between qubits
    #load length of a 6.5GHz lambdahalf resonator
    lambdahalf65 = defaults['lambdahalf65']
    transLen = 2*lambdahalf65/freq*6.5
    #start and end with a CPW, so that the transmons can be connected at wiggle ends
    OT.addCPW(300*um, 'launcher0.connect')
    OT.addWiggle(11, transLen, 2.7*mm, 'CPW1.connectB', bridges='more')
    OT.addCPW(300*um, 'launcher4.connect',flip=True)
    OT.addWiggle(11, transLen, 2.7*mm, 'wiggle1.connectB', bridges='more')

    #add Transmons
    OT.addTransmonBox('wiggle1.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectB', offset=(0,0))

    #manual airbridges at launchers and qubits
    OT.addAirbridge('launcher0.connect', offset=(50*um, 0), rot=90)
    OT.addAirbridge('launcher4.connect', offset=(-50*um, 0), rot=90)

    #A few more at qubits
    OT.addAirbridge('transmonBox1.connectB', offset=(0*um, -100*um), rot=0)
    OT.addAirbridge('transmonBox1.connectB', offset=(100*um, -240*um), rot=90)
    OT.addAirbridge('transmonBox2.connectB', offset=(0*um, -100*um), rot=0)
    OT.addAirbridge('transmonBox2.connectB', offset=(0*um, -240*um), rot=0)
    OT.addAirbridge('transmonBox3.connectB', offset=(0*um, -100*um), rot=0)
    OT.addAirbridge('transmonBox3.connectB', offset=(-100*um, -240*um), rot=90)

    #charge Lines
    OT.addChargeLine('launcher7.connect', 'transmonBox1.connectB')
    OT.addChargeLine('launcher6.connect', 'transmonBox2.connectB')
    OT.addChargeLine('launcher5.connect', 'transmonBox3.connectB')
    
    if show:
        OT.show()

    if export:
        OT.save()

    return OT


def openTrans3qbF(freq = 7.2, label='',
        exportName ='./wafer1/openTransmissionLine3QubitsFlux.gds', 
        export=False, show=True):
    '''
    Makes a chip with an open transmission line and 3 qubits, no charge and
    gate lines.
    '''

    #delete previous instance
    if 'OT' in locals():
        del(OT)
        print 'previous instance deleted'

    #Initialize a sample Instance 
    OT = cc.Sample(1, label=label, launcherConfig='A', 
            launcherPositions =[0,4,5,6,7], alignPos=range(1,4),
            labelPos=(-3.15*mm, .55*mm))
    OT.fileName = exportName

    OT.addText('D17_v1', (-3.25*mm, .2*mm), fontSize = 250*um,
            font='gothgbt',rot=90)

    #calculate length between qubits
    #load length of a 6.5GHz lambdahalf resonator
    lambdahalf65 = defaults['lambdahalf65']
    transLen = 2*lambdahalf65/freq*6.5
    #start and end with a CPW, so that the transmons can be connected at wiggle ends
    OT.addCPW(300*um, 'launcher0.connect')
    OT.addWiggle(11, transLen, 2.7*mm, 'CPW1.connectB', bridges='more')
    OT.addCPW(300*um, 'launcher4.connect',flip=True)
    OT.addWiggle(11, transLen, 2.7*mm, 'wiggle1.connectB', bridges='more')

    #add Transmons
    OT.addTransmonBox('wiggle1.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectB', offset=(0,0))


    #Flux lines, right and left Lines
    OT.addFluxLine('launcher7.connect', 'transmonBox1.connectC', endrot = 'l')
    OT.addFluxLine('launcher5.connect', 'transmonBox3.connectA', endrot = 'r')

    #fluxLine center
    OT.addSLine(289*um, 'launcher6.connect', reflect=True, flip=True, rot=90)
    OT.addFluxLine('sLine1.connectB', 'transmonBox2.connectC', endrot = 'l')

    #manual airbridges at launchers and qubits
    OT.addAirbridge('launcher0.connect', offset=(50*um, 0), rot=90)
    OT.addAirbridge('launcher4.connect', offset=(-50*um, 0), rot=90)

    #A few more at qubits
    OT.addAirbridge('transmonBox1.connectC', offset=(+140*um, -100*um), rot=0)
    OT.addAirbridge('transmonBox1.connectC', offset=(+140*um, -240*um), rot=0)
    OT.addAirbridge('transmonBox2.connectC', offset=(140*um, -100*um), rot=0)
    OT.addAirbridge('transmonBox2.connectC', offset=(140*um, -200*um), rot=0)
    OT.addAirbridge('transmonBox3.connectA', offset=(-140*um, -100*um), rot=0)
    OT.addAirbridge('transmonBox3.connectA', offset=(-140*um, -240*um), rot=0)

    if show:
        OT.show()

    if export:
        OT.save()

    return OT

 
def openTrans4qb(freq = 7.2, label='',
        exportName ='./wafer1/openTransmissionLine4Qubits.gds', 
        export=False, show=True):
    '''
    Makes a chip with an open transmission line and 3 qubits, no charge and
    gate lines.
    '''

    #delete previous instance
    if 'OT' in locals():
        del(OT)
        print 'previous instance deleted'

    #Initialize a sample Instance 
    OT = cc.Sample(2, label=label, launcherConfig='A', 
            launcherPositions =[0,4], alignPos=range(1,4))
    OT.fileName = exportName

    OT.addText('OT4Q', (-2.9*mm, .8*mm), fontSize = 600*um,rot=90)

    #calculate length between qubits
    #load length of a 6.5GHz lambdahalf resonator
    lambdahalf65 = defaults['lambdahalf65']
    transLen = 2*lambdahalf65/freq*6.5
    #start and end with a CPW, so that the transmons can be connected at wiggle ends
    OT.addCPW(300*um, 'launcher0.connect')
    OT.addWiggle(6, transLen, 1.8*mm, 'CPW1.connectB', bridges='more')
    OT.addWiggle(6, transLen, 1.8*mm, 'wiggle1.connectB', bridges='more')
    OT.addWiggle(6, transLen, 1.8*mm, 'wiggle2.connectB', bridges='more')
    OT.addCPW(300*um, 'launcher4.connect',flip=True)

    #add Transmons
    OT.addTransmonBox('wiggle1.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle3.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle3.connectB', offset=(0,0))

    #manual airbridges at launchers and qubits
    OT.addAirbridge('launcher0.connect', offset=(50*um, 0), rot=90)
    OT.addAirbridge('launcher4.connect', offset=(-50*um, 0), rot=90)

    if show:
        OT.show()

    if export:
        OT.save()

    return OT

        
def openTrans4qbC(freq=7.2, label='',
        exportName ='./wafer1/openTransmissionLine4QubitsCharge.gds', 
        export=False, show=True):
    '''
    Makes a chip with an open transmission line and 3 qubits, no charge and
    gate lines.
    '''

    #delete previous instance
    if 'OT' in locals():
        del(OT)
        print 'previous instance deleted'

    #Initialize a sample Instance 
    OT = cc.Sample(2, label=label, launcherConfig='A', 
            launcherPositions =[0,2,3,4,6,7], alignPos=range(1,4),
            labelPos=(-3.15*mm, .55*mm))
    OT.fileName = exportName

    OT.addText('D17_v2', (-3.4*mm, 1.75*mm), fontSize = 450*um,
            font='gothgbt',rot=0)

    #calculate length between qubits
    #load length of a 6.5GHz lambdahalf resonator
    lambdahalf65 = defaults['lambdahalf65']
    transLen = 2*lambdahalf65/freq*6.5
    skewDis = 900*um
    #start and end with a CPW, so that the transmons can be connected at wiggle ends
    OT.addSLine(skewDis, 'launcher0.connect', reflect=True, bridges=True)
    OT.addCPW(160*um, 'sLine1.connectB')
    #OT.addWiggle(6, transLen, 1.7*mm, 'launcher0.connect', bridges='more')
    OT.addWiggle(5, transLen, 1.6*mm, 'CPW1.connectB', bridges='more',
            skew=skewDis, yOffset=0)
    OT.addWiggle(8, transLen, 2.08*mm, 'wiggle1.connectB', bridges='more',
            skew=-skewDis, yOffset=0)
    OT.addWiggle(5, transLen, 1.6*mm, 'wiggle2.connectB', bridges='more',
            skew=skewDis, yOffset=0)
    OT.addCPW(160*um, 'wiggle3.connectB')
    OT.addSLine(skewDis, 'CPW2.connectB', reflect=True, bridges=True)

    #add Transmons
    OT.addTransmonBox('wiggle1.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle2.connectA', offset=(0,0), flip=True)
    OT.addTransmonBox('wiggle3.connectA', offset=(0,0))
    OT.addTransmonBox('wiggle3.connectB', offset=(0,0), flip=True)

    #charge Lines
    OT.addChargeLine('launcher7.connect', 'transmonBox1.connectB')
    OT.addChargeLine('launcher2.connect', 'transmonBox2.connectB')
    OT.addChargeLine('launcher6.connect', 'transmonBox3.connectB')
    OT.addChargeLine('launcher3.connect', 'transmonBox4.connectB')
    
    if show:
        OT.show()

    if export:
        OT.save()

    return OT

##################################################################################
#----------     --------------------Miscellanerous-----------------   ------------
##################################################################################

def testing(label='test', exportName = 'temptest.gds'):
    '''
    A function for testing scenarios
    '''
    
    #Initialize a sample Instance 
    SR = cc.Sample(3, label='testTEST', launcherConfig='C', 
            launcherPositions =[0,1,2,5,6,7,8,9,12,13,14,15],
            labelPos=(-3*mm, -3*mm))
    SR.fileName = exportName

    #testing transmonbox connectors
    test = 'D'

    SR.addCPW(2*mm, (0,2*mm), rot=90)
    SR.addCPW(2*mm, (0,2*mm), rot=0)
    SR.addCPW(2*mm, (-1*mm,2*mm), rot=90)

    SR.addWiggle(5, 5*mm, 2*mm,(-2.5*mm,2.5*mm), closeB=True)
    SR.addCPW(2*mm, (-0.5*mm,2.4*mm), closeB=True)

    SR.addCornerTransmonBox('CPW2.coords', offset=(0,0), rot=0)
    SR.addCornerTransmonBox('CPW2.coords', offset=(.5*mm,0), rot=90)
    SR.addCornerTransmonBox('CPW2.coords', offset=(1*mm,0), rot=180)
    SR.addCornerTransmonBox('CPW2.coords', offset=(1.5*mm,0), rot=270)
    #SR.addCornerTransmonBox(['CPW2.coords','CPW3.coords'], offset=(0*um,0), rot=270)

    SR.addFluxLine((2*mm,-2*mm), 'cornerTransmonBox1.connect'+test, endrot='r',
            fluxOffset = (100*um, 100*um), startrot=90)
    SR.addFluxLine((2*mm,-2*mm), 'cornerTransmonBox2.connect'+test, endrot='r',
            fluxOffset = (100*um, 100*um), startrot=90)
    SR.addFluxLine((2*mm,-2*mm), 'cornerTransmonBox3.connect'+test, endrot='r',
            fluxOffset = (100*um, 100*um), startrot=90)
    SR.addFluxLine((2*mm,-2*mm), 'cornerTransmonBox4.connect'+test, endrot='r',
            fluxOffset = (100*um, 100*um), startrot=90)
    
    SR.addChargeLine((2*mm, -2*mm), 'cornerTransmonBox4.connect'+test, endrot='r', chargeOffset = (100*um, 100*um), startrot=90)

    SR.show()


def rad(degrees):
    return degrees*2*np.pi/360


if __name__ == '__main__':
    (15.4)

#TODO TRANSMONBOXESCORNER
#TODO Test Merge
#TODO AllComponents
#TODO Multi-Paramp
#TODO
#TODO
#TODO

