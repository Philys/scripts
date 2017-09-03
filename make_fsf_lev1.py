#!/usr/bin/python

# This script will generate each subjects design.fsf, but does not run it.
# It depends on your system how will launch feat

import glob

# Set this to the directory all of the sub### directories live in
studydir = '/Users/Phili/Documents/Abschlussarbeit_Seminar_Datenanalyse/Aufgabe_1/Datensatz'

# Set this to the directory where you'll dump all the fsf files
# May want to make it a separate directory, because you can delete them all o
#   once Feat runs
fsfdir = "%s/fsfs" % (studydir)

# Get all the paths!  Note, this won't do anything special to omit bad subjects
subfiles = glob.glob("%s/sub*/func/sub*_task-objectcategories_run*_bold.nii.gz" % (studydir))

# set this to the first entry of your subfiles to split it later
file = subfiles[0]

for file in list(subfiles):
    splitfile = file.split('/')
    # YOU WILL NEED TO EDIT THIS TO GRAB sub001
    splitfile_sub = splitfile[7]
    subnum = splitfile_sub[-2:]
    #  YOU WILL ALSO NEED TO EDIT THIS TO GRAB THE PART WITH THE RUNNUM
    splitfile_run = splitfile[9]
    runnum = splitfile_run[33:34]
    print(subnum)
    replacements = {'SUBNUM': subnum, 'RUNNUM': runnum}
    with open("%s/lev1/template_lev1.fsf" % (fsfdir)) as infile:
        with open("%s/lev1/design_sub%s_run%s.fsf" % (fsfdir, subnum, runnum), 'w') as outfile:
            for line in infile:
                # Note, since the video, I've changed "iteritems" to "items"
                # to make the following work on mpyore versions of python
                #  (python 3 no longer has iteritems())
                for src, target in replacements.items():
                    line = line.replace(src, target)
                outfile.write(line)
