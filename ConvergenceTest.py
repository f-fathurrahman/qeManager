from PWSCFInput import *
from utils_read import *
import os
import numpy as np

class ConvergenceTest:

    def __init__(self, pwinput, what=None, values=None):
        """
        `what` can be one of ecutwfc, kpts
        `values`
        """
        #
        if what == None and values==None:
            raise RuntimeWarning('Value of what is set to ecutwfc')
            self.what = 'ecutwfc'
            self.values = np.arange(20,80,10)
        #
        self.pwinput = pwinput
        self.what = what
        self.values = values
        self.Ndata = len(values)
        #
        self.energies = None
        self.inpFiles = []
        self.outFiles = []
        for v in values:
            self.inpFiles.append('PWINPUT_' + str(v))
            self.outFiles.append('LOG_' + str(v))
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
        if self.what == 'ecutwfc':
            for i in range(self.Ndata):
                os.system('pw.x < ' + self.inpFiles[i] + ' > ' + self.outFiles[i])
        else:
            raise RuntimeError('what = %s is not implemented yet' % (self.what))


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
        else:
            raise RuntimeError('what = %s is not implemented yet' % (self.what))
        #
        self.inputs_have_been_written = True


    def read(self):
        """
        Read data
        """
        if self.what == 'ecutwfc':
            energies = []
            for i in range(self.Ndata):
                energies.append( read_pwscf_energy(self.outFiles[i]) )
            self.energies = np.array(energies)
            return self.values, self.energies
        #
        else:
            raise RuntimeError('what = %s is not implemented yet' % (self.what))
