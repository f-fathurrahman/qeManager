from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
from ase.build import bulk

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import *

atoms = bulk('Mo', cubic=True, a=6.0*Bohr)

pspFiles = ['Mo.pbe-spn-kjpaw_psl.0.3.0.UPF']

pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT',
            move_atoms=False, kpt_automatic=True, Nk=[4,4,4] )
pwinput.CONTROL.pseudo_dir = '/home/efefer/pseudo'
pwinput.CONTROL.disk_io = 'none'
pwinput.SYSTEM.nosym = True
pwinput.set_smearing()
pwinput.write()
