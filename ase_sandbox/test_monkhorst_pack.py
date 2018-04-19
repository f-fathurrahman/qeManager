from ase.dft.kpoints import monkhorst_pack

print("Using (3,3,3):")
kpts = monkhorst_pack((3,3,3))
Nkpts = len(kpts)
print("Nkpts = %d" % (Nkpts))
print(kpts)

print("")
print("Using (1,1,3):")
kpts = monkhorst_pack((1,1,3))
Nkpts = len(kpts)
print("Nkpts = %d" % (Nkpts))
print(kpts)

