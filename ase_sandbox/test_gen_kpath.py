execfile('gen_kpath.py')

from ase.build import bulk
import sys

atoms = bulk('Cu')

kpts, x, Xkpt = gen_kpts(atoms,lattice='fcc')

Nkpts = len(x)
for ik in range(Nkpts):
    sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
print(Xkpt)
