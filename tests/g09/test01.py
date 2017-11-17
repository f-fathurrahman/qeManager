import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')

from qeManager.g09 import *

from ase.build import molecule
atoms = molecule('NH3')

G09Input(atoms).write()
