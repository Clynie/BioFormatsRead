# -*- coding: utf-8 -*-
"""
@author: Sebi

File: showZsurface.py
Date: 01.06.2017
Version. 0.3
"""

import bftools as bf
import dispZsurface as dsp
import matplotlib.pyplot as plt
import argparse
import sys
import os

# setup commandline parameters
parser = argparse.ArgumentParser(description='Read Filename and Parameters.')
parser.add_argument('-file', action="store", dest='filename')
parser.add_argument('-csv', action="store", dest='writecsv')
parser.add_argument('-sep', action="store", dest='separator')
parser.add_argument('-save', action="store", dest='savefigure')
parser.add_argument('-show', action="store", dest='showsurface')
parser.add_argument('-format', action="store", dest='saveformat')

# get the arguments
args = parser.parse_args()

# get the filename
filenameczi = args.filename
saveformat = args.saveformat

# get separator
separator = args.separator
if args.separator == 'tab':
    separator = '\t'
elif args.separator == 'comma':
    separator = ','
elif args.sparator == 'semicolon':
    separator = ';'

# get CSV write option
if args.writecsv == 'True':
    wcsv = True
elif args.writecsv == 'False':
    wcsv = False

# get save option
if args.savefigure == 'True':
    save = True
elif args.savefigure == 'False':
    save = False

# get show surface options
if args.showsurface == 'True':
    surface = True
elif args.showsurface == 'False':
    surface = False

# specify bioformats_package.jar to use if required
# Attention: for larger CZI tile images containing an image pyramid one must still use 5.1.10
# since the latest version is not fully supported by python-bioformats yet
#bfpackage = r'bfpackage/5.1.10/bioformats_package.jar'
bfpackage = r'c:\Users\m1srh\Documents\Software\Bioformats\5.1.10\bioformats_package.jar'
bf.set_bfpath(bfpackage)

# create plane info from CZI image file and write CSV file (optional)
planetable, filenamecsv = bf.get_planetable(filenameczi, writecsv=wcsv, separator=separator)

# show the dataframe
print(planetable[:10])

# define name for figure to be saved
figuresavename = os.path.splitext(filenamecsv)[0] + '_XYZ-Pos' + '.' + saveformat

# display the XYZ positions
fig1, fig2 = dsp.scatterplot(planetable, ImageID=0, T=0, CH=0, Z=0, size=250,
                savefigure=save, figsavename=figuresavename, showsurface=surface)

# show the plot
plt.show()
print('Exiting ...')
os._exit(42)
