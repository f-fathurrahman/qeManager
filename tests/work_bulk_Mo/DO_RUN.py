from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
from ase.build import bulk

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import ConvergenceTest
from qeManager.pwscf import *

atoms = bulk('Mo', cubic=True, a=6.0*Bohr)

pspFiles = ['Mo.pbe-spn-kjpaw_psl.0.3.0.UPF']

pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT',
            move_atoms=False, kpt_automatic=True )
pwinput.CONTROL.pseudo_dir = '/home/efefer/pseudo'
pwinput.CONTROL.disk_io = 'none'
pwinput.SYSTEM.nosym = False
pwinput.set_smearing()

klist = []
for i in range(2,20):
    klist.append( np.ones(3,dtype=np.int8)*i )
conv_test = ConvergenceTest( pwinput, what='kpoints', values=klist )

#conv_test.run()
ecutrho, energies, forces = conv_test.read()

Ndata = len(ecutrho)
Eref = energies[-1]  # take the most converged data (the last one) as the reference

print('\nConvergence in total energy:')
for i in range(Ndata):
    print("%10.5f %18.10f %18.10f" % (klist[i][0], energies[i], energies[i]-Eref))

print('\nConvergence in total force:')
for i in range(Ndata):
    totForces = np.sum(np.abs(forces[i]))/len(atoms)
    print("%10.5f %18.10f" % (klist[i][0], totForces))


