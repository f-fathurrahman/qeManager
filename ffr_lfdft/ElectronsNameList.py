import sys

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
        f.write('&ELECTRONS\n')
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
