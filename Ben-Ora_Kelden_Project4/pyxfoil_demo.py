"""PYXFOIL DEMO: XFOIL AUTOMATION USING PYTHON
EAE 127
UCD

DESCRIPTION: Use pyxfoil module to simulate airfoil performance with XFOIL
and process results

REQUIREMENTS: XFOIL must be downloaded from http://web.mit.edu/drela/Public/web/xfoil/
For Windows:
    1. Download XFOIL6.99.zip
    2. Decompress and move xfoil.exe to same folder as Python script
For Mac:
    1. Download Xfoil for Mac-OSX
    2. Open dmg, follow installation instructions

USAGE:
Windows: Save 'pyxfoil.py' and 'xfoil.exe' in same folder as script calling pyxfoil
Mac:     Save 'pyxfoil.py' in same folder as script calling pyxfoil
"""

# this is a modified version of the pyxfoil_demo to make it easier to do many trials with multiple airfoils

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import pyxfoil from same folder as a module
import pyxfoil

# #Import pyxfoil from a different folder as a module
# import sys
# sys.path.append('../../../utils')
# import pyxfoil

########################################################################
#RUN XFOIL FOR NACA AIRFOIL (GEMOETRY FROM EQUATION, NOT FILE)

#Calculate surface pressure distributions of NACA 0012 at Re=0, AoA=0
#Save all force/moment coefficients to single polar file
#Also save airfoil geometry to file
def pyxfoil_demo(airfoil, Re1, Re2, alfas, plot):
    #Inputs
    # foil = '4412' #NACA airfoil number
    # naca = True   #allows NACA number input rather than geometry text file
    # Re   = 0      #Reynolds Number (inviscid)
    # alfs = [5]#Angles of Attack to simulated

    foil = airfoil
    naca = True
    Re = Re1
    alfs = alfas
    #Run Xfoil,
        #save geometry, surface pressures, and polar (Cl vs alpha)
        #change quiet to 'False' to see raw Xfoil output
    print(f"Running XFOIL/pyxfoil and saving data in 'Data/naca{foil}' folder...\n")
    pyxfoil.GetPolar(foil, naca, alfs, Re, SaveCP=True, quiet=True)
    # print('Xfoil run complete')
    # input("Press any key to continue...")

    ########################################################################
    #READ XFOIL SOLUTION FROM SAVED TEXT FILES

    #read airfoil geometry data from file
        #(this file was created by the above 'pyxfoil.GetPolar' call)
    geom = pyxfoil.ReadXfoilAirfoilGeom(f'Data/naca{foil}/naca{foil}.dat')
    #Plot airfoil geometry
        #(NOTE: You must plot airfoil geometry from EQUATION, not file, for points in PJ1)
    print('\nPlotting airfoil geometry from file saved by XFOIL/pyxfoil')
    if plot:
        plt.figure()
        plt.title('airfoil geom')
        plt.plot(geom['x'], geom['z'])
        plt.axis('equal')
        plt.xlabel('x/c')
        plt.ylabel('z/c')
        plt.show()

    #Read and print polar data
    polar = pyxfoil.ReadXfoilPolar(f'Data/naca{foil}/naca{foil}_polar_Re0.00e+00a0.0-30.0.dat')
    print('\nPolar from file saved by XFOIL/pyxfoil:')
    print(polar)

    print("\n\nNOTE: FOR READING SURFACE PRESSURE DISTRIBUTIONS, SEE 'msesdemo.py'")
    print('------------------------------------------------------------------\n\n')

    ########################################################################
    #RUN XFOIL USING GEOMETRY SAVED IN FILE

    #You can also load an airfoil geometry from a text file
    #Use this for airfoils that are not defined by an equation
    #In this example, the NACA 0012 geometry saved to file in the previous part
    #will be loaded from file, rather than specified by NACA number

    #Inputs
    foilpath = f'Data/naca{foil}/naca{foil}.dat' #path to airfoil geometry file
    naca = False      #'False' option loads geometry from file path, not equation
    Re   = Re2        #Reynolds Number (viscous effects calculated)
    # alfs = [5] #Angles of Attack to simulate. Comment out to use same as previous

    #Run Xfoil with same command as before
    print('Running XFOIL/pyxfoil a second time, loading geometry from file...\n')
    pyxfoil.GetPolar(foilpath, naca, alfs, Re, SaveCP=True, quiet=True)

    print("There are now two different polar files in the save directory:")
    import glob
    [print('    {}: {}'.format(i+1, g)) for i, g in enumerate(glob.glob(f"Data/naca{foil}/*polar*.dat"))]
    print('The first is the inviscid polar from our first XFOIL run')
    print('The second is the viscous polar from our latest XFOIL run')

    viscpolar = pyxfoil.ReadXfoilPolar(f'Data/naca{foil}/naca{foil}_polar_Re6.00e+05a0.0-30.0.dat')
    print('\nViscous polar from file saved by XFOIL/pyxfoil the second time:')
    print(viscpolar)

    print('\n(Notice there are three entries in the table this time, rather than two')


    print('\nPlotting airfoil lift curves from polar data from files saved by XFOIL/pyxfoil')
    if plot:
        plt.figure()
        plt.title('lift curves')
        #plot inviscid data loaded in previous section
        plt.plot(polar['alpha'], polar['Cl'], marker='o', label='inviscid')
        #plot viscous data loaded in current section
        plt.plot(viscpolar['alpha'], viscpolar['Cl'], marker='x', label='viscous')
        plt.legend()
        plt.xlabel('$\\alpha$')
        plt.ylabel('$C_l$')
        plt.show()
