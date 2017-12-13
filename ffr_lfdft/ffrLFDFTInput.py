import numpy as np
import sys

class ffrLFDFTInput:


    def __init__(self):
        pass

    def write(self):
        pass


class ControlNameList:

    def __init__(self):
        self.pseudo_dir = './'
        self.etot_conv_thr = 1.e-6
    
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



class SystemNameList:

    def __init__(self, atoms):
        self.ibrav = 8
        #
        if any(atoms.pbc):
            self.A = 10.0
            self.B = 10.0
            self.C = 10.0
        else:
            self.A = 10.0
            self.B = 10.0
            self.C = 10.0
        self.nat = len(atoms)

        self.ntyp = len( np.unique( atoms.get_atomic_numbers() ) )

        self.nr1 = 45
        self.nr2 = 45
        self.nr3 = 45

        if not any(atoms.pbc):
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


class ElectronsNameList:

    def __init__(self):
        self.KS_Solve = 'Emin_pcg'
        self.cg_beta = 'PR'
        self.electron_maxstep = 150
        self.mixing_beta = 0.1
        self.diagonalization = 'LOBPCG'
        self.conv_thr = None
        self.mixing_mode = None
        self.startingwfc = None
        self.ortho_check_after_diag = None
        self.poisson_solver = None

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

