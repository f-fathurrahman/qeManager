from __future__ import print_function

class G09Input:

    def __init__(self, atoms, basis='STO-3G',
                 charge=0, multiplicity=1,
                 theorylevel='B3LYP', filename=None,
                 chk='CHECKPOINT.chk'):
        #
        self.atoms = atoms
        self.basis = basis
        self.charge = charge
        self.multiplicity = multiplicity
        self.theorylevel = theorylevel
        self.chk = chk

        if filename == None:
            self.filename = 'INPUT.gjf'

        self.directives  = ''
        self.directives += '# P gfinput\n'
        self.directives += '# ' + self.theorylevel + '/' + self.basis + '\n'
        self.directives += '# IOP(6/7=3)\n'

        self.comments = 'Generated input file'


    def write(self):
        f = open(self.filename, 'w')
        #
        f.write('% chk=' + self.chk)
        f.write('\n')
        #
        f.write(self.directives)
        f.write('\n')   # only one newline is needed
        #
        f.write(self.comments)
        f.write('\n\n')
        #
        f.write('0 1')   # FIXME: charge and multiplicity
        f.write('\n')
        #
        for a in self.atoms:
            f.write('%s %18.10f %18.10f %18.10f\n' %
                   (a.symbol, a.position[0], a.position[1], a.position[2]))
        f.write('\n')
