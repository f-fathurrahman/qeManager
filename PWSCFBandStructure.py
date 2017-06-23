import matplotlib.pyplot as plt
from utils_read import *

class PWSCFBandstructure:

    def __init__(self,pwinput):
        self.pwinput = pwinput


    def write_scf(self):
        self.pwinput.filename = 'PWINPUT_scf'
        self.pwinput.write()

    def write_bands(self):
        self.pwinput.set_calc_bands('fcc',Nkpts=100)
        self.pwinput.filename = 'PWINPUT_bands'
        self.pwinput.write()

    def write_collect_bands(self):
        write_bands_inp()

    def run(self):
        pass

    def plot_bands(self, use_collect_bands_data=True,
                   shift_to_efermi=False, ):
        #
        Nbands, Nkpts = get_Nbands_Nkpts('LOG_bands')
        print('Nbands = ', Nbands, 'Nkpts = ', Nkpts)

        if not use_collect_bands_data:
            xcoords = pwinput.bands_xcoords
            ebands = read_bandstructure('LOG_bands')
        else:
            xcoords, ebands = read_bands_gnu('bands.out.gnu', Nbands, Nkpts)

        Efermi = read_fermi_level('LOG_scf')

        if shift_to_efermi:
            ebands[:,:] = ebands[:,:] - Efermi

        #Emin = np.min(ebands)
        #Emax = np.max(ebands)
        Emin = 10
        Emax = 30

        print('Emin   = ', Emin)
        print('Emax   = ', Emax)
        print('Efermi = ', Efermi)

        plt.clf()
        for ib in range(Nbands):
            plt.plot( xcoords[ib,:], ebands[ib,:], marker='o' )

        plt.grid()
        plt.ylim(Emin,Emax)

        #specialk_xcoords = pwinput.specialk_xcoords
        specialk_xcoords = read_specialk_xcoords('LOG_collect_bands')

        kmin = np.min(specialk_xcoords)
        kmax = np.max(specialk_xcoords)

        plt.xlim(kmin,kmax)

        for p in specialk_xcoords:
          plt.plot([p, p], [Emin, Emax], 'k-')

        plt.plot([kmin,kmax],[Efermi,Efermi], 'k-', linewidth=2)

        plt.savefig('bands.png', dpi=300)
