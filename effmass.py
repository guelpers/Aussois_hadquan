"""

functions to calculate the effective mass of a twopoint function

coshmass(two_pt,TT) and coshmass_2(two_pt,TT)

both take as an argument the two-point function as an array in time and 
the time extend of the lattice.  

Functions return the effective mass as an array in time

"""

import numpy as np
import scipy.optimize as optimization





################################################
# coshmass for two_pt. TT is time extend of lattice
#
# meff = acosh ((C(t-1)+C(t+1))/(2C(t)))
################################################
def coshmass(two_pt,TT):
    meff = [0 for i in range(int(TT/2))]
    for t in range(1,int(TT/2-1)):
        meff[t] = (two_pt[t-1]+two_pt[t+1])/(2*two_pt[t])
        meff[t] = np.arccosh(meff[t])
    return meff



###############################################
# coshmass to solve for m with C(t)/C(t+1)
###############################################
def f_coshmass(x, ct, ct1, t, t1, TT):
	return ct/ct1 - np.cosh(x*(t-TT/2))/np.cosh(x*(t1-TT/2))
def coshmass_2(two_pt,TT):
    meff = [0 for i in range(int(TT/2))]
    for t in range(1,int(TT/2-1)):
        dump = optimization.fsolve(f_coshmass, 0.2, args=(two_pt[t],two_pt[t+1],t,t+1,TT), full_output=0)
        meff[t]=dump[0]
    return meff
