#!/usr/bin/env python


import glob
import os


path = '/Users/Phili/Documents/Abschlussarbeit_Seminar_Datenanalyse/Aufgabe_1/Datensatz/'

boldfiles = glob.glob('%s/sub*/func/sub*_task-objectcategories_run*_bold.nii.gz' % (path))

for file in boldfiles:
    print file
    os.system("fslnvols %s" % (file))
