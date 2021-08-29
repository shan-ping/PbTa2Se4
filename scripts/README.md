# PbTa2Se4
some scripts for the calculation of three phases
all the scripts only tested in ubuntu system and for our calculation, you may change it to fit your neads.

## cat_band_interestedin.sh is used for get the banddata of your interested in(energy range) from vaspkit output banddata.
it is based on band_interested_in.py and data_separate_by_line.sh, use these scripts also can help to get the bands cross the Fermi level

## get_symof_band.py get_symof_nodes.py used to deal with the output of irvasp 
the irvasp output should be outir. and this script will not be used in the structure that contain invertion symmetry. And you should run cat_band_interestedin.sh first to get the k path of a band to run get_symof_band.py, the nodes get from get_symof_band.py are the points the degenercy changed between the next k point.

## CHGCARdataseperate.sh is used to cat the data from the CHGCAR file 
the output are 1 lattice file(contain lattice parameters); 2 NGFS file(contain NG(X,Y,Z)F); 3 CHGCARclean file(contain the charge density in CHGCAR file)
## CHGD(z)get.ipynb is used to calculate the planar-averaged charge density
get the D(z) file
