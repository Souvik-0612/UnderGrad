import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scienceplots
plt.style.use(['science', 'notebook', 'grid'])

#Potential
def V(x):
	return 1/2*x*x
	
#Initial conditions
S0 = (0, 1)

a = 5

#X range
x = np.linspace(-a, a, 500)

#Differeantial equation solver
def Schrodinger(S, x, E):
	(psi, dpsi) = S
	return [dpsi, -2*(E - V(x))*psi]

#Energy
E, h = np.linspace(0, 20, 100, retstep=True)

	
def psiL(e):
	sol = odeint(Schrodinger, S0, x, args=(e, ))
	return sol.T[0][-1]

#Root finding
def NR(f, G, tol = 0.001):
	count = 0
	while abs(f(G)) > tol:
		count += 1
		G -= 2*h*f(G)/(f(G+h) - f(G-h))
		if count > 100:
			break
	return G
#Integration
def integrate(y, x): # y is an array
    h = x[1] - x[0]
    return 0.5*h*(y[0]+y[-1]+2*sum(y[1:-1]))
	
En = [] #Eigen energies
for i in range(0, 30):
	En.append(NR(psiL, i))

plt.figure(figsize=(14, 8))
plt.title("Linear 1D quantum harmonic oscillator")
plt.xlabel(r"x $\rightarrow$")
plt.ylabel(r"$\psi(x)$")
plt.plot(x, 0.1*V(x), label = "Potential")

for e in En[0:3]: #Change the slicing of En to go particular E
	psi = odeint(Schrodinger, S0, x, args=(e, )).T[0]
	Norm = np.sqrt(1/integrate(psi*psi, x))
	plt.plot(x, Norm*psi, label = "E = " + str(round(e, 1)))
	
plt.legend()
	
plt.show()