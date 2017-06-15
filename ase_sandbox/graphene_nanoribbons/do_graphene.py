from __future__ import print_function

from ase.build import graphene_nanoribbon

"""
type armchair, zigzag
ase.build.graphene_nanoribbon(n, m, type='zigzag',
       saturated=False, C_H=1.09, C_C=1.42,
       vacuum=None, magnetic=None, initial_mag=1.12,
       sheet=False, main_element='C', saturate_element='H')
"""

atoms = graphene_nanoribbon( 2, 2, sheet=True, type='armchair')
atoms.set_pbc([True,True,True])
atoms.write('orig.xyz')
atoms.write('orig.xsf')


# setup the cell
cell = atoms.get_cell()
print('original:')
print(cell)
zz = cell[2,2]
cell[1,1] = zz
cell[2,2] = 10.0
atoms.set_cell(cell)

# setup coords
pos = atoms.positions
print(pos)
zz = pos[:,2]
print(zz)
pos[:,1] = zz
pos[:,2] = 0.0
print(pos)
atoms.set_positions(pos)

atoms.write('graphene.xsf')
