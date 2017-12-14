import numpy as np

import sys

class SystemNameList:

    def __init__(self, atoms):
        self.ibrav = 8
        #
        if all(atoms.pbc) == True:
            # XXX these values are in angstrom
            self.A = atoms.cell[0,0]
            self.B = atoms.cell[1,1]
            self.C = atoms.cell[2,2]
        elif all(atoms.pbc) == False:
            self.A = 10.0
            self.B = 10.0
            self.C = 10.0
        else:
            raise RuntimeError('Mixed periodic and isolated BC is not supported yet')
        #
        self.nat = len(atoms)

        self.ntyp = len( np.unique( atoms.get_atomic_numbers() ) )

        self.nr1 = 45
        self.nr2 = 45
        self.nr3 = 45

        if all(atoms.pbc) == False:
            self.assume_isolated = 'sinc'
        else:
            self.assume_isolated = 'none'

        self.input_dft = None  # use defaults
        self.Nstates_extra_ = None

    def write_all(self,f=None):
        if f == None:
            f = sys.stdout
        #
        f.write('&SYSTEM\n')
        sdict = self.__dict__
        for k in sdict:
            if not( sdict[k] == None ):
                if type(sdict[k]) == str:
                    f.write('  %s = \'%s\'\n' % (k,sdict[k]))
                elif type(sdict[k]) == list:
                    Nlist = len(sdict[k])
                    for i in range(Nlist):
                        f.write('  %s(%d) = %f\n' % (k,i+1,sdict[k][i]))
                else:
                    f.write('  %s = %s\n' % (k,sdict[k]))
        f.write('/\n\n')
