from __future__ import print_function
import os

def setup_pseudopotentials(atoms):
    print('Next, we need to setup the pseudopotentials.')
    print('We will copy the needed PBE GTH pseudopotentials')
    print('in the ./pspot directory.')
    print('Alternatively you can setup the pseudopotentials manually later')
    print('')
    print('What do you want to do?')
    print('')
    print('[1] Use the PBE GTH pseudopotentials')
    print('[2] Setup my own pseudopotentials')


def get_working_directory():
    print('First, you need to choose a working directory.')
    print('')
    print('[1] Choose the current directory as working directory')
    print('[2] Choose another directory')
    print('[r] Return to the previous screen')
    print('[q] Quit')
    print('')

    choice = raw_input('Please enter your choice: ')
    print('\nYou choose: %s' % choice)

    if choice == '1':
        print('You will be using current directory as working directory')

    elif choice == '2':
        print('You will use another directory as working directory.')
        dirpath = raw_input('Please enter the path to working directory: ')
        print(dirpath)
        os.chdir(dirpath)
        print(os.getcwd())
        os.system('ls -l')

    elif choice == 'q':
        print('Good bye!')
        exit()
