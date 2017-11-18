class NWChemInput:

    def __init__(self, atoms, basis='sto-3g', filename=None):
        self.atoms = atoms
        self.basis = basis
        #
        if filename == None:
            self.filename = 'INPUT.nw'
        else:
            self.filename = filename

    def write(self):
        f = open(self.filename,'w')
        f.write('start NWChemJob\n\n')
        self.write_atoms(f)
        self.write_basis(f)
        self.write_task(f)
        f.close()

    def write_atoms(self,f):
        f.write('GEOMETRY UNITS ANGSTROM\n')
        for a in self.atoms:
            f.write('%s %18.10f %18.10f %18.10f\n' %
                   (a.symbol, a.position[0], a.position[1], a.position[2]))
        f.write('END\n\n')

    def write_basis(self,f):
        f.write('BASIS\n')
        f.write('* library ' + self.basis + '\n')
        f.write('END\n\n')

    def write_task(self,f):
        f.write('task dft\n')
        f.write('\n\n')
