import sys
from .ControlNameList import *
from .SystemNameList import *
from .ElectronsNameList import *
from ..pwscf.utils_write import write_atomic_positions, write_atomic_species


class ffrLFDFTInput:


    def __init__(self, atoms, pspFiles, filename=None):
        self.atoms = atoms
        self.pspFiles = pspFiles
        if filename == None:
            self.filename = sys.stdout
        else:
            self.filename = filename
                #
        self.CONTROL = ControlNameList()
        self.SYSTEM = SystemNameList(atoms)
        self.ELECTRONS = ElectronsNameList()

    def write(self):
                #
        inpFile = open(self.filename,'w')
        #
        self.CONTROL.write_all(f=inpFile)
        self.SYSTEM.write_all(f=inpFile)
        self.ELECTRONS.write_all(f=inpFile)
        write_atomic_species( self.atoms, pspFiles=self.pspFiles, f=inpFile )
        write_atomic_positions( self.atoms, f=inpFile )



