from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import ConvergenceTest
from qeManager.pwscf import *

atoms = ase.io.read('../structures/NH3.xyz')

# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

pspFiles = ['H.q1.gth', 'N.q5.gth']

pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT', move_atoms=True, gamma_only=True)
pwinput.CONTROL.pseudo_dir = '../../GTH_PBE/'
conv_test = ConvergenceTest( pwinput, what='ecutwfc', values=np.arange(20.,100.,2.) )

conv_test.run()
ecutrho, energies, forces = conv_test.read()

Ndata = len(ecutrho)
Eref = energies[-1]  # take the most converged data (the last one) as the reference

print('\nConvergence in total energy:')
for i in range(Ndata):
    print("%10.5f %18.10f %18.10f" % (ecutrho[i], energies[i], energies[i]-Eref))

print('\nConvergence in total force:')
for i in range(Ndata):
    totForces = np.sum(np.abs(forces[i]))/len(atoms)
    print("%10.5f %18.10f" % (ecutrho[i], totForces))

