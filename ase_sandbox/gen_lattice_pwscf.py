# Assumption: v1, v2, and v3 are given by row
import numpy as np
from math import sqrt

def gen_lattice_sc(a):
    cell = np.array( [[1,0,0], [0,1,0], [0,0,1]] )
    return a*cell

def gen_lattice_fcc(a):
    cell = np.array( [[-1,0,1], [0,1,1], [-1,1,0]] )
    return 0.5*a*cell

def gen_lattice_bcc(a): 
    #
    LL = np.zeros((3,3))
    LL[0,:] = 0.5*a*np.array([1,1,1])
    LL[1,:] = 0.5*a*np.array([-1,1,1])
    LL[2,:] = 0.5*a*np.array([-1,-1,1])
    return LL    

# more symmetric axis:
def gen_lattice_bcc_v2(a):
    #
    LL = np.zeros((3,3))
    LL[0,:] = 0.5*a*np.array([-1,1,1]) 
    LL[1,:] = 0.5*a*np.array([1,-1,1])
    LL[2,:] = 0.5*a*np.array([1,1,-1])
    return LL

# also for trigonal P
def gen_lattice_hexagonal(a,c):
    #
    LL = np.zeros((3,3))
    LL[0,:] = a*np.array([1,0,0])
    LL[1,:] = a*np.array([-1/2,sqrt(3)/2,0]) 
    LL[2,:] = np.array([0,0,c])
    return LL    

def gen_lattice_tetragonal_P(a,c):
    #
    LL = np.zeros((3,3))
    LL[0,:] = a*np.array([1,0,0])
    LL[1,:] = a*np.array([0,1,0])
    LL[2,:] = np.array([0,0,c])
    return LL


def gen_lattice_tetragonal_I(a, c):
    #
    LL = np.zeros((3,3))
    LL[0,:] = 0.5*np.array([a,-a,c])
    LL[1,:] = 0.5*np.array([a,a,c])
    LL[2,:] = 0.5*np.array([-a,-a,c])
    return LL

def gen_lattice_orthorhombic( a, b, c ):
    #
    LL = np.zeros((3,3))
    LL[0,:] = np.array([a,0,0]) 
    LL[1,:] = np.array([0,b,0])
    LL[2,:] = np.array([0,0,c])
    return LL

