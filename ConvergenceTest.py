class ConvergenceTest:

    def __init__(self, what=None, values=None):
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
        self.what = what
        self.values = values
        #
        self.inputs_have_been_written = False


    def write(self):
        """
        writes only the required input files
        """
        self.inputs_have_been_written = True
        pass

    def run(self):
        """
        """
        if not self.inputs_have_been_written:
            self.write()
        pass