from __future__ import print_function

from ase.build import bulk
# ase.build.bulk(name, crystalstructure=None, a=None, c=None, covera=None, u=None, orthorhombic=False, cubic=False)

atoms = bulk('Cu')
atoms.write('Cu.xsf')
