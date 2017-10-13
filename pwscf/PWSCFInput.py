from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

from .ControlNameList import *
from .SystemNameList import *
from .ElectronsNameList import *
from .IonsNameList import *
from .utils_write import *
from ..utils import *

class PWSCFInput:

    """
    A simple Python class to generate PWSCF input
    """

    def __init__(self, atoms, pspFiles, filename=None, move_atoms=False,
                 gamma_only=False, kpt_automatic=False, Nk=[1,1,1], nkshift=[0,0,0]):

        self.atoms = atoms
        self.pspFiles = pspFiles
        if filename == None:
            self.filename = sys.stdout
        else:
            self.filename = filename
        self.move_atoms = move_atoms
        self.gamma_only = gamma_only
        self.kpt_automatic = kpt_automatic
        self.Nk = Nk
        self.nkshift = nkshift
        #
        self.CONTROL = ControlNameList()
        self.SYSTEM = SystemNameList(atoms)
        self.ELECTRONS = ElectronsNameList()
        self.IONS = IonsNameList()
        # for bandstructure
        self.bandstructure_mode = False
        self.kpts = None
        self.kweights = None
        self.special_kcoords = None


    def set_spinpolarized(self):
        self.SYSTEM.set_spinpolarized()

    def set_ecutwfc(self,ecutwfc):
        self.SYSTEM.set_ecutwfc(ecutwfc)

    def set_smearing(self,smearing_type='mv',degauss=0.01):
        self.SYSTEM.set_smearing(smearing_type=smearing_type,degauss=degauss)

    def set_calc_bands(self, lattice, Nkpts=60):
        self.bandstructure_mode = True
        self.kpt_automatic = False
        self.gamma_only = False
        self.CONTROL.calculation = 'bands'
        self.CONTROL.verbosity = 'high'
        #
        kpts, x, Xkpt = gen_kpath( self.atoms, lattice, Nkpts=Nkpts )
        Nkpts = len(x)
        print("Nkpts = ", Nkpts)
        for ik in range(Nkpts):
            sys.stdout.write('%.8f %.8f %.8f %.8f\n' % (kpts[ik,0],kpts[ik,1],kpts[ik,2],x[ik]))
        print(Xkpt)
        #
        self.bands_xcoords = x
        self.kpts = kpts
        self.kweights = np.ones(len(x))
        self.specialk_xcoords = Xkpt


    def write(self):
        #
        inpFile = open(self.filename,'w')
        #
        self.CONTROL.write_all(f=inpFile)
        self.SYSTEM.write_all(f=inpFile)
        self.ELECTRONS.write_all(f=inpFile)
        if self.move_atoms:
            self.IONS.write_all(f=inpFile)
        write_atomic_species( self.atoms, pspFiles=self.pspFiles, f=inpFile )
        write_atomic_positions( self.atoms, f=inpFile )
        #
        if self.bandstructure_mode:
            write_kpoints( f=inpFile, gamma_only=self.gamma_only, automatic=self.kpt_automatic,
                       Nk=self.Nk, nkshift=self.nkshift,
                       bandstructure=True,
                       kpts=self.kpts, weights=self.kweights )
        else:
            write_kpoints( f=inpFile, gamma_only=self.gamma_only, automatic=self.kpt_automatic,
                       Nk=self.Nk, nkshift=self.nkshift )
        #
        write_cell( self.atoms, f=inpFile )
        #
        inpFile.close()
