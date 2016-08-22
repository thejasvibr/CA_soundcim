# script to test out the CA simulation of sound propagation:

import numpy as np
import math as m

# CA modelling of sound propagation
"""
this is a prototype to see how things work :
"""

'''inputs of cellupdate: i,j position of the focal cell 
#outputs of cellupdate: a 1x5 nparray with 0:3 columns having velocity components in 
# N,E,S,W directions, and [4] having the Pressure at the next time step.'''


class SOUNDCELL : 
    
    def __init__(self):
        
        
        
        self.d=0.001
        
        
        
        
        
        
    def V_P_update(self,P_nbr):
        ''' function which updates the pressure and velocity values of each cell'''
        # Pressures of the neighbours                
        self.P_nbr=P_nbr
        
        # vprime at t+1 for each direction        
        self.Va_prime= [ self.Va[dirn] - ( self.P_nbr[dirn] - self.P) for dirn in range(4)  ] 
        
        # velocity in all the directions 
        self.Va = [ (1-self.d)*self.Va_prime[dirn] for dirn in range(4) ] 
        
        #Pressure of the cell 
        
                        # here I'm using 2 instead of sqrt(2)**2 - to avoid rounding off errors! 
        self.P = self.P - 2*np.sum(self.Va)
        
        
    
    
         
    
    
    
    
    