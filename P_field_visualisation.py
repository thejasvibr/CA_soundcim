# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 00:44:36 2016

@author: tbeleyur
"""

# -- making 

import matplotlib.pyplot as plt

timestep=np.shape(P_simspace)[0]

for T in range(timestep):
    plt.imshow(P_simspace[T,:,:],vmin=-10,vmax=10.0) # for a 'proper' visualisation
    #plt.colorbar()   
    plt.pause(0.05)
    
