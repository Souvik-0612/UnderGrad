import numpy as np
import matplotlib.pyplot as plt
import scienceplots
plt.style.use(['science', 'notebook', 'grid'])

# Experimental data
T = np.array([800, 1000, 1100, 1240, 1300, 1400, 1540, 1560, 1720, 1760, 1780, 1840, 1900, 1940, 2040, 2140, 2340])
P = np.array([154, 316.4, 457.6, 737.2, 970.2, 1242, 1650, 1835, 2488, 2724, 3193.6, 4137, 4902, 5148, 6051.6, 8077.6, 9359])
newT = np.log(T)
newP = np.log(P)


Aug = np.array([[sum(newT**2), sum(newT), sum(newT*newP)],
[sum(newT), len(newT), sum(newP)]], dtype=float)


Aug[1] = Aug[1] - Aug[1][0]*Aug[0]/Aug[0][0]

c = Aug[1][-1]/Aug[1][-2]
m = (Aug[0][-1] - c*Aug[0][-2])/Aug[0][0]


print("Slope", m)
print("Intercept", c)


y = m*newT + c

yrr = newP - y
plt.figure(figsize = (14, 10))
plt.title("Stephan's Law verification", size = 25)
#
plt.plot(newT, newP, "ro", label = "Experimental data")
plt.plot(newT, y, label = "Fitting curve")


upperlims = []; lowerlims = []
for i in range(len(yrr)):
	if yrr[i] < 0:
		lowerlims.append(True)
		upperlims.append(False)
	else:
		lowerlims.append(False)
		upperlims.append(True)
		
	print(yrr[i], lowerlims[i], upperlims[i])

		

plt.errorbar(newT, y, yerr= yrr, uplims=upperlims, lolims= lowerlims, ecolor="k")


plt.legend(loc = 'best')
plt.xlabel(r"$\ln T$", size = 20)
plt.ylabel(r"$\ln P$", size = 20)
plt.savefig("Souvik.png")
plt.show()