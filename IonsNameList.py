import sys

class IonsNameList:
    """
    A class to represent IONS namelist in PWSCF
    """

    def __init__(self):
         self.ion_dynamics = None
         self.ion_positions = None
         self.pot_extrapolation = None
         self.wfc_extrapolation = None
         self.remove_rigid_rot = None
         self.ion_temperature = None
         self.tempw = None
         self.tolp = None
         self.delta_t = None
         self.nraise = None
         self.refold_pos = None
         self.upscale = None
         self.bfgs_ndim = None
         self.trust_radius_max = None
         self.trust_radius_min = None
         self.trust_radius_ini = None
         self.w_1 = None
         self.w_2 = None

    def write_all(self,f=None):
        if f == None:
            f = sys.stdout
        #
        f.write('&IONS\n')
        sdict = self.__dict__
        for k in sdict:
            if not( sdict[k] == None ):
                if type(sdict[k]) == str:
                    f.write('  %s = \'%s\'\n' % (k,sdict[k]))
                else:
                    f.write('  %s = %s\n' % (k,sdict[k]))
        f.write('/\n\n')
