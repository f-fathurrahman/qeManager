from ase.dft.kpoints import *
from ase.units import Bohr
import sys

# a slightly modified version
def my_bandpath(path, cell, npoints=50):
    """Make a list of kpoints defining the path between the given points.

    path: list or str
        Can be:

        * a string that parse_path_string() understands: 'GXL'
        * a list of BZ points: [(0, 0, 0), (0.5, 0, 0)]
        * or several lists of BZ points if the the path is not continuous.
    cell: 3x3
        Unit cell of the atoms.
    npoints: int
        Length of the output kpts list.

    Return list of k-points, list of x-coordinates and list of
    x-coordinates of special points."""

    if isinstance(path, basestring):
        special = get_special_points(cell)
        paths = []
        for names in parse_path_string(path):
            paths.append([special[name] for name in names])
    elif np.array(path[0]).ndim == 1:
        paths = [path]
    else:
        paths = path

    points = np.concatenate(paths)
    dists = points[1:] - points[:-1]

    #lengths = [np.linalg.norm(d) for d in kpoint_convert(cell, skpts_kc=dists)]
    lengths = [np.linalg.norm(d) for d in dists]

    i = 0
    for path in paths[:-1]:
        i += len(path)
        lengths[i - 1] = 0

    length = sum(lengths)
    kpts = []
    x0 = 0
    x = []
    X = [0]
    for P, d, L in zip(points[:-1], dists, lengths):
        n = max(2, int(round(L * (npoints - len(x)) / (length - x0))))

        for t in np.linspace(0, 1, n)[:-1]:
            kpts.append(P + t * d)
            x.append(x0 + t * L)
        x0 += L
        X.append(x0)
    kpts.append(points[-1])
    x.append(x0)

    return np.array(kpts), np.array(x), np.array(X)


def get_segment_length( kpt_spec, cell ):
    Nkpt = len(kpt_spec)
    kpt, x, Xkpt = my_bandpath( kpt_spec, cell, npoints=Nkpt )
    return x[Nkpt-1]

# use input delta_k to determine Nkpt ??
def gen_kpath( atoms, lattice, dk=0.05 ):
    """
    dk is given in scaled coordinate

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
    - `monoclinic`
    - `rhombohedral type 1`
    - `rhombohedral type 2`
    """
    #
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
        #
        kpt_spec = [points[k] for k in paths[isegment]]
        #
        L_segment = get_segment_length( kpt_spec, atoms.cell )
        print("isegment = ", isegment, ", L = ", L_segment)
        #
        Nkpt_L = int( L_segment/dk )
        print("Nkpt_L = ", Nkpt_L)
        #
        kpt, x, Xkpt = my_bandpath(kpt_spec,atoms.cell,npoints=Nkpt_L)
        #
        KPT.append(kpt)
        X.append(x)
        XKPT.append(Xkpt)
        KPT_SPEC.append(kpt_spec)
    #
    return KPT, X, XKPT, paths, KPT_SPEC


