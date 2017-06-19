from ase.units import Bohr
from ase import Atom
import numpy as np

import sys

def write_kpoints(f=None, kpts=None, weights=None,
                  Nk=[1,1,1], nkshift=[0,0,0],
                  gamma_only=False,
                  automatic=False):
    if gamma_only:
        f.write('K_POINTS gamma\n')
        f.write('\n')
    elif automatic:
        f.write('K_POINTS automatic\n')
        f.write('%d %d %d %d %d %d\n\n' % (Nk[0], Nk[1], Nk[2],
                 nkshift[0], nkshift[1], nkshift[2]))
    else:
        f.write('K_POINTS')
        Nkpts = kpts.shape[0]
        for ik in Nkpts:
            f.write('%.9f %.9f %.9f %.9f\n' % (kpts[0,ik],kpts[1,ik],kpts[2,ik]))


def write_atomic_species(atoms, f=None, pspFiles=None, masses=None):
    if f==None:
        f = sys.stdout
    #
    unique_species = np.unique(atoms.get_chemical_symbols())

    f.write('ATOMIC_SPECIES\n')
    #
    if pspFiles is not None:
        isp = 0
        for s in unique_species:
            f.write('%5s %8.2f  %s\n' % (s, Atom(s).mass, pspFiles[isp]))
            isp = isp + 1
    else:
        raise RuntimeError('pspFiles needs to be specified')
    #
    f.write('\n')




def write_atomic_positions(atoms, f=None):
    if f == None:
        f = sys.stdout
    #
    f.write('ATOMIC_POSITIONS angstrom\n')
    for a in atoms:
        f.write('%5s %18.10f %18.10f %18.10f\n' %
                (a.symbol, a.position[0], a.position[1], a.position[2]))
    f.write('\n')

def write_cell(atoms,f=None):
    cell = atoms.get_cell()/Bohr # convert to Bohr
    if f == None:
        f = sys.stdout
    #
    f.write('CELL_PARAMETERS bohr\n')
    f.write('%18.10f %18.10f %18.10f\n' % (cell[0,0],cell[0,1],cell[0,2]) )
    f.write('%18.10f %18.10f %18.10f\n' % (cell[1,0],cell[1,1],cell[1,2]) )
    f.write('%18.10f %18.10f %18.10f\n' % (cell[2,0],cell[2,1],cell[2,2]) )
    f.write('\n')


def find_ntyp(atoms):
    """
    Return number of unique atom types (species)
    Not really needed, he he he :-)
    np.unique can be used instead
    """
    symbs = atoms.get_chemical_symbols()
    unique_symbols = []
    for s in symbs:
        if not (s in unique_symbols):
            unique_symbols.append(s)
    #
    return len(unique_symbols)
