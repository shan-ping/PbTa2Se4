#!/bin/bash

#--------------------------------------------------------------+
# Program:                                                     |
#        to get separate the data generate by line             |
# History:                                                     |
# 2021/07/27     Zhefeng Lou                                   |
# Require:                                                     |
#                                                              |
#--------------------------------------------------------------+
mkdir separate
echo "the file of data to separate:"
read filename
echo "How to separate? the separator(it is very important, before the first datas the file should have the separator, the file should not have the separator after the last data):"
read separator
nbands=`grep  "$separator"  $filename | awk '{print NR}' | tail -n 1`
grep -n "$separator"  $filename | awk -F "[:]" '{print $1}' > linenums
((nnum=nbands-1))
echo "$nbands datafiles"
# now separate the bands
for ((i=1;i<=$nnum;i++));
	do
	bandN=`sed  -n "${i}p"  linenums | sed 's/^[ \t]*//g'`
	((k=i+1))
	bandNA=`sed  -n "${k}p"  linenums | sed 's/^[ \t]*//g'`
	((bandNA=bandNA-1))
	((dband=bandNA-bandN))
	head -n $bandNA $filename | tail -n $dband | sed '/^ *$/d' > ./separate/${i}.dat
done
totline=`awk 'END{print NR}' $filename`
((dband=totline-bandNA-1))
tail -n $dband $filename > ./separate/${nbands}.dat
rm linenums
echo "job done"

 #---------------------------------------------------------
