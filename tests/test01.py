from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

from ControlNameList import *
from SystemNameList import *
from ElectronsNameList import *
from IonsNameList import *
from utils import *

atoms = ase.io.read('structures/NH3.xyz')

# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

ctrl_NL = ControlNameList()
ctrl_NL.pseudo_dir = 'GTH_PBE_2015'
ctrl_NL.write_all()

sys_NL = SystemNameList(atoms)
sys_NL.write_all()

elec_NL = ElectronsNameList()
elec_NL.write_all()

ions_NL = IonsNameList()
ions_NL.ion_dynamics = 'bfgs'
ions_NL.write_all()

pspFiles = ['H.q1.gth', 'N.q5.gth']
write_atomic_species( atoms, pspFiles=pspFiles )

write_atomic_positions(atoms)

write_cell(atoms)
