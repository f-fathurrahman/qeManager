import sys

class ControlNameList:

    def __init__(self):
        self.pseudo_dir = './'
        self.etot_conv_thr = 1.e-6
    
    def write_all(self,f=None):
        if f == None:
            f = sys.stdout
        #
        f.write('&CONTROL\n')
        sdict = self.__dict__
        for k in sdict:
            if not( sdict[k] == None ):
                if type(sdict[k]) == str:
                    f.write('  %s = \'%s\'\n' % (k,sdict[k]))
                elif type(sdict[k]) == list:
                    Nlist = len(sdict[k])
                    for i in range(Nlist):
                        f.write('  %s(%d) = %f\n' % (k,i+1,sdict[k][i]))
                else:
                    f.write('  %s = %s\n' % (k,sdict[k]))
        f.write('/\n\n')

