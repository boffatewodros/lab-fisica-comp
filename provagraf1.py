import matplotlib.pyplot as plt
import numpy as np

# Lettura file: prima colonna dt, seconda colonna errore
dt1, e1 = np.loadtxt("euler.dat", unpack=True)
dt2, e2 = np.loadtxt("cromer.dat", unpack=True)
dt3, e3 = np.loadtxt("verlet.dat", unpack=True)
dt4, e4 = np.loadtxt("rk2.dat", unpack=True)
dt5, e5 = np.loadtxt("rk4.dat", unpack=True)

plt.figure(figsize=(8, 6))

plt.loglog(dt1, e1, "o-", label="Eulero")
plt.loglog(dt2, e2, "s-", label="Eulero-Cromer")
plt.loglog(dt3, e3, "^-", label="Velocity Verlet")
plt.loglog(dt4, e4, "d-", label="RK2")
plt.loglog(dt5, e5, "v-", label="RK4")

plt.xlabel(r"Passo temporale $\Delta t$")
plt.ylabel("Errore globale")
plt.title("Analisi di convergenza dei metodi numerici")

# Griglia adatta al grafico bilogaritmico (linee principali e secondarie)
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("convergenza.png")
plt.show()
