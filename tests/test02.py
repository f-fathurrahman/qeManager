from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

from PWSCFInput import *

atoms = ase.io.read('structures/NH3.xyz')

# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

pspFiles = ['H.q1.gth', 'N.q5.gth']

pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT', move_atoms=True)

pwinput.CONTROL.pseudo_dir = 'GTH_PBE_2015'
pwinput.CONTROL.calculation = 'relax'
pwinput.IONS.ion_dynamics = 'bfgs'

pwinput.write()
