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


def testResonators(freqList = np.arange(4,9,1), label = 'TR1', sharedLen
        = 300*um, yDis = 3*um, bridges=True,
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
    TR = cc.Sample(2, label=label, launcherConfig = 'B', alignPos = [0,3],
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
        TR.addJLine(lenList[i], .5*mm, 3*mm, 9,  'CPW1.coords', (horPos[i],
            -gap-yDis), bridges=bridges)

    TR.show()

    if export:
        TR.save()

    return TR

    
def singleRes(freq, wiggles=6, label='RES', exportName ='./wafer1/singleResonator.gds',
        labelPos = (-.5*mm, -3.1*mm), offset1=300*um, offset2 = 800*um):
    '''
    Single Resonator
    '''

    #Initialize a sample Instance 
    SR = cc.Sample(3, label=label, launcherConfig='C', 
            launcherPositions =[0,1,2,5,6,7,8,9,12,13,14,15,],
            labelPos=labelPos)
    SR.fileName = exportName

    #Figure out vertical pos of launcher
    vpos = abs(SR.launcher15.coords[1])
    print 'vpos is ', vpos

    # Add CPW on either side of launcher
    SR.addSLine(vpos, 'launcher15.connect')
    SR.addSLine(vpos, 'launcher7.connect', reflect=False, flip=True)

    #Add fingerCouplers
    SR.addFingerCoupler(5, 'sLine1.connectB')
    SR.addFingerCoupler(5, 'sLine2.connectA', flip=True)
    
    #Calculate Xspan:
    xspan = SR.fingerCoupler2.connectA[0] - SR.fingerCoupler1.connectB[0]
    leng = lambdahalf65/freq*6.5 - 300*um #subtract 2* half a gate cap
    #Add a resonator with fingerCaps and SLine
    SR.addWiggle(wiggles, leng, xspan, 'fingerCoupler1.connectB')
 
    #Add 4 Transmons
    SR.addTransmonBox('wiggle1.connectA', offset=(offset1, 0))
    SR.addTransmonBox('wiggle1.connectA', offset=(offset2,0), flip=True)
    SR.addTransmonBox('wiggle1.connectB', offset= (-offset2,0), flip=True)
    SR.addTransmonBox('wiggle1.connectB', offset=(-offset1,0))

    #GateLines
    SR.addGateLine('launcher13.connect', 'transmonBox1.connectB',
            gapOffset=(-00*um,00*um), endrot=0)
    #SR.addFluxLine('launcher12.connect', 'transmonBox1.connectC', endrot='l')

    #fluxLines
    SR.addDoubleArc(50*um, 'launcher14.connect') #prevent cableClash
    SR.addFluxLine('doubleArc1.connectA', 'transmonBox1.connectA', endrot=0)
    SR.addGateLine('launcher8.connect', 'transmonBox4.connectB', endrot='r')

    LP = md.CPWroute((0,0), -300*um, 700*um)

    SR.show()
   
    return SR



if __name__ == '__main__':
    (15.4)


#TODO Complete doubleArc class
#TODO Complete ROUTE
#TODO COMplete gateLine
#TODO complete FluxLine
