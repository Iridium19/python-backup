import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Daten laden
prozent1, q0 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q0.txt", delimiter=",", unpack=True)
prozent2, q1 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q1.txt", delimiter=",", unpack=True)
prozent3, q2 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q2.txt", delimiter=",", unpack=True)
prozent4, q3 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q3.txt", delimiter=",", unpack=True)

# Umrechnen von Prozent in relative Einheiten für Berechnungen
prozent11 = prozent1 * 1e-2
prozent22 = prozent2 * 1e-2
prozent33 = prozent3 * 1e-2
prozent44 = prozent4 * 1e-2

q00 = q0 * 1e-2
q11 = q1 * 1e-2
q22 = q2 * 1e-2
q33 = q3 * 1e-2

# Plot der Messdaten (x und y auf 0–100 % skaliert)
plt.scatter(prozent11 * 100, q00 * 100, marker='x', label='$Q^0$', color='blue')
plt.scatter(prozent22 * 100, q11 * 100, marker='x', label='$Q^1$', color='orange')
plt.scatter(prozent33 * 100, q22 * 100, marker='x', label='$Q^2$', color='green')
plt.scatter(prozent44 * 100, q33 * 100, marker='x', label='$Q^3$', color='red')

# Theoriekurven (ebenfalls auf Prozent skaliert)

# Q0-Theorie
f = np.linspace(64, 75, 100)   # 64 % bis 75 %
x_f = f / 100
q0_theorie = (3 * x_f - 2) / (1 - x_f) * 100
plt.plot(f, q0_theorie, color='blue', label='Theorie $Q^0$')

# Q1-Theorie
p = np.linspace(0.0, 67, 100)
x_p = p / 100
fitq1 = (-1 + 2 * x_p) / (1 - x_p) * 100
plt.plot(p, fitq1, color='orange', label='Theorie $Q^1$')

e = np.linspace(66, 80, 100)
x_e = e / 100
fitq11 = (3 - 4 * x_e) / (1 - x_e) * 100
plt.plot(e, fitq11, color='orange')

# Q2-Theorie
j = np.linspace(0.0, 50, 100)
x_j = j / 100
fitq2 = x_j / (1 - x_j) * 100
plt.plot(j, fitq2, color='green', label='Theorie $Q^2$')

n = np.linspace(50, 67, 100)
x_n = n / 100
fitq22 = (2 - 3 * x_n) / (1 - x_n) * 100
plt.plot(n, fitq22, color='green')

# Q3-Theorie
x_hdfs = p / 100
fitq3 = (1 - x_hdfs / (1 - x_hdfs)) * 100
plt.plot(p, fitq3, color='red', label='Theorie $Q^3$')

# Achsenbeschriftung & Formatierung
plt.xlabel(r'$Na_2O$ (mol %)')
plt.ylabel('Q-Anteil (%)')
plt.xlim(0, 80)
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.show()
