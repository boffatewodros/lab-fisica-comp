import matplotlib.pyplot as plt
import numpy as np

# Lettura dei file dati (colonne: tempo, theta, omega, energia)
t0, th0, w0, E0 = np.loadtxt("gamma0.dat", unpack=True)
t1, th1, w1, E1 = np.loadtxt("gamma02.dat", unpack=True)
t2, th2, w2, E2 = np.loadtxt("gamma1.dat", unpack=True)
t3, th3, w3, E3 = np.loadtxt("gamma7.dat", unpack=True)


# GRAFICO 1: Angolo nel tempo

plt.figure(figsize=(8, 5))
plt.plot(t0, th0, label=r"$\gamma = 0$")
plt.plot(t1, th1, label=r"$\gamma = 0.2$")
plt.plot(t2, th2, label=r"$\gamma = 1.0$")
plt.plot(t3, th3, label=r"$\gamma = 7.0$")

plt.xlabel(r"Tempo $t$ [s]")
plt.ylabel(r"Angolo $\theta$ [rad]")
plt.title(r"Evoluzione temporale dell'angolo $\theta(t)$")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("angolo.png", dpi=200)
plt.show()


# GRAFICO 2: Spazio delle fasi (omega vs theta)

plt.figure(figsize=(7, 6))
plt.plot(th0, w0, label=r"$\gamma = 0$")
plt.plot(th1, w1, label=r"$\gamma = 0.2$")
plt.plot(th2, w2, label=r"$\gamma = 1.0$")
plt.plot(th3, w3, label=r"$\gamma = 7.0$")

plt.xlabel(r"$\theta$ [rad]")
plt.ylabel(r"$\omega = \dot{\theta}$ [rad/s]")
plt.title("Traiettorie nello spazio delle fasi")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("fasi.png", dpi=200)
plt.show()


# GRAFICO 3: Energia meccanica nel tempo

plt.figure(figsize=(8, 5))
plt.plot(t0, E0, label=r"$\gamma = 0$")
plt.plot(t1, E1, label=r"$\gamma = 0.2$")
plt.plot(t2, E2, label=r"$\gamma = 1.0$")
plt.plot(t3, E3, label=r"$\gamma = 7.0$")

plt.xlabel(r"Tempo $t$ [s]")
plt.ylabel(r"Energia $E$ [J]")
plt.title(r"Decadimento dell'energia meccanica $E(t)$")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("energia.png")
plt.show()
