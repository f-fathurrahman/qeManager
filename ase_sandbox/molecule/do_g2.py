from __future__ import print_function

from ase.build import molecule

from ase.collections import g2

for m in g2.names:
    print(m)
    atoms = molecule(m)
    atoms.write(m + '.xyz')
