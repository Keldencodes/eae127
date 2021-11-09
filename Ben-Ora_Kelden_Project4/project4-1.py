# For problem 2. Creating cl vs alpha data for the given 4408 airfoil and the arbitrarily chosen 4208. The alpha is varied

import pyxfoil_demo
import numpy as np
foils = ['0020', '2412', '4412']

Re1 = 0 # inviscid
Re2 = np.linspace(start=50000, stop=100000, num=21) # viscous effects
alfs = [5]
plot = False
for i in range(len(foils)):
    for j in range(len(Re2)):
        pyxfoil_demo.pyxfoil_demo(foils[i], Re1, Re2[j], alfs, plot)