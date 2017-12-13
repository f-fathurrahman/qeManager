from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io
import numpy as np

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')

from qeManager.ffr_lfdft import *

from ase.build import molecule

atoms = molecule('NH3')

# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

# Build PW input manually using `*NameList` classes.
# `ATOMIC_SPECIES` and `ATOMIC_POSITIONS` cards are written using
# several simple functions.

ctrl_NL = ControlNameList()
ctrl_NL.pseudo_dir = '../../pseudopotentials/pade_gth'
ctrl_NL.write_all()

sys_NL = SystemNameList(atoms)
sys_NL.write_all()

elec_NL = ElectronsNameList()
elec_NL.write_all()

"""
pspFiles = ['H.q1.gth', 'N.q5.gth']
write_atomic_species( atoms, pspFiles=pspFiles )
write_atomic_positions(atoms)
write_cell(atoms)
"""