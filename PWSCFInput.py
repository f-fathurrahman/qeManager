from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

from ControlNameList import *
from SystemNameList import *
from ElectronsNameList import *
from IonsNameList import *
from utils import *

class PWSCFInput:

    """
    A simple Python class to generate PWSCF input
    """

    def __init__(self, atoms, pspFiles, filename=None, move_atoms=False,
                 gamma_only=False):

        self.atoms = atoms
        self.pspFiles = pspFiles
        if filename == None:
            self.filename = sys.stdout
        else:
            self.filename = filename
        self.move_atoms = move_atoms
        self.gamma_only = gamma_only
        #
        self.CONTROL = ControlNameList()
        self.SYSTEM = SystemNameList(atoms)
        self.ELECTRONS = ElectronsNameList()
        self.IONS = IonsNameList()


    def set_spinpolarized(self):
        self.SYSTEM.set_spinpolarized()

    def set_ecutwfc(self,ecutwfc):
        self.SYSTEM.set_ecutwfc(ecutwfc)

    def set_smearing(self,smearing_type='mv',degauss=0.01):
        self.SYSTEM.set_smearing(smearing_type=smearing_type,degauss=degauss)

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
        write_kpoints( f=inpFile, gamma_only=self.gamma_only )
        write_cell( self.atoms, f=inpFile )
        #
        inpFile.close()
