#!/bin/bash

#--------------------------------------------------------------+
# Program:                                                     |
#        to get rho(r) data from CHGCAR                        |
# History:                                                     |
# 2021/07/21     Zhefeng Lou                                   |
# Require:                                                     |
#        CHGCAR file                                           |
#--------------------------------------------------------------+

head -n 5 CHGCAR | tail -n 4 > lattice




nnum=`sed  -n '7p'  CHGCAR | awk '{print NF}'`
natoms=0
for ((i=1;i<=$nnum;i++));
	do
	nplus=`sed  -n '7p'  CHGCAR | awk "{print \$"$i"}" | sed 's/^[ \t]*//g'`
	((natoms=natoms+nplus))
done
((nlines=10+natoms))
sed  -n "${nlines}p"  CHGCAR > NGFS


# CHGCARclean file generate
((CHGCARbegin=11+natoms))
CHGCARend=`grep -n "augmentation occupancies" CHGCAR | awk -F "[:]" '{print $1}' | head -n 1`
((CHGCARend=CHGCARend-1))
((z=CHGCARend-CHGCARbegin+1))
head -n $CHGCARend CHGCAR | tail -n $z > CHGCARclean
echo -e "The lattice file contain the lattice parameters. The CHGCARclean file only contain the density data very convient for other program to deal with. The NGFS file is NGXF NGYF NGZF"
 #---------------------------------------------------------
