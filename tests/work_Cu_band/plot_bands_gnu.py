import numpy as np
import matplotlib.pyplot as plt
from ase.units import Ry

NBANDS   = 31
NKPOINTS = 60

databands = np.loadtxt('bands.out.gnu')

ebands = np.zeros( (NKPOINTS, NBANDS) )
kvec   = np.zeros( (NKPOINTS, NBANDS) )

for ib in range(NBANDS):
  idx1 = (ib)*NKPOINTS
  idx2 = (ib+1)*NKPOINTS
  ebands[:,ib] = databands[idx1:idx2,1]*Ry
  kvec[:,ib]   = databands[idx1:idx2,0]

Efermi = 10.3205 # in eV
ebands[:,:] = ebands[:,:] - Efermi

Emin = -25.0
Emax =  15.0

plt.figure(figsize=(5, 6))
plt.clf()
for ib in range(NBANDS):
  plt.plot( kvec[:,ib], ebands[:,ib], marker='o' )


Xkpt   = [0.0000, 0.7434, 1.4505, 2.1938, 2.9009, 3.4009, 4.1443]
labelX = ['$\Gamma$', 'Z', 'A', 'M', '$\Gamma$', 'X', 'R']

for p in Xkpt:
  plt.plot([p, p], [Emin, Emax], 'k-')
plt.xticks(Xkpt, labelX)

plt.plot([0, Xkpt[-1]], [0, 0], 'k--')

plt.ylim( Emin,Emax )
plt.xlim( 0, Xkpt[-1] )
plt.xlabel('k vector')
plt.ylabel('Energy (eV)')
plt.title('Band structure of SnO2')
plt.savefig('BANDSTR_v1.pdf')


