
import numpy as np
import matplotlib.pyplot as plt

t, media, msd = np.loadtxt("rw.dat", unpack=True)

nwalks = 10000
sigma = np.sqrt(t/nwalks)

# Posizione media
plt.figure()
plt.plot(t, media, label="Media")
plt.plot(t, sigma, "--", label="+sigma")
plt.plot(t, -sigma, "--", label="-sigma")
plt.xlabel("Tempo")
plt.ylabel("<x>")
plt.title("Random walk - Posizione media")
plt.legend()
plt.grid()
plt.savefig("media_rw.png")

# MSD in scala logaritmica
plt.figure()
plt.loglog(t, msd, label="MSD simulato")
plt.loglog(t, t, "--", label="MSD teorico")
plt.xlabel("Tempo")
plt.ylabel("MSD")
plt.title("Random walk - Diffusione")
plt.legend()
plt.grid()
plt.savefig("msd_rw.png")

# Fit lineare
m, q = np.polyfit(t, msd, 1)

D = m/2

print("Pendenza =", m)
print("Intercetta =", q)
print("D misurato =", D)
print("D teorico = 0.5")

# Grafico del fit
plt.figure()
plt.plot(t, msd, label="Dati")
plt.plot(t, m*t+q, "--", label="Fit lineare")
plt.xlabel("Tempo")
plt.ylabel("MSD")
plt.title("Random walk - Fit lineare")
plt.legend()
plt.grid()
plt.savefig("fit_rw.png")

plt.show()
