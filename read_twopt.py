#####################################################
#
# programm to read in the twopoint function data provided
#
# can be used as a starting point for the tutoral
# on extracting hadronic quantities
#
#####################################################


import numpy as np


def main():
    
    TT = 96 # time extend of the lattice
    num_conf = 100 #number of configurations
    
    
    twopt_conf = [[0 for conf in range(num_conf)] for t in range(TT)]
    
    ##################################################
    #
    # read in the files
    #
    ##################################################
    print("reading in the twopt functions for each configuration\n")
    
    for conf in range(num_conf):
        filename='data/pion_g5-g5.%s.dat' %(conf)
        t_read, twopt_read = np.loadtxt(filename, unpack=True)
        for t in range(TT):
            twopt_conf[t][conf] = twopt_read[t]
            
main()
