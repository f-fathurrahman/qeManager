execfile('gen_kpath.py')

from ase.build import bulk
import sys

atoms = bulk('Zn')

kpts, x, Xkpt = gen_kpath(atoms,lattice='hexagonal')

Nkpts = len(x)
for ik in range(Nkpts):
    sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
print(Xkpt)
