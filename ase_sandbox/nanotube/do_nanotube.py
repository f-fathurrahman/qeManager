from ase.build import nanotube

# nanotube(n, m, length=1, bond=1.42, symbol='C', verbose=False, vacuum=None)
atoms = nanotube(3,3, bond=1.42, symbol='C', verbose=True, vacuum=10.0)
atoms.set_pbc([True,True,True])
atoms.write('CNT.xsf')
