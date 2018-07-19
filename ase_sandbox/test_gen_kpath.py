from __future__ import print_function

import sys
from math import pi

import ase.build
from ase import Atom, Atoms

import numpy as np

from gen_kpath import *
from gen_lattice_pwscf import *

def do_lattice(latt_name):

    if latt_name == "cubic":

        print("--------------------")
        print("Simple cubic lattice")
        print("--------------------")
    
        atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_sc(5.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_sc.xsf")

    elif latt_name == "fcc":

        print("-----------")
        print("FCC lattice")
        print("-----------")
    
        atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_fcc(5.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_fcc.xsf")

    elif latt_name == "bcc":

        print("-----------")
        print("BCC lattice")
        print("-----------")
    
        atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_bcc(5.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_bcc.xsf")

    elif latt_name == "hexagonal":

        print("-----------------")
        print("Hexagonal lattice")
        print("-----------------")
    
        atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_hexagonal(5.0, 8.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_hexagonal.xsf")
    
    elif latt_name == "tetragonal":

        print("------------------")
        print("Tetragonal lattice")
        print("------------------")
    
        atoms = Atoms( [Atom("H", (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_tetragonal_P(5.0, 6.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_tetragonal.xsf")

    elif latt_name == "orthorhombic":

        print("--------------------")
        print("Orthorhombic lattice")
        print("--------------------")
    
        atoms = Atoms( [Atom('H', (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_orthorhombic(5.0, 8.0, 6.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_orthorhombic.xsf")
    
    elif latt_name == "rhombohedral type 1":
    
        print("-----------------------------")
        print("Rhombohedral lattice (type 1)")
        print("-----------------------------")
    
        atoms = Atoms( [Atom("H", (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_rhombohedral(5.0, 80.0) # gamma < 90 degree
        atoms.set_cell( LatVecs )
        #
        atoms.write("H_rhombohedral.xsf")
        #
    elif latt_name == "monoclinic":

        print("------------------")
        print("Monoclinic lattice")
        print("------------------")
    
        atoms = Atoms( [Atom("H", (0.0, 0.0, 0.0))], pbc=True )
        LatVecs = gen_lattice_monoclinic(5.0, 8.0, 6.0, 80.0)
        atoms.set_cell( LatVecs )
        atoms.write("H_monoclinic.xsf")
    
    else:

        raise RuntimeError("Unknown lattice name:", lattice)

    
    KPT, X, XKPT, PATH_STR, KPT_SPEC = gen_kpath( 
            atoms,lattice=latt_name )

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
            sys.stdout.write("%18.10f %18.10f %18.10f: %18.10f\n" % (kpt[ik,0],kpt[ik,1],kpt[ik,2],x[ik]))
        #
        kpt_spec = np.array(kpt_spec)
        Nkpt_spec = len(path_str)
        print(Nkpt_spec)
        for ik in range(Nkpt_spec):
            sys.stdout.write("%18.10f %18.10f %18.10f %s\n" %
                            (kpt_spec[ik,0], kpt_spec[ik,1], kpt_spec[ik,2], path_str[ik]))


do_lattice("cubic")
do_lattice("fcc")
do_lattice("hexagonal")
do_lattice("rhombohedral type 1")

