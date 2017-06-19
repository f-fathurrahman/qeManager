import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import *

pwout = PWSCFOutput('ex_LOG/LOG_relax')
pwout.parse()
pwout.close()
