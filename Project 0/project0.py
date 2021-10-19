import numpy as np
import matplotlib.pyplot as plt

# Part 1: Boundary Layers and Numeric Integration

# Part 1.1: Turbulent Boundary Layer Velocity Profile
ynon = np.linspace(start=0, stop=1, num=1000)
unon = ynon**(1/7)
plt.figure(1)
plt.title('Boundary Layer Velocity Profile\nRe=1.0E+08')
plt.xlabel('u/ue')
plt.ylabel('y/delta')
plt.plot(unon, ynon)
plt.show()


# Part 1.2: Boundary Layer Thickness
Rex = 10**8
x = 300 #feet
delta = 0.16*x/(Rex**(1/7))
print(f'Boundary layer thickness estimate: {delta} in')

deltastarnon = np.trapz(1-unon, ynon)
deltastar = deltastarnon*delta
print(f'Displacement thickness by integration: {deltastar} in')

# Part 2.1: Airfoil Plotting
# airfoils picked: e423, n2415, s1223
filename = 'e423.dat'
e423x,e423z=np.loadtxt(filename,unpack=True, delimiter=',')
filename = 'n2415.dat'
n2415x, n2415z = np.loadtxt(filename, unpack=True, delimiter=',')
filename = 's1223.dat'
s1223x, s1223z = np.loadtxt(filename, unpack=True)
plt.plot(e423x, e423z, linestyle='-')
plt.plot(s1223x, s1223z, linestyle='--')
plt.plot(n2415x, n2415z, linestyle='-', markers='.')
plt.grid(True)
plt.xlim([0,1])
plt.axis('equal')
plt.xlabel("x/c")
plt.ylabel("z/c")
plt.show()



# Part 2.2: Cross-sectional area line integration
c=9.5
filename='naca66210_geom.txt'
x,z=np.loadtxt(filename,unpack=True,skiprows=1)
x*=c
z*=c
area_green=-np.trapz(z,x)
x,z=np.loadtxt(filename,unpack=True,skiprows=1)
plt.title('Airfoil Geometries for Naca 66210')
plt.xlabel("x/c")
plt.ylabel("z/c")
plt.plot(x*c,z*c)
plt.axis('equal')
plt.xlim([0,c])
plt.show()


# Part 3.1: Airfoil Surface pressure
file = 'naca2412_SurfPress_a6.csv'
x,cpl,cpu=np.loadtxt(file,skiprows=1,unpack=True,delimiter=',')
plt.figure(4)
plt.title('Surface Pressure Distribution NACA 2412')
plt.xlabel("x/c")
plt.ylabel("C_P")
plt.gca().invert_yaxis()
plt.plot(x,cpu,label = 'Upper')
plt.plot(x,cpl,label='Lower')
plt.grid(True)
plt.xlim([0,1])
plt.legend()
plt.show()

# Part 3.2: Surface Pressure Gradient and Numeric Differentiation
dCpu_dx = np.zeros(len(cpu)-1)
dCpl_dx = np.zeros(len(cpl)-1)
for i in range(len(dCpu_dx)):
    dCpu_dx[i] = (cpu[i+1]-cpu[i])/(x[i+1]-x[i])
    dCpl_dx[i]=(cpl[i+1]-cpl[i])/(x[i+1]-x[i])
plt.figure(5)
plt.title('Surface Pressure Gradient \n NACA 2412 $(\\alpha=6^o)$')
plt.xlabel("x/c")
plt.ylabel("$dC_P$/dx")
plt.plot(x[:-1],dCpu_dx,label='Upper')
plt.plot(x[:-1],dCpl_dx,label='Lower')
plt.grid(True)
plt.xlim([0,1])
plt.ylim([-10,10])
plt.legend()
plt.show()

# Part 4.1: Lift curve and excel files
import pandas as pd 
df=pd.read_excel('naca0018_LiftCurve.xlsx')
alpha0018=df['alpha']
Cl0018=df['Cl']
df2=pd.read_excel('naca4418_LiftCurve.xlsx')
alpha4418=df2['alpha']
Cl4418=df2['Cl']
filename="naca0018.dat"
x0018,y0018=np.loadtxt(filename,unpack=True,skiprows=1)
filename="naca4418.dat"
x4418,y4418=np.loadtxt(filename,unpack=True,skiprows=1)

plt.figure(6)
plt.title('Airfoil Geometry for NACA 0018')
plt.xlabel("x/c")
plt.ylabel("z/c")
plt.plot(x0018,y0018)
plt.grid(True)
plt.xlim([0,1])
plt.axis('equal')
plt.show()

plt.figure(7)
plt.title('Airfoil Geometry for NACA 4418')
plt.xlabel("x/c")
plt.ylabel("z/c")
plt.plot(x4418,y4418)
plt.grid(True)
plt.xlim([0,1])
plt.axis('equal')
plt.show()

plt.subplot(1,2,1)
plt.title('NACA 0018')
plt.xlabel("x/c")
plt.ylabel("z/c")
plt.plot(x0018,y0018)
plt.grid(True)
plt.xlim([0,1])
plt.axis('equal')
plt.subplot(1,2,2)
plt.title('NACA 4418')
plt.xlabel("x/c")
plt.ylabel("z/c")
plt.plot(x4418,y4418)
plt.grid(True)
plt.xlim([0,1])
plt.axis('equal')
plt.show()

# Part 4.2: Linear interpolation
plt.figure(8)
plt.title('NACA 0018 Lift Curve')
plt.xlabel("$\\alpha$")
plt.ylabel("$C_l$")
plt.plot(alpha0018,Cl0018,marker='.',markersize=12,linewidth=2)
plt.grid(True)
plt.xlim([-12,22])
plt.ylim([-1.1,2.0])
plt.show()

plt.figure(9)
plt.title('NACA 4418 Lift Curve')
plt.xlabel("$\\alpha$")
plt.ylabel("$C_l$")
plt.plot(alpha4418,Cl4418,marker='.',markersize=12,linewidth=2)
plt.grid(True)
plt.xlim([-12,22])
plt.ylim([-1.1,2.0])
plt.show()

# Part 5: Linear Algebra
A = np.array([[4, 2, 3, 2], 
              [-3, 1, -2, 3], 
              [0, 1, 2, 1], 
              [3, 1, -1, -2]])
b = np.array([10, 9, -3, -5])
l = np.linalg.solve(A, b)
print(f'A: {A}')
print(f'b: {b}')
print(f'Solved matrix lambda: {l}')