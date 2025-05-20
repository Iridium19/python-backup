import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

Wellenlänge, Absorbtion = np.loadtxt(r'C:\Users\Justus\Desktop\12\Scan_5mM_10mm.csv',delimiter=',',unpack=True)

plt.plot(Wellenlänge, Absorbtion, color='black',label='Absorption')
plt.vlines(x=612, ymin=0, ymax=0.1249, colors='blue', ls='--', lw=1,)
plt.hlines(y=0.1255, xmin=400, xmax=604, colors='blue', linestyles='--', lw=1, label='Absorbtionsmaximum')

plt.vlines(x=604, ymin=0, ymax=0.1249, colors='red', ls='--', lw=1,)
plt.hlines(y=0.1249, xmin=400, xmax=604, colors='red', linestyles='--', lw=1, label='Absorptionsmaximum (VISONlite)')



plt.ylim([0,0.13])
plt.xlim([400,900])
plt.xlabel('Wellenlänge [nm]')
plt.ylabel('Absortion $[-log(I/I_0$)]')
plt.legend(fontsize=8)
plt.show()