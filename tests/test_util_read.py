from __future__ import print_function
import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import *

force = read_pwscf_force('ex_LOG/LOG_relax')
print(force)

ene = read_pwscf_energy('ex_LOG/LOG_relax')
print('%f eV' % (ene))
