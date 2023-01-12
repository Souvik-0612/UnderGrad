import numpy as np
import matplotlib.pyplot as plt

def LagrangeInterpol(x, y, xin): 
	#xin => Point of interest
	summ = 0
	
	for s in range(len(x)):
		a = 1; b = 1;
		for m in range(len(x)):
			if m != s:
				a *= (x[s] - x[m])
				b *= (xin - x[m])
				
		summ += y[s]*b/a
		
	return summ

#Given data
x = np.array([1, 2, 4, 7, 9])
y = np.array([1, 4, 16, 49, 81])

#interpolated 
xx = np.linspace(1, 9, 100)

plt.plot(x, y, 'ro')
plt.plot(xx, LagrangeInterpol(x, y, xx))
plt.show()
