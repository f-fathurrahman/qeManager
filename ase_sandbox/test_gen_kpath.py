from __future__ import print_function

import sys
from math import pi

from ase import Atom, Atoms
import numpy as np

from gen_kpath import *
from gen_lattice_pwscf import *

"""
atoms = bulk('Zn')

kpts, x, Xkpt = gen_kpath(atoms,lattice='hexagonal')

Nkpts = len(x)
for ik in range(Nkpts):
    sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
print(Xkpt)
"""

def test_fcc():
    
    print("-----------")
    print("FCC lattice")
    print("-----------")
    
    atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
    atoms.set_cell( gen_lattice_fcc(5.0) )
    atoms.write("H_fcc.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice='fcc')
    #
    Nkpt = len(x)
    print(Nkpt)
    for ik in range(Nkpt):
        sys.stdout.write('%18.10f %18.10f %18.10f\n' % (kpt[ik,0],kpt[ik,1],kpt[ik,2]))
    #
    kpt_spec = np.array(kpt_spec)
    Nkpt_spec = len(path_str)
    print(Nkpt_spec)
    for ik in range(Nkpt_spec):
        sys.stdout.write("%18.10f %18.10f %18.10f %s\n" %
                        (kpt_spec[ik,0], kpt_spec[ik,1], kpt_spec[ik,2], path_str[ik]))

def test_sc():
    
    print("--------------------")
    print("Simple cubic lattice")
    print("--------------------")
    
    atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
    atoms.set_cell( gen_lattice_sc(5.0) )
    atoms.write("H_sc.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice="cubic")
    #
    Nkpt = len(x)
    print(Nkpt)
    for ik in range(Nkpt):
        sys.stdout.write("%18.10f %18.10f %18.10f\n" % (kpt[ik,0],kpt[ik,1],kpt[ik,2]))
    #
    kpt_spec = np.array(kpt_spec)
    Nkpt_spec = len(path_str)
    print(Nkpt_spec)
    for ik in range(Nkpt_spec):
        sys.stdout.write("%18.10f %18.10f %18.10f %s\n" %
                        (kpt_spec[ik,0], kpt_spec[ik,1], kpt_spec[ik,2], path_str[ik]))


test_sc()

test_fcc()



"""
kpts = kpoint_convert(atoms.get_cell(), ckpts_kv=kpts)
for ik in range(Nkpts):
    sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
"""
