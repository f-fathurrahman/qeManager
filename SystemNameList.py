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
        """
        noinv | no_t_rev | force_symmorphic | use_all_frac | occupations | one_atom_occupations |
        starting_spin_angle | degauss | smearing | nspin | noncolin | ecfixed | qcutz | q2sigma |
        input_dft | exx_fraction | screening_parameter | exxdiv_treatment | x_gamma_extrapolation |
        ecutvcut | nqx1 | nqx2 | nqx3 | lda_plus_u | lda_plus_u_kind | Hubbard_U | Hubbard_J0 |
        Hubbard_alpha | Hubbard_beta | Hubbard_J(i,ityp) | starting_ns_eigenvalue(m,ispin,I) |
        U_projection_type | edir | emaxpos | eopreg | eamp | angle1 | angle2 | constrained_magnetization
        | fixed_magnetization | lambda | report | lspinorb | assume_isolated | esm_bc | esm_w |
        esm_efield | esm_nfit | fcp_mu | vdw_corr | london | london_s6 | london_c6 | london_rvdw |
        london_rcut | ts_vdw_econv_thr | ts_vdw_isolated | xdm | xdm_a1 | xdm_a2 | space_group | uniqueb
        | origin_choice | rhombohedral | zmon | realxz | block | block_1 | block_2 | block_height
        """

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
