from __future__ import print_function
import string

class PWSCFOutput:

    def __init__(self, fname):
        self.filename = fname
        self.file = open(fname, 'r')

    def parse(self):
        f = self.file
        line = f.readline()
        while line:
            #
            if 'Program PWSCF' in line:
                self.version = line.split()[2]
                self.start_date = line.split()[8]
                self.start_time = string.join( line.split()[10:] ).replace(' ','')
                print('Version = %s' % self.version)
                print('Start date = %s' % self.start_date)
                print('Start time = %s' % self.start_time)
            #
            line = f.readline()

    def close(self):
        self.file.close()
