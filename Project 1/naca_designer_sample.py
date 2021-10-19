import numpy as np

def naca_design(X,C):

    """Here, we can choose a 4 digit designation for an airfoil and 
    plot the expected geometry. Since this function is for symmetric airfoils,
    the first two digits, (max camber, and location of max camber) should be 0.

    X = maximum thickness of airfoil
    C = desired chord length
    """

    'Variable Definition'
    # Here, you should use the inputs (seen above) to describe any variables you will use in the function.
    # You should also define your x coordinate.

    xloc = 

    'Creation of Chord and Camber Line'
    # Create an empty array to hold the chord and camber values
    chord = (np.zeros(len(xloc)))
    camber = (np.zeros(len(xloc)))

    'Upper Thickness Definition'
    uZ =

    'Lower Thickness Definition'
    lZ =

    'Camber Line Definition'
    # Here, we should define the camber line according to any necessary equations. (None for symmetric)


    'Surface Definition'
    # Here, we should adjust our camber line to get the upper and lower surfaces
    upperSurf = 
    lowerSurf = 

    'Plotting'


    



