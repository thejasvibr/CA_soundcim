# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:54:07 2016

@author: tbeleyur
"""

# location of the module :
scriptlocn='C:\\Users\\tbeleyur\\Google Drive\\Holger Goerlitz- IMPRS\PHD_2015\\projects and analyses\\CA_modelling_sound_prop'

sys.path.append ( scriptlocn ) # add the location of the module to the search path of python 
import CA_soundprop  # import the one function from the module 

#initialise the array and define the rows, columns and number of timesteps to run the simulation 
rows=3
cols=3
timesteps=3

totalcells=rows*cols

P_simspace=np.zeros([timesteps,rows,cols]) # create the numpy array which will store the values for each value over time 4

#create instances of the soundcells 
all_cells=[SOUNDCELL() for k in range(totalcells)] 

# assigning the neighbours for all the cells :
cell_nbrs=[neighbours(np.array([i,j]),rows,cols ) for i in range(rows) for j in range(cols)]
# all cells are numbered row-wise , as in 0,1,2,3; 4,5,6,7; 8,9,10,11 - eg. for a 3x4 space



# ----- initialise all of the cells with 0 pressure and 0 velocity vectors at the beginning :

for k in range(totalcells):
    all_cells[k].Va=np.zeros([4,1]) # have 0 Va's just at start 
    
    notvalidVas=np.isnan(cell_nbrs[k][:,0]) # finding which of the neighbours don't exist for each cell
    
    all_cells[k].Va[notvalidVas]=np.nan # the Va for directions with no neighbours
    all_cells[k].P=0 # also assigning the default value of 0
    
# ----------------creating the sound sources -----------:
    
# here the sound source is the middle one, this is a list of sources - when there are different sources 
source_ij=[ np.array([0,0]) ]
source_P=[np.array(10) ]

for src in range(len(source_ij)):
    
    P_simspace[0,source_ij[src][0],source_ij[src][1] ]=source_P[src] # assign pressure values to the sources @ timestep 0
    all_cells[ source_ij[src][0]*cols + source_ij[src][1]  ].P=source_P[src] # assigning instance values of pressure 

# ------------ running the simulations :

ijvals=[ [i,j] for i in range(rows) for j in range(cols) ]



for T in range(timesteps):
    
    for foc_cell in range(totalcells):      
        P_simspace[T,ijvals[foc_cell][0],ijvals[foc_cell][1] ] = all_cells[foc_cell].P
    
    print('\n TIMESTEP: %d \n' % T)
    
    for foc_cell in range(totalcells):
        
         print('\n PRE :focal cell number: %d'%foc_cell)
         print(all_cells[foc_cell].Va)
         print(all_cells[foc_cell].P)
         # making an np array of the Pressure values of the neighbours             
         P_Nbrs=P_nbrget(P_simspace[T,:,:],cell_nbrs[foc_cell])
         all_cells[foc_cell].V_P_update( P_Nbrs )
         print('\n focal cell number: %d'%foc_cell)
         print(all_cells[foc_cell].Va)
         print(all_cells[foc_cell].P)
         
    