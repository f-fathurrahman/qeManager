import numpy as np
from ase.dft.kpoints import *
from ase.units import Bohr

def gen_kpath( cell, lattice, Nkpts=60 ):
    """
    Automatically generate k-points for a band structure calculation.
    """
    #
    points = special_points[lattice]
    paths = parse_path_string(special_paths[lattice])
    print(paths[0])
    kpts_spec = [points[k] for k in paths[0]]
    kpts, x, Xkpt = get_bandpath(kpts_spec,cell)
    #
    # TODO: also return string for special k-points' symbol
    # probably using variable `paths`.
    return kpts, x, Xkpt


a = 5.0

kpts, x, Xkpt = gen_kpath( gen_fcc_cell(a), "fcc" )
Nkpts = len(x)
for ik in range(Nkpts):
    print("%15.8f %15.8f %15.8f %15.8f" % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
print(Xkpt)

kpts, x, Xkpt = gen_kpath( gen_cubic_cell(a), "cubic" )
Nkpts = len(x)
for ik in range(Nkpts):
    print("%15.8f %15.8f %15.8f %15.8f" % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
print(Xkpt)

print(get_special_points(gen_cubic_cell(a)))


