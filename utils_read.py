from __future__ import print_function
from ase.units import Bohr, Ry
import numpy as np
import sys

def read_pwscf_energy(logfile,last=True):
    """
    Read PWSCF energy
    """
    f = open(logfile,'r')
    energy = []
    while True:
        line = f.readline()
        if not line:
            break
        if('!    total energy' in line):
            sys.stdout.write(line)
            energy.append( float(line.split()[4]) )
    #
    f.close()
    #
    if last:
        return energy[-1]*Ry
    else:
        return energy*Ry


def read_pwscf_force(logfile,last=True):
    f = open(logfile,'r')
    all_force = []

    while True:
        line = f.readline()
        # break if EOF
        if not line:
            break
        # Read number of atoms
        if('number of atoms' in line):
            #print line
            Natoms = int( line.split()[4] )
        # Read force
        if('Forces acting' in line):
            line = f.readline()
            #
            force = np.zeros( (Natoms,3) )
            for ia in range(Natoms):
                line = f.readline()
                #print line
                force[ia,0] = float( line.split()[6] )
                force[ia,1] = float( line.split()[7] )
                force[ia,2] = float( line.split()[8] )
                #
                print()
                print(force*Ry/Bohr)
                all_force.append(force)
    #
    f.close()
    #
    if last:
        return all_force[-1]*(Ry/Bohr)
    else:
        return all_force*(Ry/Bohr)
