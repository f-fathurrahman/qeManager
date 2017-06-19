from ase.dft.kpoints import *
from ase.units import Bohr
import sys

def gen_kpath( atoms, lattice, Nkpts=60 ):
    #
    if lattice=='fcc':
        points = ibz_points[lattice]
        G = points['Gamma']
        X = points['X']
        W = points['W']
        K = points['K']
        L = points['L']
        kpts, x, Xkpt = get_bandpath([W, L, G, X, W, K], atoms.cell, npoints=Nkpts)
    #
    elif lattice=='hexagonal':
        points = ibz_points[lattice]
        G = points['Gamma']
        M = points['M']
        K = points['K']
        A = points['A']
        L = points['L']
        kpts, x, Xkpt = get_bandpath([G, M, K, G, A, L], atoms.cell, npoints=Nkpts)
    #
    elif lattice=='tetragonal':
        points = ibz_points[lattice]
        G = points['G']
        M = points['M']
        Z = points['Z']
        X = points['X']
        A = points['A']
        R = points['R']
        kpts, x, Xkpt = get_bandpath([G, Z, A, M, G, X, R], atoms.cell, npoints=NKPT)
    else:
        raise RuntimeError('Unknown lattice: %s' % lattice)
    #
    return kpts, x, Xkpt
