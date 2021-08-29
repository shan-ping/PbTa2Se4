#!/usr/bin/env python3
# should use cat_band_interestedin.sh to get the band you interested in and this script should have the separate band data to support us.
# The separate fold should in the diractory and contain the band information it is used for us to get the kpath to form the band data
# Also this script need the Fermi energy you can get it from the output of vaspkit FERMI_ENERGY or DOSCAR(OUTCAR)(from scf calculation) 
# Mind this script is used for max double degenerated band
# workflow : 1 open the file 2. get the data 3. if the '+' in the line  
import numpy as np
import os

# get the neaded information -----------------------------------------------------------------------------------------------------------------------------------------------

minbd = int(input('The number of bands \nThe minband:\n'))
maxbd = int(input('The maxband:\n'))
EF = float(input('E-fermi:\n'))

# mkdir------------------------------------------------------------------------------------------------------------------------------------------------------- 
os.system('rm -r symnodes1')
os.system('mkdir symnodes1')
os.system('rm -r symnodesdataonly')
os.system('mkdir symnodesdataonly')


# get the nodes------------------------------------------------------------------------------------------------------------------------------------------------------- 
for i in range(minbd,maxbd+1,1):
    strB='0'
    str1=str(i)+'  2 '
    j=0  
    for line in open('./outir'):
        if 'k =' in line:
            linenode=line.strip().split('=')[1]
        if (str1 in line) and not('knum =' in line) and not('Table' in line):
            energy=float(line.strip().split()[2])-EF
            strG=line.strip().split('=')[1].strip()
            strE=("%.6f" % energy)
            f=open('./symnodes1/'+'nodes'+str(i)+'sym.dat','a+')
            f.writelines(linenode.replace("-", " -")+'   '+strE+'   '+strG+'\n')
            f.close()
            f=open('./symnodesdataonly/'+'nodes'+str(i)+'sym.dat','a+')
            f.writelines(linenode.replace("-", " -")+'\n')
            f.close()

print("job done")
