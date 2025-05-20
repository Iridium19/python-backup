import matplotlib.pyplot as plt
import numpy as np

# Energieniveaus (in eV, Beispielwerte)
niveaus_energie = [0, 1.5, 3.0, 4.5, 6.0]  # Energieniveaus (in eV)
niveaus = [1, 2, 3, 4]  # Die Niveaus: n = 1 bis n = 4

# Erstelle das Diagramm
fig, ax = plt.subplots(figsize=(6, 6))

# Zeichne die Energieniveaus als horizontale Linien
for i, energie in enumerate(niveaus_energie):
    ax.hlines(energie, 0, 1, colors='blue', linewidth=2)
    ax.text(1.02, energie, f'n={niveaus[i]}', verticalalignment='center', fontsize=12)

# Darstellung der Elektronen
# Elektronen auf n=1, n=2, n=3 (voll besetzt)
# Wir setzen den Abstand zwischen den Elektronen auf den Niveaus
elektronen_pos = {
    1: [0.1, 0.2],  # Zwei Elektronen auf n=1
    2: [0.3, 0.4],  # Zwei Elektronen auf n=2
    3: [0.5, 0.6],  # Zwei Elektronen auf n=3
}

# Zeichne Elektronen auf den Niveaus
for n, pos in elektronen_pos.items():
    for p in pos:
        ax.plot(p, niveaus_energie[n - 1], 'bo', markersize=10)

# Elektronensprung von n=3 nach n=4 (Elektron wird angeregt)
# Wir verwenden einen roten Pfeil, um den Übergang zu zeigen
ax.arrow(0.55, niveaus_energie[2], 0, niveaus_energie[3] - niveaus_energie[2],
         head_width=0.05, head_length=0.1, fc='red', ec='red')

# Text für die Energie des Photons
energie_quanten = niveaus_energie[3] - niveaus_energie[2]
ax.text(0.55, (niveaus_energie[2] + niveaus_energie[3]) / 2,
        f'ΔE = {energie_quanten} eV', color='red', fontsize=12)

# Achsen anpassen
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.5, 6.5)
ax.set_xlabel('Position (Arbitrary)', fontsize=12)
ax.set_ylabel('Energie (eV)', fontsize=12)
ax.set_title('Energieniveauschema und Elektronenanregung', fontsize=14)

# Verstecke die x-Achse
ax.get_xaxis().set_visible(False)

# Zeige das Diagramm
plt.tight_layout()
plt.show()
