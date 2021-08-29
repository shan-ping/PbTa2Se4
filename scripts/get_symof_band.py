#!/usr/bin/env python3
# should use cat_band_interestedin.sh to get the band you interested in and this script should have the separate band data to support us.
# The separate fold should in the diractory and contain the band information it is used for us to get the kpath to form the band data
# Also this script need the Fermi energy you can get it from the output of vaspkit FERMI_ENERGY or DOSCAR(OUTCAR)(from scf calculation) 
# Mind this script is used for max double degenerated band
# workflow : 1 open the file 2. get the data 3. if the '+' in the line  
import numpy as np
import os

#os.system('irvsp1 -sg '+symgroup+' > outir')
# get the neaded information -----------------------------------------------------------------------------------------------------------------------------------------------

minbd = int(input('The number of bands \nThe minband:\n'))
maxbd = int(input('The maxband:\n'))
EF = float(input('E-fermi:\n'))

# get the k-path data from ./separate/1.dat---------------------------------------------------------------------------------------------------------------------------------

kpoints = np.loadtxt('./separate/1.dat')[:,0]


# get the band neaded------------------------------------------------------------------------------------------------------------------------------------------------------- 
os.system('rm -r symnbGn')
os.system('rm -r symGn')
os.system('rm -r symnodes')
os.system('mkdir symnbGn')
os.system('mkdir symGn')
os.system('mkdir symnodes')
for i in range(minbd,maxbd+1,1):

#this part is very easy to get into trouble----------------------------------------------------------
    strB='0'
    str1=''
    str2=''
    for kl in range(0,3-len(str(i)),1):
        str1=' '+str1
    str1=str1+str(i)+'  '
    i1=i-1
    str2=str(i1)+'  2 '
    j=0  
    for line in open('./outir'):
        if 'k =' in line:
            linenode=line.strip().split('=')[1] 
        if (str2 in line or str1 in line) and not('knum =' in line) and not('Table' in line):
        #this part is very easy to get into trouble---------------------------------------------------
            k=kpoints[j]
            energy=float(line.strip().split()[2])-EF
            strG=line.strip().split('=')[1].strip()
            strE=("%.6f" % energy)
            strk=("%.5f" % k)
            if '+' in strG:
                strGN=strG.split('+')
                for strGi in strGN:
                    strGn=strGi.strip()
                    if (strG != strB) and (strGn !=strB):
                        f=open('./symnbGn/'+str(i)+strGn+'sym.dat','a+')
                        f.writelines('\n&\n')
                        f.close()
                        
                        f=open('./symGn/'+strGn+'sym.dat','a+')
                        f.writelines('\n&\n')
                        f.close()
                        
                        f=open('./symnodes/'+'nodes'+str(i)+'sym.dat','a+')
                        f.writelines(linenode.replace("-", " -")+'\n')
                        f.close()
                            
                    f=open('./symnbGn/'+str(i)+strGn+'sym.dat','a+')
                    f.writelines(strk+'   '+strE+'   '+strG+'\n')
                    f.close()
                    f=open('./symGn/'+strGn+'sym.dat','a+')
                    f.writelines(strk+'   '+strE+'   '+strG+'\n')
                    f.close()
            else:
                if not (strG in strB):
                    f=open('./symnbGn/'+str(i)+strG+'sym.dat','a+')
                    f.writelines('\n&\n')
                    f.close()
                    
                    f=open('./symGn/'+strG+'sym.dat','a+')
                    f.writelines('\n&\n')
                    f.close()
                    
                    f=open('./symnodes/'+'nodes'+str(i)+'sym.dat','a+')
                    f.writelines(linenode.replace("-", " -")+'\n')
                    f.close()
                            
                f=open('./symnbGn/'+str(i)+strG+'sym.dat','a+')
                f.writelines(strk+'   '+strE+'   '+strG+'\n')
                f.close()
                f=open('./symGn/'+strG+'sym.dat','a+')
                f.writelines(strk+'   '+strE+'   '+strG+'\n')
                f.close()
            
            strB=strG
            j=j+1

print("Job done, you can get the sym of different band in symnbGn and the formed band in symGn")
