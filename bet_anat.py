#!/usr/bin/env python
 
 
import glob
import os
 
  
path = '/Users/Phili/Documents/Abschlussarbeit_Seminar_Datenanalyse/Aufgabe_1/Datensatz/'
 
anatfiles = glob.glob('%s/sub-*/anat/sub-*_T1w.nii.gz'%(path))
 
for file in anatfiles:
    print file
    output = file[:-7]
    os.system("bet %s %s_brain.nii.gz -R -m"%(file,output))
 
 
