from __future__ import print_function

import ase.io

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/qeManager/')
from utils_wizard import *
from PWSCFInput import *

working_dir = get_working_directory()
print(working_dir)

atoms = setup_atoms_molecules()

pspFiles = setup_pseudopotentials(atoms)
print(pspFiles)


pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT')

pwinput.CONTROL.pseudo_dir = './pspots'
pwinput.write()
