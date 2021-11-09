# For problem 2. Creating cl vs alpha data for the given 4408 airfoil and the arbitrarily chosen 4208. The alpha is varied

import pyxfoil_demo
import numpy as np
foils = ['4520']

Re1 = 0 # inviscid
Re2 = 6e5 # viscous effects
alfs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
plot = False

for i in range(2):
    pyxfoil_demo.pyxfoil_demo(foils[i], Re1, Re2, alfs, plot)