from ase.dft.kpoints import *
from ase.units import Bohr
import sys

def gen_kpts( atoms, lattice, Nkpts=60 ):
    if lattice=='fcc':
        points = ibz_points['fcc']
        G = points['Gamma']
        X = points['X']
        W = points['W']
        K = points['K']
        L = points['L']
        kpts, x, Xkpt = get_bandpath([W, L, G, X, W, K], atoms.cell, npoints=Nkpts)
    else:
        raise RuntimeError('Unknown lattice: %s' % lattice)
    #
    return kpts, x, Xkpt
