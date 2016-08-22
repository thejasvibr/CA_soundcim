# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:54:07 2016

@author: tbeleyur
"""


rows=3
cols=3
timesteps=4

totalcells=rows*cols

P_simspace=np.zeros([rows,cols,timesteps]) # create the numpy array which will store the values


# initiate the source of the sound :

soundsource=4
v_source=np.array([0.3,0.3,0.3,0.3])

cell_list=[SOUNDCELL() for i in range(rows*cols)] # initiating a whole bunch of empty soundcells

for i in range(totalcells):
    cell_list[i].P=0
    cell_list[i].Va=np.array([0,0,0,0])


cell_list[soundsource].Va=v_source # attributing the source to the central cell
cell_list[soundsource].P=3


def neighbours(cellpos,rows,cols):
    ''' function which calculates the neighbouring cells of a given cell''' 
    
