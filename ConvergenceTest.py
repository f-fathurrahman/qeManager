from PWSCFInput import *
from utils_read import *
import os
import numpy as np

class ConvergenceTest:
    """
    A class for doing 1D convergence test.
    """

    def __init__(self, pwinput, what=None, values=None, prefixInp='PWINPUT_', prefixOut='LOG_'):
        """
        `what` can be one of ecutwfc, kpts
        `values`
        """
        #
        if what == None and values==None:
            raise RuntimeWarning('Test convergence is set to ecutwfc')
            self.what = 'ecutwfc'
            self.values = np.arange(20,80,10)
        #
        self.pwinput = pwinput
        self.what = what
        self.values = values
        self.Ndata = len(values)
        #
        self.energies = None
        #
        self.prefixInp = prefixInp  # XXX need to save this ?
        self.prefixOut = prefixOut
        self.inpFiles = []
        self.outFiles = []
        for v in values:
            self.inpFiles.append(self.prefixInp + what + '_' + str(v))
            self.outFiles.append(self.prefixOut + what + '_' + str(v))
        #
        self.inputs_have_been_written = False


    def run(self):
        """
        one-time run
        """
        #
        if not self.inputs_have_been_written:
            self.write()
        #
        for i in range(self.Ndata):
            os.system('pw.x < ' + self.inpFiles[i] + ' > ' + self.outFiles[i])


    def write(self):
        """
        writes only the required input files
        """
        #
        if self.what == 'ecutwfc':
            for i in range(self.Ndata):
                self.pwinput.filename = self.inpFiles[i]
                self.pwinput.SYSTEM.set_ecutwfc(self.values[i])
                self.pwinput.write()
        #
        elif self.what == 'ecutrho':
            for i in range(self.Ndata):
                self.pwinput.filename = self.inpFiles[i]
                self.pwinput.SYSTEM.ecutrho = self.values[i]
                self.pwinput.write()
        #
        else:
            raise RuntimeError('what = %s is not implemented yet' % (self.what))
        #
        self.inputs_have_been_written = True


    def read(self):
        """
        Read data
        """
        energies = []
        for i in range(self.Ndata):
            energies.append( read_pwscf_energy(self.outFiles[i]) )
        self.energies = np.array(energies)
        return self.values, self.energies
