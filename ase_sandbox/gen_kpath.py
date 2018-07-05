from ase.dft.kpoints import *
from ase.units import Bohr
import sys

def gen_kpath( atoms, lattice, Nkpt=60 ):
    """
    Automatically generate k-points for a band structure calculation.
    This relies on two dictionaries:
    - `special_points[lattice]`
    - `special_paths[lattice]`
    Reading up the source for the ase-3.16.2, common keys for `lattice` are
    - `cubic`
    - `fcc`
    - `bcc`
    - `tetragonal`
    - `orthorhombic`
    - `hexagonal`
    Currently missing: `monoclinic` and `rhombohedral`
    
    TODO: Probably need to make use of function `get_special_points(cell)`
    """
    #
    #points = special_points[lattice] #XXX change to get_special_points
    points = get_special_points( atoms.get_cell(), lattice=lattice )
    #
    paths = parse_path_string(special_paths[lattice])
    Nsegment = len(paths)
    #
    print("paths = ", paths)
    #
    KPT = []
    X = []
    XKPT = []
    KPT_SPEC = []
    #
    for isegment in range(Nsegment):
        #print(paths)
        kpt_spec = [points[k] for k in paths[isegment]]
        #
        kpt, x, Xkpt = get_bandpath(kpt_spec,atoms.cell,npoints=Nkpt)
        #
        KPT.append(kpt)
        X.append(x)
        XKPT.append(Xkpt)
        KPT_SPEC.append(kpt_spec)
    #
    return KPT, X, XKPT, paths, KPT_SPEC


