# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:08:08 2016

@author: tbeleyur
"""

''' Scripts to test the various functions ''' 
import sys


# location of the module :
scriptlocn='C:\\Users\\tbeleyur\\Google Drive\\Holger Goerlitz- IMPRS\PHD_2015\\projects and analyses\\CA_modelling_sound_prop'

sys.path.append ( scriptlocn ) # add the location of the module to the search path of python 
from CA_soundprop import neighbours  # import the one function from the module 




# script to test the neighbouring function 

print('\n middle cell with all neighbours \n')
neighbours(np.array([1,1]),3,3)

print(' SE cornercell: \n')
neighbours(np.array([2,2]),3,3)

print('E column cell: \n')
neighbours(np.array([1,2]),3,3)

print('N row cell: \n')
neighbours(np.array([0,1]),3,3)

# -- function working as expected - last tested on 23/8/2016