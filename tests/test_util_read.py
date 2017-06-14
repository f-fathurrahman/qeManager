import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import *

#forces = read_pwscf_forces('LOG_opt')
#print(forces)

ene = read_pwscf_energy('LOG_opt')
print('%f eV' % (ene))
