import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')

from qeManager.nwchem import *

from ase.build import molecule
atoms = molecule('NH3')

NWChemInput(atoms).write()
