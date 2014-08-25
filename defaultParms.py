#!/usr/bin/python
'''
This module contains the default variables for maskDesign
'''
um = 1e3
mm = 1e6

def dLists():
    '''
    populate the borderTagList and offcenters and return them
    '''

    #border sizes
    borderTagList = [(),
            (7000*um, 2000*um), 
            (7000*um, 4300*um),
            (7000*um, 6600*um)]
    offCenters = {'A' : 2470*um, 'B' : (2470*um, 1170*um, 2300*um), 
        'C' : (925*um, 2775*um, 875*um, 2625*um)}
    # entry 3 and 4: third number is distance form left center to left upper launcher
    #last entry, last 4 numbers: vertical distances, then horizontal distances
 
    return borderTagList, offCenters


def dPars():
    '''
    populate and return a dictionary with default design values
    '''

    defDict = {'centerConductor'    : 10*um,
            'CPWGap'                : 19*um,
            'minimumRadius'         : 100*um,   #Minimum radius for bends (rbend)
            'borderGap'             : 300*um,   #Gap between chips
            'alignDistance'         : 300*um,   #Distance between border and alignment markers
            'launcherWidth'         : 150*um,   #Launcher
            'launcherWidth'         : 150*um,   
            'launcherWideLen'       : 250*um,
            'launcherTaperLen'      : 250*um,
            'gapCouplerSize'        : 5*um,     #GapCoupler
            'fingerCenterLen'       : 100*um,   #FingerCoupler
            'fingerTaperLen'        : 100*um,
            'fingerLen'             : 70*um,    
            'fingerThick'           : 3*um,
            'fingerGapWidth'        : 3*um,
            'fingerGapHeight'       : 3*um,
            'ABbridgeLenX'          : 40*um,   #airbridge Options (start with AB)
            'ABbridgeLenY'          : 10*um,
            'ABfooterLen'           : 30*um,
            'ABreflowGap'           : 3*um,
            'ABirGap'               : 40*um,
            'ABlayers'              : (2,1,25),
            'ABdistance'            : 200*um,
            'ABstart'               : 100*um,   #start and end distance for airbridges
            'ABend'                 : 100*um,
            'transmonWidth'         : 300*um,
            'transmonHeight'        : 150*um,
            'cornerTransmonWidht'   : 300*um,
            'cornerTransmonHeight'  : 150*um,
            'labelFont'             : 'romand', 
            'labelFontSize'         : 500*um,
            'gateGapLen'            : 25*um,    #gap length at the end of the  gateLine
            'fluxGap'               : 2*um,     #Gap for current flow at the fluxline      
            'fluxLen'               : 40*um,    #Length of the fluxLine end      
            'fluxWidth'             : 30*um,    #Final width of the flux line      
            'lambdahalf65'          : 2*4670*um}

    return defDict

