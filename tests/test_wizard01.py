from __future__ import print_function

import sys
sys.path.append('../')

import ase.io

from utils_wizard import *

atoms = ase.io.read('structures/NH3.xyz')

working_dir = get_working_directory()
print(working_dir)

setup_pseudopotentials(atoms)
