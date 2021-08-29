#!/usr/bin/env python3
# need the data from vaspkit to get the information of fatbands
# this script helps you to get the band you are interested in. you should use data_separate_by_line.sh to get the seperated band data firstly
#
import numpy as np

# get the neaded information -----------------------------------------------------------------------------------------------------------------------------------------------

nbnd = int(input('The number of bands :\n'))
Emin = float(input('The energy range you are interested in:\nThe Emin: \n'))
Emax = float(input('The Emax: \n'))
datapath = input('Please input the bandseperated data path(XXX/): \n')


# Find the lowest band that contain the information that you are interested in.-----------------------------------------------------------------------------------------------
datafile=datapath+'1'+'.dat'
i=1
Enkmax = np.loadtxt(datafile)[:,1].max()
while (Enkmax < Emin) :
    i=i+1
    datafile=datapath+str(i)+'.dat'
    Enkmax = np.loadtxt(datafile)[:,1].max()

nbndmin=i


# Find the highest band that contain the information that you are interested in.----------------------------------------------------------------------------------------------
i=nbnd
datafile=datapath+str(i)+'.dat'
Enkmin = np.loadtxt(datafile)[:,1].min()
while (Enkmin > Emax) :
    i=i-1
    datafile=datapath+str(i)+'.dat'
    Enkmin = np.loadtxt(datafile)[:,1].min()

nbndmax=i
numofbands=nbndmax-nbndmin+1
print('You are interst in '+str(numofbands)+' bands\n'+'The band is from '+str(nbndmin)+' to '+str(nbndmax) )
