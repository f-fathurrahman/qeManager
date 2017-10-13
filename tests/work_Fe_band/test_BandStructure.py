from __future__ import print_function
from ase.build import bulk

import os

import sys
sys.path.append('/home/efefer/WORKS/my_github_repos/')
from qeManager import *

atoms = bulk('Fe')

pspFiles = ['Fe.pbe-spn-kjpaw_psl.0.2.1.UPF']

pwinput = PWSCFInput(atoms, pspFiles, filename='PWINPUT',
            kpt_automatic=True, Nk=[8,8,8])


pwinput.filename = 'PWINPUT_scf'
pwinput.CONTROL.pseudo_dir = '/home/efefer/pseudo'
pwinput.set_smearing()
pwinput.write()
#os.system('pw.x < PWINPUT_scf > LOG_scf')

pwinput.set_calc_bands('fcc',Nkpts=100)
pwinput.filename = 'PWINPUT_bands'
pwinput.write()
#os.system('pw.x < PWINPUT_bands > LOG_bands')


xcoords = pwinput.bands_xcoords
ebands = read_bandstructure('LOG_bands')

#Emin = np.max(ebands)
#Emax = np.max(ebands)

Emin = 5
Emax = 25

Nkpts = len(xcoords)
Nbands = ebands.shape[0]
print("Nbands = ", Nbands)
import matplotlib.pyplot as plt
plt.clf()
for ib in range(Nbands):
    plt.plot( xcoords, ebands[ib,:], marker='o' )

plt.grid()
plt.ylim(Emin,Emax)

specialk_xcoords = pwinput.specialk_xcoords

for p in specialk_xcoords:
  plt.plot([p, p], [Emin, Emax], 'k-')


plt.savefig('bands.png', dpi=300)
