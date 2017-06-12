from __future__ import print_function

import os
import numpy as np

import ase.io
from ase.units import Bohr

from globals_wizard import *


def setup_atoms_molecules(xyzfile=None,bounding_box=None):
    print('')
    print('Setting up molecule:')
    print('--------------------')
    print('')
    if xyzfile == None:
        print('Current directory: %s' % os.getcwd())
        xyzfile = raw_input('Please specify path to xyz file: ')

    if bounding_box == None:
        bbox_in = raw_input('Please specify bounding box dimensions (in Bohr): ')
        Lx = float( bbox_in.split()[0] )
        Ly = float( bbox_in.split()[1] )
        Lz = float( bbox_in.split()[2] )
        print('Using bounding box dimensions: [%.5f,%.5f,%.5f] bohr' % (Lx, Ly, Lz))

    atoms = ase.io.read(xyzfile)
    atoms.set_pbc([True,True,True])
    cell = np.array([Lx,Ly,Lz])*Bohr
    atoms.set_cell(cell)
    atoms.center()

    return atoms



def setup_pseudopotentials(atoms, choice=None):
    print('')
    print('Setting up pseudopotentials:')
    print('----------------------------')
    print('')
    #
    if choice == None:
        print('Next, we need to setup the pseudopotentials.')
        print('We will copy the needed PBE GTH pseudopotentials')
        print('in the ./pspot directory.')
        print('Alternatively you can setup the pseudopotentials manually later')
        print('')
        print('What do you want to do?')
        print('')
        print('[1] Use the PBE GTH pseudopotentials')
        print('[2] Setup my own pseudopotentials')
        print('[r] Return to previous')
        print('[q] Quit')
        print('')
        choice = raw_input('Your choice: ')
    #
    species_list = np.unique(atoms.get_chemical_symbols())
    for s in species_list:
        print('Species: %s' % s)

    pspFiles = None
    if choice == '1':
        pspFiles = []
        if not os.path.exists('./pspots'):
            os.makedirs('./pspots')
        for s in species_list:
            os.system('cp ' + GTH_PSP_HOME + '/' + s + '.*.gth ./pspots')
        pspFiles = os.listdir('./pspots')

    elif choice == '2':
        print('')
        print('You need to edit your input file manually later.')

    else:
        pass
    #
    return pspFiles


def get_working_directory(choice=None):
    print('')
    print('Setting up working directory:')
    print('-----------------------------')
    print('')
    if choice == None:
        print('You need to choose a working directory.')
        print('')
        print('[1] Choose the current directory as working directory')
        print('[2] Choose another directory')
        print('[r] Return to the previous screen')
        print('[q] Quit')
        print('')

        choice = raw_input('Please enter your choice: ')
        print('\nYou choose: %s' % choice)

    working_dir = None
    if choice == '1':
        print('You will be using current directory as working directory')
        working_dir = './'

    elif choice == '2':
        #
        print('You will use another directory as working directory.')
        dirpath = raw_input('Please enter the path to working directory: ')
        #
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        os.chdir(dirpath)
        #
        working_dir = dirpath

    elif choice == 'q':
        print('Good bye!')
        exit()

    return working_dir
