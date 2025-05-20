import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import io
import sympy as sp
import scipy.constants as kon
wellenlängeM02bg, IntensitätM02bg0=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Methan_p02_bg0.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängeM02, IntensitätM02=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Methan_p02_probe0.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängeM80, IntensitätM80=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Methan_p080.dpt', skiprows=0, delimiter='\t', unpack=True)
ghf=IntensitätM02/IntensitätM02bg0

plt.subplot(1, 2, 1)
plt.plot(wellenlängeM02, ghf,linewidth='0.3',color='black')
plt.xlim(1280,1320)

# Fourier-Spektrum
plt.subplot(1, 2, 2)
plt.plot(wellenlängeM80, IntensitätM80, linewidth='0.3',color='black')
plt.xlim(2550,2620)



plt.ylim(0.8,1.02)
plt.xlim(2580,2620)
plt.show()