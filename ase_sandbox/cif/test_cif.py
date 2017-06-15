from __future__ import print_function

import sys
import ase.io

arg = sys.argv[1]
print(arg)
atoms = ase.io.read(arg)

outxsf = arg.replace('.cif','.xsf')
atoms.write(outxsf)
