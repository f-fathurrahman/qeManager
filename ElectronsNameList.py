import sys

class ElectronsNameList:
    """
    A class to represent ELECTRONS namelist in PWSCF input.
    """

    def __init__(self):
        self.electron_maxstep = 150
        self.conv_thr = 1e-6
        self.mixing_mode = 'plain'
        self.mixing_beta = 0.7
        self.mixing_ndim = 8
        self.diagonalization = 'david'
        self.scf_must_converge = None
        self.adaptive_thr = None
        self.conv_thr_init = None
        self.conv_thr_multi = None
        self.mixing_fixed_ns = None
        self.ortho_para = None
        self.diago_thr_init = None
        self.diago_cg_maxiter = None
        self.diago_david_ndim = None
        self.diago_full_acc = None
        self.efield = None
        self.efield_cart = None
        self.efield_phase = None
        self.startingpot = None
        self.startingwfc = None
        self.tqr = None

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
                else:
                    f.write('  %s = %s\n' % (k,sdict[k]))
        f.write('/\n\n')
