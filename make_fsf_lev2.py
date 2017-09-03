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
subdirs = glob.glob("%s/sub*" % (studydir))

# set this to the first entry of your subfiles to split it later
dir = subdirs[0]

for dir in list(subdirs):
    splitfile = dir.split('/')
    # YOU WILL NEED TO EDIT THIS TO GRAB sub001
    splitfile_sub = splitfile[7]
    subnum = splitfile_sub[-2:]
    print(subnum)
    replacements = {'SUBNUM': subnum}
    with open("%s/lev2/template_lev2.fsf" % (fsfdir)) as infile:
        with open("%s/lev2/design_sub%s_lev2.fsf" % (fsfdir, subnum), 'w') as outfile:
            for line in infile:
                # Note, since the video, I've changed "iteritems" to "items"
                # to make the following work on mpyore versions of python
                #  (python 3 no longer has iteritems())
                for src, target in replacements.items():
                    line = line.replace(src, target)
                outfile.write(line)
