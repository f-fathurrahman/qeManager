#!/usr/bin/python
from __future__ import print_function
import sys
from ase.build import bulk
# ase.build.bulk(name, crystalstructure=None, a=None, c=None, covera=None, u=None, orthorhombic=False, cubic=False)

atomName = sys.argv[1]
atoms = bulk(atomName)
atoms.write(atomName + '.xsf')
