
import numpy as np
import matplotlib.pyplot as plt

x10 = np.loadtxt("rw10.dat")
x100 = np.loadtxt("rw100.dat")
x1000 = np.loadtxt("rw1000.dat")

nwalks = 100000
D = 0.5

# Conteggio delle posizioni
val10, cont10 = np.unique(x10, return_counts=True)
val100, cont100 = np.unique(x100, return_counts=True)
val1000, cont1000 = np.unique(x1000, return_counts=True)

# Probabilita'
p10 = cont10/nwalks
p100 = cont100/nwalks
p1000 = cont1000/nwalks

# Gaussiane teoriche
g10 = 2*np.exp(-val10**2/(4*D*10))/np.sqrt(4*np.pi*D*10)

g100 = 2*np.exp(-val100**2/(4*D*100))/np.sqrt(4*np.pi*D*100)

g1000 = 2*np.exp(-val1000**2/(4*D*1000))/np.sqrt(4*np.pi*D*1000)

# Distribuzione dopo 10 passi
plt.figure()
plt.plot(val10, p10, "o", label="Simulazione")
plt.plot(val10, g10, "--", label="Gaussiana")
plt.xlabel("Posizione x")
plt.ylabel("Probabilita'")
plt.title("Distribuzione dopo 10 passi")
plt.legend()
plt.grid()
plt.savefig("distribuzione10.png")

# Distribuzione dopo 100 passi
plt.figure()
plt.plot(val100, p100, "o", label="Simulazione")
plt.plot(val100, g100, "--", label="Gaussiana")
plt.xlabel("Posizione x")
plt.ylabel("Probabilita'")
plt.title("Distribuzione dopo 100 passi")
plt.legend()
plt.grid()
plt.savefig("distribuzione100.png")

# Distribuzione dopo 1000 passi
plt.figure()
plt.plot(val1000, p1000, "o", label="Simulazione")
plt.plot(val1000, g1000, "--", label="Gaussiana")
plt.xlabel("Posizione x")
plt.ylabel("Probabilita'")
plt.title("Distribuzione dopo 1000 passi")
plt.legend()
plt.grid()
plt.savefig("distribuzione1000.png")

plt.show()
