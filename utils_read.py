from __future__ import print_function
from ase.units import Bohr, Ry
import numpy as np

def read_pwscf_energy(logfile):
    """
    XXX: Can result in forever loop !!!! Need to fix this
    """
    f = open(logfile,'r')
    line = f.readline()
    while not ('!    total energy' in line):
        line = f.readline()
    energy = float(line.split()[4])
    return energy*Ry


def read_pwscf_forces(logfile):
    f = open(logfile,'r')

    line = f.readline()
    while not ('number of atoms' in line):
        line = f.readline()

    #print line
    Natoms = int( line.split()[4] )

    while not ('Forces acting' in line):
        line = f.readline()
    line = f.readline()
    #
    forces = np.zeros( (Natoms,3) )
    for ia in range(Natoms):
        line = f.readline()
        #print line
        forces[ia,0] = float( line.split()[6] )
        forces[ia,1] = float( line.split()[7] )
        forces[ia,2] = float( line.split()[8] )
    f.close()
    return forces*(Ry/Bohr)
