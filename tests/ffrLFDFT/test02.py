from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io
import numpy as np

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')

from qeManager.ffr_lfdft import ffrLFDFTInput

from ase.build import molecule
atoms = molecule('NH3')
# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

pspFiles = ['H-q1.gth', 'N-q5.gth']
input = ffrLFDFTInput(atoms, pspFiles=pspFiles, filename='INPUT')
input.write()