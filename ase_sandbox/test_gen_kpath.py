from __future__ import print_function

import sys
from math import pi

import ase.build
from ase import Atom, Atoms

import numpy as np

from gen_kpath import *
from gen_lattice_pwscf import *

"""
atoms = ase.build.bulk("Zn")

atoms.write("Zn.xsf")

kpts, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice='hexagonal')

Nkpts = len(x)
for ik in range(Nkpts):
    sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
print(Xkpt)

exit()
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


def test_bcc():
    
    print("-----------")
    print("BCC lattice")
    print("-----------")
    
    atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
    atoms.set_cell( gen_lattice_bcc(5.0) )
    atoms.write("H_bcc.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice='bcc')
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


def test_hexagonal():
    
    print("-----------------")
    print("Hexagonal lattice")
    print("-----------------")
    
    atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
    LatVecs = gen_lattice_hexagonal(5.0, 8.0)
    atoms.set_cell( LatVecs )
    #
    atoms.write("H_hexagonal.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice='hexagonal')
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


def test_orthorhombic():
    
    print("--------------------")
    print("Orthorhombic lattice")
    print("--------------------")
    
    atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
    LatVecs = gen_lattice_orthorhombic(5.0, 8.0, 6.0)
    atoms.set_cell( LatVecs )
    #
    atoms.write("H_orthorhombic.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice='orthorhombic')
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


def test_monoclinic():
    
    print("------------------")
    print("Monoclinic lattice")
    print("------------------")
    
    atoms = Atoms( [Atom("H", (0.0, 0.0, 0.0))], pbc=True )
    LatVecs = gen_lattice_monoclinic(5.0, 8.0, 6.0, 80.0)
    atoms.set_cell( LatVecs )
    #
    atoms.write("H_monoclinic.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice="monoclinic")
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


def test_tetragonal():
    
    print("------------------")
    print("Tetragonal lattice")
    print("------------------")
    
    atoms = Atoms( [Atom("H", (0.0, 0.0, 0.0))], pbc=True )
    LatVecs = gen_lattice_tetragonal_P(5.0, 6.0)
    atoms.set_cell( LatVecs )
    #
    atoms.write("H_tetragonal.xsf")
    #
    kpt, x, Xkpt, path_str, kpt_spec = gen_kpath(atoms,lattice="tetragonal")
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


def test_rhombohedral():
    
    print("--------------------")
    print("Rhombohedral lattice")
    print("--------------------")
    
    atoms = Atoms( [Atom("H", (0.0, 0.0, 0.0))], pbc=True )
    LatVecs = gen_lattice_rhombohedral(5.0, 80.0)
    atoms.set_cell( LatVecs )
    #
    atoms.write("H_rhombohedral.xsf")
    #
    KPT, X, XKPT, PATH_STR, KPT_SPEC = gen_kpath( 
            atoms,lattice="rhombohedral type 1") # gamma > 90 degree
    #
    Nsegment = len(PATH_STR)
    print("Nsegment = ", Nsegment)
    #
    for isegment in range(Nsegment):
        #
        x = X[isegment]
        kpt = KPT[isegment]
        path_str = PATH_STR[isegment]
        kpt_spec = KPT_SPEC[isegment]
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



test_rhombohedral()

#test_tetragonal()

#test_monoclinic()

#test_orthorhombic()

#test_hexagonal()

#test_bcc()

#test_sc()

#test_fcc()



"""
kpts = kpoint_convert(atoms.get_cell(), ckpts_kv=kpts)
for ik in range(Nkpts):
    sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
"""
