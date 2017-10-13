from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

import numpy as np

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')

from qeManager.pwscf import *

from ase.build import molecule
atoms = molecule('NH3')

# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

pspFiles = ['H.q1.gth', 'N.q5.gth']

# Build PWSCF input using `PWSCFInput` class
pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT', move_atoms=True, gamma_only=True)
# Set several variables manually
pwinput.CONTROL.pseudo_dir = 'GTH_PBE_2015'
pwinput.CONTROL.calculation = 'relax'
pwinput.IONS.ion_dynamics = 'bfgs'

pwinput.write()
