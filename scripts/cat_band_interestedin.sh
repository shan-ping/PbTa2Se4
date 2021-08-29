#!/bin/bash

#--------------------------------------------------------------+
# Program:                                                     |
#        to form the band you are interested in                |
# History:                                                     |
# 2021/07/28     Zhefeng Lou                                   |
# Require:                                                     |
#        you shuold get the banddata from vaspkit              |
#--------------------------------------------------------------+

echo "the band data file:"
read datafile
separator="# Band-Index"
echo "The energy range you are interested in:"
echo "The Emin:"
read Emin
echo "The Emax:"
read Emax
echo "$datafile" > 1
echo "$separator" >> 1

#run data_separate_by_line.sh to separate bands
data_separate_by_line.sh < 1 > 2
rm 1
nband=`sed -n '3p' 2 | awk '{print $1}' | sed 's/^[ \t]*//g'`
echo "$nband" > 3
echo "$Emin" >> 3
echo "$Emax" >> 3
echo './separate/' >> 3

band_interested_in.py < 3 > 4

rm 2
head -n 2 $datafile > bandinterested.dat
bdmin=`sed -n '7p' 4 | awk '{print $5}' | sed 's/^[ \t]*//g'`
bdmax=`sed -n '7p' 4 | awk '{print $7}' | sed 's/^[ \t]*//g'`
for ((i=bdmin;i<=bdmax;i++));
	do
	echo "# Band-Index $i" >> bandinterested.dat
	cat ./separate/${i}.dat >> bandinterested.dat
	echo " " >> bandinterested.dat
	echo " " >> bandinterested.dat
done
rm 3 
rm 4
echo "The bandinterested.dat show the bands you are interested in.($bdmin to $bdmax)"


 #---------------------------------------------------------
