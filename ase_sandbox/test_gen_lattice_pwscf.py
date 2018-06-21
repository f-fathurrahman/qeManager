from __future__ import print_function
from gen_lattice_pwscf import *

print("\nSimple cubic lattice")
print(gen_lattice_cubic(10.0))

print("\nFCC lattice")
print(gen_lattice_fcc(10.0))

print("\nBCC lattice")
print(gen_lattice_bcc(10.0))

print("\nBCC lattice v2")
print(gen_lattice_bcc_v2(10.0))

print("\nHexagonal lattice")
print(gen_lattice_hexagonal(10.0, 5.0))

print("\nTetragonal lattice P")
print(gen_lattice_tetragonal_P(10.0, 5.0))

print("\nTetragonal lattice I")
print(gen_lattice_tetragonal_I(10.0, 5.0))

print("\nOrthorhombic lattice")
print(gen_lattice_orthorhombic(10.0, 5.0, 8.0))
