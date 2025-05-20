import matplotlib.pyplot as plt
import numpy as np

# Energieniveaus (in eV, als Beispiel)
niveaus = [0, 1, 2, 3, 4,5 ,6 ,7]
niveaus_energie = [0, 1, 2, 3, 4, 5, 6, 7]  # Energie in eV

x=7
y=6




# Erstelle das Diagramm
fig, ax = plt.subplots(figsize=(6, 6))

# Zeichne die Energieniveaus als horizontale Linien
for i, energie in enumerate(niveaus_energie):
    if i == 0:
        continue
    ax.hlines(energie, 0, 0.4, colors='blue', linewidth=2)
    ax.text(0.42, energie, f'n={niveaus[i]}', verticalalignment='center', fontsize=12)

# Elektronenzustände
elektron_start = y  # Startniveaus (z.B. n=0)
elektron_end = x    # Zielniveaus (z.B. n=3)


elektronen_pos = {
    1: [0.1, 0.2],  # Zwei Elektronen auf n=1
    2: [0.1, 0.2],  # Zwei Elektronen auf n=2
    3: [0.1, 0.2],  # Zwei Elektronen auf n=3
    4: [0.1, 0.2],
    5: [0.1, 0.2],
    6: [0.1, 0.2],
    7: [0.1, 0.2],
}

# Zeichne Elektronen auf den Niveaus
for n, pos in elektronen_pos.items():
    for p in pos:
        ax.plot(p, niveaus_energie[n - 1], 'bo', markersize=10)



# Elektronensprung von n=3 nach n=4 (Elektron wird angeregt)
# Wir verwenden einen roten Pfeil, um den Übergang zu zeigen
ax.arrow(0.2, niveaus_energie[y], 0, niveaus_energie[x]-0.13 - niveaus_energie[y],
         head_width=0.03, head_length=0.1, fc='red', ec='red')

# Text für die Energie des Photons
energie_quanten = niveaus_energie[x] - niveaus_energie[y]
ax.text(0.25, (niveaus_energie[x] + niveaus_energie[y]) / 2, r'$\frac{h^2}{8mL^2} \cdot $'f'{x**2-y**2}' , color='red', fontsize=12)

# Achsen anpassen
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0.5, 7.5)
ax.set_xlabel('Position (Arbitrary)', fontsize=12)
ax.set_ylabel(r'Energie [$\frac{h^2}{8mL^2}$]', fontsize=12)



# Verstecke die Achsen
ax.get_xaxis().set_visible(False)

# Zeige das Diagramm
plt.tight_layout()
plt.show()