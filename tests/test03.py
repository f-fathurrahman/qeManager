import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager.pwscf import *

pwout = PWSCFOutput('ex_LOG/LOG_relax')
pwout.parse()
pwout.close()
