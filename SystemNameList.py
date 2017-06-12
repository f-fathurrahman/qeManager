import numpy as np
import sys

class SystemNameList:

    """
    A class to represent SYSTEM namelist in PWSCF input.
    Atomic structures will be specified using in CELL_PARAMETERS.
    """
    def __init__(self, atoms):

        self.ibrav = 0
        self.celldm = None
        self.A = None
        self.B = None
        self.C = None
        self.cosAB = None
        self.cosAC = None
        self.cosBC = None
        self.nat = len(atoms)

        self.ntyp = len( np.unique( atoms.get_atomic_numbers() ) )

        self.nbnd = None
        self.tot_charge = None
        self.tot_magnetization = None
        self.starting_magnetization = None
        self.ecutwfc = 30.0
        self.ecutrho = 4.*self.ecutwfc
        self.ecutfock = None
        self.nr1 = None
        self.nr2 = None
        self.nr3 = None
        self.nr1s = None
        self.nr2s = None
        self.nr3s = None
        self.nosym = None
        self.nosym_evc = None

        self.noinv = None
        self.no_t_rev = None
        self.force_symmorphic = None
        self.use_all_frac = None
        self.occupations = None
        self.one_atom_occupations = None
        self.starting_spin_angle = None
        self.degauss = None
        self.smearing = None
        self.nspin = None
        self.noncolin = None
        self.ecfixed = None
        self.qcutz = None
        self.q2sigma = None
        self.input_dft = None

        self.exx_fraction = None
        self.screening_parameter = None
        self.exxdiv_treatment = None
        self.x_gamma_extrapolation = None
        self.ecutvcut = None
        self.nqx1 = None
        self.nqx2 = None
        self.nqx3 = None
        self.lda_plus_u = None
        self.lda_plus_u_kind = None
        self.Hubbard_U = None
        self.Hubbard_J0 = None
        self.Hubbard_alpha = None
        self.Hubbard_beta = None
        #Hubbard_J(i,ityp)
        #starting_ns_eigenvalue(m,ispin,I)
        self.U_projection_type = None
        self.edir = None
        self.emaxpos = None
        self.eopreg = None
        self.eamp = None
        self.angle1 = None
        self.angle2 = None
        self.constrained_magnetization = None
        self.fixed_magnetization = None
        #lambda
        self.report = None
        self.lspinorb = None
        self.assume_isolated = None
        self.esm_bc = None
        self.esm_w = None
        self.esm_efield = None
        self.esm_nfit = None
        self.fcp_mu = None
        self.vdw_corr = None
        self.london = None
        self.london_s6 = None
        self.london_c6 = None
        self.london_rvdw = None
        self.london_rcut = None
        self.ts_vdw_econv_thr = None
        self.ts_vdw_isolated = None
        self.xdm = None
        self.xdm_a1 = None
        self.xdm_a2 = None
        self.space_group = None
        self.uniqueb = None
        self.origin_choice = None
        self.rhombohedral = None
        self.zmon = None
        self.realxz = None
        self.block = None
        self.block_1 = None
        self.block_2 = None
        self.block_height = None


    def set_ecutwfc(self,ecutwfc):
        self.ecutwfc = ecutwfc
        self.ecutrho = 4.0*ecutwfc

    def write(self, f=None):
        if f == None:
            f = sys.stdout
        #
        f.write('&SYSTEM\n')
        f.write('  ibrav = %d\n' % self.ibrav)
        f.write('  nat = %d\n' % self.nat)
        f.write('  ntyp = %d\n' % self.ntyp)
        f.write('  ecutwfc = %f\n' % self.ecutwfc)
        f.write('  ecutrho = %f\n' % self.ecutrho)
        f.write('/\n\n')

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
                else:
                    f.write('  %s = %s\n' % (k,sdict[k]))
        f.write('/\n\n')
