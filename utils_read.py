from __future__ import print_function
from ase.units import Bohr, Ry
import numpy as np
import sys

def get_Nbands_Nkpts(logfile):
    f = open(logfile,'r')
    #
    while True:
        line = f.readline()
        if not line:
            break
        # Read number of bands
        if('number of Kohn-Sham states' in line):
            Nbands = int( line.split()[4] )
        # read number of k-points
        if('number of k points' in line):
            Nkpts = int( line.split()[4] )
    #
    return Nbands, Nkpts



def read_bandstructure(logfile):
    #
    Nbands, Nkpts = get_Nbands_Nkpts(logfile)
    #
    ebands = np.zeros((Nbands,Nkpts))
    #
    ENE_PER_LINE = 8
    #
    f = open(logfile,'r')
    #
    while True:
        line = f.readline()
        if not line:
            break
        #
        Nline = Nbands/ENE_PER_LINE
        Nextra = Nbands%ENE_PER_LINE
        #
        if('End of band structure calculation' in line):
            #ikpt = 0
            for ikpt in range(Nkpts):
                f.readline()
                f.readline()
                f.readline()
                ibnd = 0
                for i in range(Nline):
                    line = f.readline()
                    #print(line,end='')
                    for i in range(8):
                        ebands[ibnd,ikpt] = float(line.split()[i])
                        ibnd = ibnd + 1
                #
                if Nextra > 0:
                    line = f.readline()
                    #print(line,end='')
                    for i in range(Nextra):
                        ebands[ibnd,ikpt] = float(line.split()[i])
                        ibnd  = ibnd + 1
                #
                print(ebands[:,ikpt])


    print("Nkpts = ", Nkpts, " Nbands = ", Nbands)
    f.close()
    return ebands


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
