# An example of uing PWSCFOutput class
# FIXME This class does not have full functionality yet.

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager.pwscf import *

pwout = PWSCFOutput('ex_LOG/LOG_relax')
pwout.parse()
pwout.close()
