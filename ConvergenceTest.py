from PWSCFInput import *
from utils_read import *

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
        #
        self.inputs_have_been_written = False


    def run(self):
        """
        one-time run
        """
        #
        if self.what == 'ecutwfc':
            for e in self.values:
                #
                inpName = 'PWINPUT_' + str(e)
                self.pwinput.filename = inpName
                self.pwinput.SYSTEM.set_ecutwfc(e)
                self.pwinput.write()
                #
                outName = 'LOG_' + str(e)
                os.system('pw.x < ' + inpName + ' > ' + outName)
                #
                energies.append( read_pwscf_energy(outName) )
        #
        else:
            pass


    def write_all(self):
        """
        writes only the required input files
        """
        self.inputs_have_been_written = True
        pass

    def run_all(self):
        """
        """
        if not self.inputs_have_been_written:
            self.write()
        pass
