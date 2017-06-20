from ase.dft.kpoints import *
from ase.units import Bohr
import sys

def gen_kpath( atoms, lattice, Nkpts=60 ):
    """
    Automatically generate k-points for a band structure calculation.
    """
    #
    points = special_points[lattice]
    paths = parse_path_string(special_paths[lattice])
    print(paths[0])
    kpts_spec = [points[k] for k in paths[0]]
    kpts, x, Xkpt = get_bandpath(kpts_spec,atoms.cell)
    #
    # TODO: also return string for special k-points' symbol
    # probably using variable `paths`.
    return kpts, x, Xkpt
