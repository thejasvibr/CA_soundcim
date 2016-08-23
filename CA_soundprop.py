# script to test out the CA simulation of sound propagation:

import numpy as np
import math as m

class SOUNDCELL : 
    '''class which stores and updates pressure and velocity values in each cell''' 
    
    def __init__(self):
        
        self.d=0.001 # absorption factor - needs to be changed according the specific frequency being studied
        self.Va_prime=np.zeros([1,4])
        
    def V_P_update(self,P_nbr):
        ''' function which updates the pressure and velocity values of each cell
        all equations are numbered according to :
        Komatsuzaki,T., Iwata,Y., Morishita,S., 2012, Modelling of incident sound wave propagation
        around sound barriers using cellular automata         
        '''
        # Pressures of the neighbours                
        self.P_nbr=P_nbr        
        # vprime at t+1 for each direction        
        #self.Va_prime=np.array( [ self.Va[dirn] - ( self.P_nbr[dirn] - self.P) for dirn in range(4)  ] )
        
        self.Va_prime=self.Va- (self.P_nbr - self.P) # eqn 1 
        
        # velocity in all the directions 
        #self.Va = np.array([ (1-self.d)*self.Va_prime[dirn] for dirn in range(4) ] )
        self.Va= (1-self.d)*self.Va_prime # eqn 2 
        
        #Pressure of the cell        
        # here I'm using 0.5 instead of (1/sqrt(2))**2 - to avoid rounding off errors! 
        
        # just choose the indices which are not nans!        
        self.P = self.P - 0.5* np.sum(self.Va[np.isfinite(self.Va)]) # eqn 3
        
    
        


def neighbours(cellpos,rows,cols):
    
    ''' function which calculates the von Neumann neighbour of a given cell
    inputs: 1x2 np.array with index numbers of the focal cell, number of rows,number of columns
    outputs: 4x2 np,array with neighbours. when no numbers are present then one/both columns have nan's''' 
    # N , E, S, W neighbours:
    
    nbr=np.array([cellpos+np.array([-1.0,0.0])   ,cellpos+np.array([0.0,1.0]), cellpos+np.array([1.0,0.0]), cellpos+np.array([0.0,-1.0]) ])
    
    # now check which of these nbrs are invalid :
    # 1) checks for cells that are on the west and north of valid boundary
    # 2) checks for cells that are south of valid boundary
    # 3) checks for cells that are east of valid  boundary
    nbrcheck=[ [nbr<0]  , [nbr>(rows-1)] , [nbr>(cols-1)] ]
    
    # check which kind of neighbour is in error: 
    boolcheck=np.where(np.array([np.sum(SubList) for SubList in nbrcheck]  ) >0 )
    
    # convert the tuple into an iterable list     
    list_boolcheck=map(list,boolcheck)[0]
     
    #now correct this by replacing the particular cell neighbour by NAN
    
    for b in list_boolcheck:
        nbr[ nbrcheck[b] ]= np.nan;
     

    #just convert both i & j inputs to nan
    nbr[np.isnan(nbr[:,0]*nbr[:,1]),:]=np.nan
     
    return(nbr)
    

def P_nbrget(P_mat,nbrs):
    '''function which extracts the Pressure values of the valid neighbours '''
    validindxs=np.isfinite(nbrs[:,0]) # look at the directions at which valid neighbours exist
    p_nbrs=np.zeros([4,1])
    p_nbrs[-validindxs]=np.nan
    for vd_ind in list(np.where(validindxs))[0]:    
        
        p_nbrs[vd_ind]= P_mat[nbrs[vd_ind][0],nbrs[vd_ind][1] ]
    
    return(p_nbrs)
    
         
    
    
    
    
    